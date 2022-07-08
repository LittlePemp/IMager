import os
import random
import re
from typing import Iterable, Optional, Tuple, Union

from PIL import Image
from settings.config import (DISCR_BLOCK, RESIZED_POSTFIX, RESULT_POSTFIX,
                             TEMPLATE_POSTFIX, blocks_cnt, mini_size,
                             results_abs, temp_abs, topics_abs)

from .db_handler import ImagerDB

idb = ImagerDB()


class ImageAlgs:
    def get_avg_colors(self, image_path: str) -> Optional[Tuple[int]]:
        try:
            rgb = self._get_rgb_attrs(image_path)
            attrs = (rgb[0, 0][0], rgb[0, 0][1], rgb[0, 0][2])
            return attrs
        except Exception as e:
            print(e)

    def get_near_image(self,
                       main_point: list[Union[int, str]],
                       noise_degree=(0, 0)
                       ) -> str:
        near_point = self.__discr_search(main_point, noise_degree)
        near_point_name = near_point[3]
        return near_point_name

    def load_in_hash(self, topic_kw
                     ) -> list[list[list[list[Union[int, str]]]]]:
        images: list[tuple[int, int, int, str]] = idb.get_images(topic_kw)
        self.images_hash = [
            [
                [
                    list() for _ in range(blocks_cnt)]
                for _ in range(blocks_cnt)
            ]
            for _ in range(blocks_cnt)
        ]
        for image in images:
            r_discr = image[0] // DISCR_BLOCK
            g_discr = image[1] // DISCR_BLOCK
            b_discr = image[2] // DISCR_BLOCK
            self.images_hash[r_discr][g_discr][b_discr].append(image)
        return self.images_hash

    def __pythagorean_range(self, first_point: list[Union[int, str]],
                            second_point: list[Union[int, str]],
                            noise_degree=(0, 0)
                            ) -> bool:
        noise_slice = random.randint(noise_degree[0], noise_degree[1])
        return abs(((first_point[0] - second_point[0])**2
                   + (first_point[1] - second_point[1])**2
                   + (first_point[2] - second_point[2])**2)**(1 / 2)
                   - noise_slice)

    def __pythagorean_search(self, main_point: list[Union[int, str]],
                             applicants: Iterable[list[Union[int, str]]],
                             noise_degree=(0, 0)
                             ) -> list[Union[int, str]]:
        suit_point = applicants[0]
        suit_range = self.__pythagorean_range(main_point,
                                              suit_point,
                                              noise_degree)
        for applicant in applicants[1:]:
            applicant_range = self.__pythagorean_range(main_point,
                                                       applicant,
                                                       noise_degree)
            if applicant_range < suit_range:
                suit_range = applicant_range
                suit_point = applicant
        return suit_point

    def __discr_search(self, main_point: list[Union[int, str]],
                       noise_degree) -> list[Union[int, str]]:
        r_main_discr = main_point[0] // DISCR_BLOCK
        g_main_discr = main_point[1] // DISCR_BLOCK
        b_main_discr = main_point[2] // DISCR_BLOCK
        discr_applicants = (
            self.images_hash[r_main_discr][g_main_discr][b_main_discr]
        )
        rgb_vector = [r_main_discr, g_main_discr, b_main_discr]
        expand_deep = 0
        while not discr_applicants:
            expand_deep += 1
            self.__expand_applicants(discr_applicants,
                                     rgb_vector,
                                     expand_deep)
        near_point = self.__pythagorean_search(main_point,
                                               discr_applicants,
                                               noise_degree)
        return near_point

    def __expand_applicants(self, applicants: list[list[Union[int, str]]],
                            rgb_vector: list[int],
                            expand_deep: int
                            ) -> None:
        ''' Расширяем область в 3д '''
        for dim1_passing in range(-expand_deep, expand_deep + 1):
            for dim2_passing in range(-expand_deep, expand_deep + 1):
                for dim3_passing in range(-expand_deep, expand_deep + 1):
                    new_area = [rgb_vector[0] + dim1_passing,
                                rgb_vector[1] + dim2_passing,
                                rgb_vector[2] + dim3_passing]
                    if self.__expand_correct(new_area,
                                             rgb_vector,
                                             expand_deep):
                        applicants.extend(
                            self.images_hash[new_area[0]][new_area[1]][new_area[2]])

    def __expand_correct(self, new_area: list[int],
                         rgb_vector: list[int],
                         expand_deep: int
                         ) -> bool:
        ''' Проверка на возможность расширения.
        1. Не выходит за рамки
        2. Не добавляет имеющиеся области '''
        # Первый пункт
        in_frame = all(list(map(
            lambda dimension: 0 <= dimension <= blocks_cnt - 1,
            new_area)))
        # Второй пункт.
        # Если вычитание модуля изменения с любого
        # измерения глубины добавления == 0, то ОК
        dims_changes = [new_area[dim] - rgb_vector[dim] for dim in range(3)]
        not_repeat = any(list(map(
            lambda dim_change: not (abs(dim_change) - expand_deep),
            dims_changes)))
        verdict = in_frame and not_repeat
        return verdict

    def _get_rgb_attrs(self, image_path: str):
        with Image.open(image_path) as image:
            rgb_attrs = image.resize((1, 1)).load()
        return rgb_attrs


class ImagerEngine(ImageAlgs):
    def __init__(self, topic_kw):
        self.images_hash = self.load_in_hash(topic_kw)
        self.opened_images = {
            img_name:
                Image.open(os.path.join(topics_abs,
                                        topic_kw,
                                        img_name)).resize((mini_size,
                                                           mini_size))
            for img_name in
                [img_info[3] for img_info in idb.get_images(topic_kw)]
        }
        self.topic_kw = topic_kw

    def make_image(self, noise_degree, new_image_size, main_path):
        self.imager_preperation(new_image_size, main_path)
        new_img_path = self.fill_template(noise_degree, main_path)
        return new_img_path

    def fill_template(self, noise_degree, main_path):
        main_img_name = re.search(r'([^/\\&\?]+)\.[^.]+$', main_path).group(1)
        resized_path = os.path.join(temp_abs,
                                    main_img_name + RESIZED_POSTFIX)
        template_path = os.path.join(temp_abs,
                                     main_img_name + TEMPLATE_POSTFIX)
        result_path = os.path.join(results_abs,
                                   main_img_name + RESULT_POSTFIX)
        # GET PIX INFOS
        with Image.open(resized_path) as resized_img:
            width = resized_img.size[0]
            height = resized_img.size[1]
            pixels = resized_img.load()
        # SEARCH ADN PASTE IMAGES
        with Image.open(template_path) as template_img:
            for x in range(width):
                for y in range(height):
                    pixel = pixels[x, y]
                    near_img = self.get_near_image(pixel, noise_degree)
                    template_img.paste(
                        self.opened_images[near_img],
                        (mini_size * x, mini_size * y)
                    )
            template_img.save(result_path)
        return result_path
        # FILTRATE

    def imager_preperation(self, new_image_size, main_path):
        main_img_name = re.search(r'([^/\\&\?]+)\.[^.]+$', main_path).group(1)
        with Image.open(main_path) as main_img:
            # SAVE RESIZED MAIN, FOR AVG PIXELS
            width = main_img.size[0]
            height = main_img.size[1]
            if width > height:
                resized_img = main_img.resize((
                    new_image_size,
                    int(new_image_size * height / width)
                ))
            else:
                resized_img = main_img.resize((
                    int(new_image_size * width / height),
                    new_image_size
                ))
            resized_path = os.path.join(temp_abs,
                                        main_img_name + RESIZED_POSTFIX)
            resized_img.save(resized_path)

            # SAVE TEMPLATE
            imager_w = resized_img.size[0] * mini_size
            imager_h = resized_img.size[1] * mini_size
            template = Image.new('RGB', (imager_w, imager_h))
            template_path = os.path.join(temp_abs,
                                         main_img_name + TEMPLATE_POSTFIX)
            template.save(template_path)

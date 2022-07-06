from typing import Optional, Tuple, Union, Iterable

from PIL import Image
from settings.config import (RES_VOLUME, TEMP_VOLUME, TOPICS_VOLUME, RGB_SIZE, DISCR_BLOCK, blocks_cnt,
                             content_abs, results_abs, temp_abs, topics_abs)


class ImageAlgs:
    def get_avg_colors(self, image_path: str) -> Optional[Tuple[int]]:
        try:
            rgb = self._get_rgb_attrs(image_path)
            attrs = (rgb[0, 0][0], rgb[0, 0][1], rgb[0, 0][2])
            return attrs
        except Exception as e:
            print(e)

    def get_near_image(self,
                    main_point: list[Union[int, str]]
                    ) -> str:
        near_point = self.__discr_search(main_point, self.images_hash)
        near_point_name = near_point[3]
        return near_point_name

    def load_in_hash(self, images: list[Union[int, str]]
                    ) -> list[list[list[list[Union[int, str]]]]]:
        self.images_hash = [
            [
                [
                    list() for _ in range(blocks_cnt)]
                for _ in range(blocks_cnt)]
            for _ in range(blocks_cnt)]
        for image in images:
            r_discr = image[0] // DISCR_BLOCK
            g_discr = image[1] // DISCR_BLOCK
            b_discr = image[2] // DISCR_BLOCK
            self.images_hash[r_discr][g_discr][b_discr].append(image)
        return self.images_hash

    def __pythagorean_range(self, first_point: list[Union[int, str]],
                        second_point: list[Union[int, str]]
                        ) -> bool:
        return ((first_point[0] - second_point[0])**2
                + (first_point[1] - second_point[1])**2
                + (first_point[2] - second_point[2])**2)**(1/2)

    def __pythagorean_search(self, main_point: list[Union[int, str]],
                        applicants: Iterable[list[Union[int, str]]]
                        ) -> list[Union[int, str]]:
        suit_point = applicants[0]
        suit_range = self.__pythagorean_range(main_point, suit_point)
        for applicant in applicants[1:]:
            applicant_range = self.__pythagorean_range(main_point, applicant)
            if applicant_range < suit_range:
                suit_range = applicant_range
                suit_point = applicant
        return suit_point

    def __discr_search(self, main_point: list[Union[int, str]]
                    ) -> list[Union[int, str]]:
        r_main_discr = main_point[0] // DISCR_BLOCK
        g_main_discr = main_point[1] // DISCR_BLOCK
        b_main_discr = main_point[2] // DISCR_BLOCK
        discr_applicants = self.images_hash[r_main_discr][g_main_discr][b_main_discr]
        rgb_vector = [r_main_discr, g_main_discr, b_main_discr]
        expand_deep = 0
        while not discr_applicants:
            expand_deep += 1
            self.__expand_applicants(discr_applicants,
                            self.images_hash,
                            rgb_vector,
                            expand_deep)
        near_point = self.__pythagorean_search(main_point, discr_applicants)
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
                    if self.__expand_correct(new_area, rgb_vector, expand_deep):
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
        image = Image.open(image_path)
        return image.resize((1, 1)).load()


class ImagerEngine(ImageAlgs):
    def __init__(self, keyword):
        self.images_hash: list[list[list[list[Union[int, str]]]]] = self.load_in_hash()
        self.keyword = keyword

    def make_image():
        pass


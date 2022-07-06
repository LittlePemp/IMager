import os
import shutil
from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from transliterate import slugify
from settings.config import topics_abs, content_abs

from .exceptions.parse_exceptions import EmptyCacheError, NotImagesVolumesError
from .db_handler import ImagerDB


class Links(list):
    def __init__(self) -> None:
        super().__init__()
        self._keyword: Optional[str] = None
        self._slug_keyword: Optional[str] = None

    @property
    def keyword(self) -> str:
        return self._keyword

    @property
    def slug_keyword(self) -> str:
        return self._slug_keyword

    @keyword.setter
    def keyword(self, value: str) -> None:
        self._keyword = value
        #  Тут кринж из-за slugify, он не транслитит, если все трансы
        self._slug_keyword = slugify(self.keyword + 'А')[:-1]


class ParserFonwall:
    URL = 'https://fonwall.ru/search?q='
    IMG_ITEM_CLASS = 'photo-item__img'
    LINK_ATTR = 'data-big-src'

    def __init__(self):
        self.links = Links()
        self._parse_status: bool = False

    def change_parse_status(self) -> None:
        if len(self.links):
            self._parse_status ^= True

    def parse(self, keyword: str) -> None:
        self.links.keyword = keyword
        url_key = ParserFonwall.URL + keyword
        try:
            self.__parse_pages(url_key)
        except:
            pass
        print(f'Запарсено {len(self.links)}'
              f' изображений - {self.links.keyword}')
        self.change_parse_status()

    def __parse_pages(self, url_key: str) -> None:
        page_number = 0
        is_images = True
        while is_images:
            page_number += 1
            url_key_page = f'{url_key}&page={page_number}'
            is_images = self.__parse_links(url_key_page)

    def __parse_links(self, url_key_page: str) -> bool:
        img_html_attrs = self.__get_img_html_attrs(url_key_page)
        if len(img_html_attrs) <= 1:
            return False
        self.__fill_links(img_html_attrs)
        return True

    def __get_img_html_attrs(self, url_key_page: str) -> list:
        html = requests.get(url_key_page).text
        soup = BeautifulSoup(html, 'html.parser')
        img_html_attrs = soup.findAll(
            'img',
            {'class': ParserFonwall.IMG_ITEM_CLASS}
        )
        return img_html_attrs

    def __fill_links(self, img_html_attrs: BeautifulSoup) -> None:
        for image in img_html_attrs:
            href = str(image.get(ParserFonwall.LINK_ATTR))
            self.links.append(href)

    @property
    def parse_status(self) -> bool:
        return self._parse_status


class DownloaderFonwall(ParserFonwall):
    def __init__(self) -> None:
        super().__init__()
        self.images_topic_path: Optional[str] = None

    def parse(self, keyword: str) -> None:
        try:
            super().parse(keyword)
        except:
            pass
        self.images_topic_path = os.path.join(topics_abs,
                                              self.links.slug_keyword)

    def download_from_cache(self) -> None:
        if not self.parse_status:
            raise EmptyCacheError('Выполните парсинг, чтобы заполнить кеш')
        self.__make_topic_volume()
        self.__passing_links()


    def __passing_links(self) -> None:
        images_in_volume = self.get_images_in_volume()
        for image_link in self.links:
            photo_name = image_link[image_link.rfind('/')
                                    :image_link.rfind('?')]
            if photo_name not in images_in_volume:
                self.__write_file(image_link, photo_name)

    def __write_file(self, image_link: str, photo_name: str) -> None:
        photo_path = f'{self.images_topic_path}/{photo_name}'
        with open(photo_path, "wb") as image_file:
            content = self.__get_image_content(image_link)
            image_file.write(content)

    def __get_image_content(self, image_link: str) -> bytes:
        request = requests.get(image_link)
        content = request.content
        return content

    def __make_topic_volume(self) -> None:
        if not os.path.exists(topics_abs):
            os.mkdir(topics_abs)
        if self.links.slug_keyword not in os.listdir(topics_abs):
            os.mkdir(self.images_topic_path)

    def get_images_in_volume(self) -> List[str]:
        ''' /<photo_name> '''
        topic_dir = os.listdir(self.images_topic_path)
        formated_topic_dir = ['/' + photo_name for photo_name in topic_dir]
        return formated_topic_dir

    def del_all_volumes(self) -> None:
        ''' Добавить количество элементов в def volume_content
            И сделать словарь из волюмес, возможно отдельный класс
        '''
        if topics_abs not in os.listdir(content_abs):
            raise NotImagesVolumesError('Удалять нечего')
        volumes = ', '.join(os.listdir(topics_abs))
        shutil.rmtree(topics_abs)
        print('Удалены: ', volumes)

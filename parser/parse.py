import os
import requests
from bs4 import BeautifulSoup
from transliterate import slugify

from parse_exceptions import EmptyCacheError


IMG_VOLUMES_NAME = 'images_volume'
VOLUME_ROOT = '../'
VOLUMES_PATH = VOLUME_ROOT + IMG_VOLUMES_NAME


class Links:
    def __init__(self) -> None:
        self._all_links: list = list()
        self._count: int = 0
        self._keyword: str = 'Empty'
        self._slug_keyword: str = 'Empty'

    def add(self, value: str) -> None:
        self._all_links.append(value)
        self._count += 1

    def clear(self) -> None:
        self.__init__()

    def get(self) -> list:
        return self._all_links

    @property
    def count(self) -> int:
        return self._count

    @property
    def keyword(self) -> None:
        return self._keyword

    @property
    def slug_keyword(self) -> None:
        return self._slug_keyword

    @keyword.setter
    def keyword(self, value: str) -> None:
        self._keyword = value
        self._slug_keyword = slugify(self._keyword)


class ParserFonwall:
    URL = 'https://fonwall.ru/search?q='
    IMG_ITEM_CLASS = 'photo-item__img'
    LINK_ATTR = 'data-big-src'

    def __init__(self):
        self.links = Links()
        self._parse_status: bool = False

    def change_parse_status(self) -> None:
        if self.links.count:
            self._parse_status ^= True

    def parse(self, keyword: str) -> int:
        self.links.keyword = keyword
        url_key = ParserFonwall.URL + keyword
        try:
            self.__parse_pages(url_key)
        except Exception:
            pass
        self.change_parse_status()
        return self.parse_status

    def __parse_pages(self, url_key: str) -> None:
        page_number = 0
        is_images = True
        while is_images:
            page_number += 1
            url_key_page = f'{url_key}&page={page_number}'
            is_images = self.__parse_links(url_key_page)

    def __parse_links(self, url_key_page: str) -> bool:
        img_html_attrs = self.___get_img_html_attrs(url_key_page)
        if len(img_html_attrs) <= 1:
            return False
        self.__fill_links(img_html_attrs)
        return True

    def ___get_img_html_attrs(self, url_key_page: str) -> list:
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
            self.links.add(href)

    @property
    def parse_status(self):
        return self._parse_status


class DownloaderFonwall(ParserFonwall):
    def __init__(self) -> None:
        super().__init__()
        self.images_topic_path = 'Empty'

    def parse(self, keyword: str) -> int:
        status = super().parse(keyword)
        self.images_topic_path = f'{VOLUMES_PATH}/{self.links.slug_keyword}'
        return status

    def download_from_cache(self) -> None:
        if not self.links.count:  # Заменить на парсе статус
            raise EmptyCacheError('Выполните парсинг, чтобы заполнить кеш')
        self.__make_img_volume()
        for image_link in self.links.get():
            self.__write_file(image_link)

    def __write_file(self, image_link: str) -> None:
        photo_name = image_link[image_link.rfind('/'):image_link.rfind('?')]
        photo_path = f'{self.images_topic_path}/{photo_name}'
        content = self.__get_image_content(image_link)
        with open(photo_path, "wb") as image_file:
            image_file.write(content)

    def __get_image_content(self, image_link) -> str:
        request = requests.get(image_link)
        content = request.content
        return content

    def __make_img_volume(self) -> None:
        if IMG_VOLUMES_NAME not in os.listdir(VOLUME_ROOT):
            os.mkdir(VOLUMES_PATH)
        if self.links.slug_keyword not in os.listdir(VOLUMES_PATH):
            os.mkdir(self.images_topic_path)

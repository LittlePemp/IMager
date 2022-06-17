import os

from PIL import Image
from typing import Optional, Tuple

import config
from db_handler import ImagerDB
from parse import DownloaderFonwall


CONTENT_ROOT = config.CONTENT_ROOT
CROPPED_FILE_NAME = config.DEFAULT_CROPPED_FILE_NAME
IMAGER_SOURCE_NAME = config.DEFAULT_IMAGER_SOURCE
RESOURCE_VOLUME_NAME = config.DEFAULT_RESOURCE_VOLUME_NAME
RESULT_IMAGE_NAME = config.DEFAULT_RESULT_IMAGE_NAME
RESULT_VOLUME_NAME = config.DEFAULT_RESULT_VOLUME_NAME
TEMPLATE_NAME = config.DEFAULT_TEMPLATE_NAME

SOURCE_PATH = CONTENT_ROOT + IMAGER_SOURCE_NAME
RESULT_PATH = f'{SOURCE_PATH}/{RESULT_VOLUME_NAME}'
RESOURCE_PATH = f'{SOURCE_PATH}/{RESOURCE_VOLUME_NAME}'


class ImageHandler:
    def get_avg_colors(self, image_path: str) -> Optional[Tuple[int]]:
        try:
            rgb = self._get_rgb_attrs(image_path)
            attrs = (rgb[0, 0][0], rgb[0, 0][1], rgb[0, 0][2])
            return attrs
        except Exception as e:
            print(e)

    def _get_rgb_attrs(self, image_path: str):
        image = Image.open(image_path)
        return image.resize((1, 1)).load()


class ImagerModel:
    def __init__(self) -> None:
        self.dirs_tree_init()
        self.idb = ImagerDB()
        self.parser = DownloaderFonwall()
        
    def get_new_images(self, keyword: str) -> None:
        self.parser.parse(keyword)
        self.parser.download_from_cache()
        keyword = self.parser.links.slug_keyword
        self.idb.fill_db(keyword)

    def dirs_tree_init(self) -> None:
        if IMAGER_SOURCE_NAME not in os.listdir(CONTENT_ROOT):
            os.mkdir(SOURCE_PATH)
        available_dirs = os.listdir(SOURCE_PATH)
        if RESULT_VOLUME_NAME not in available_dirs:
            os.mkdir(RESULT_PATH)
        if RESOURCE_VOLUME_NAME not in available_dirs:
            os.mkdir(RESOURCE_PATH)

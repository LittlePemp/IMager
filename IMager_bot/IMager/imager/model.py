import os
from typing import Optional, Tuple

from PIL import Image
from settings.config import (RES_VOLUME, TEMP_VOLUME, TOPICS_VOLUME,
                             content_abs, results_abs, temp_abs, topics_abs)

from .db_handler import ImagerDB
from .parse import DownloaderFonwall


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
        content_content = os.listdir(content_abs)
        if TOPICS_VOLUME not in content_content:
            os.mkdir(topics_abs)
        if RES_VOLUME not in content_content:
            os.mkdir(results_abs)
        if TEMP_VOLUME not in content_content:
            os.mkdir(temp_abs)

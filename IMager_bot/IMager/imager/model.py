import os
from typing import Optional, Tuple

from PIL import Image
from settings.config import (RES_VOLUME, TEMP_VOLUME, TOPICS_VOLUME,
                             content_abs, results_abs, temp_abs, topics, topics_abs, noise_degrees, new_image_sizes)

from .db_handler import ImagerDB
from .parse import DownloaderFonwall
from .image_assembly import ImagerEngine


class ImagerModel:
    def __init__(self) -> None:
        self.dirs_tree_init()
        self.idb = ImagerDB()
        self.parser = DownloaderFonwall()
        self.ies = self.get_imager_engines()

    def get_imager_engines(self):
        ies = dict()
        print('Начинаем прогрузку в оперативу')
        for topic_kw in topics.values():
            ies[topic_kw] = ImagerEngine(topic_kw)
            print(f'{topic_kw} прогружены')
        print('Все фото прогружены в оперативку')
        return ies
            
    def get_new_image(self, data):
        topic_kw = topics[data['topic_name']]
        noise_degree = noise_degrees[data['noise_degree']]
        new_image_size = new_image_sizes[data['new_image_size']]
        user_image_path = data['image_path']
        new_image_path = self.ies[topic_kw].make_image(noise_degree, new_image_size, user_image_path)
        return new_image_path

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

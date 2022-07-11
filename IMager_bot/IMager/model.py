import os
from typing import Optional, Tuple

from PIL import Image
from settings.config import (RES_VOLUME, TEMP_VOLUME, TOPICS_VOLUME,
                             content_abs, new_image_sizes, noise_degrees,
                             results_abs, temp_abs, topics, topics_abs)

from .db_handler import ImagerDB
from .image_assembly import ImagerEngine
from .parse import DownloaderFonwall


class ImagerModel:
    def __init__(self) -> None:
        self.__dirs_tree_init()
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
        new_image_path = self.ies[topic_kw].make_image(noise_degree,
                                                       new_image_size,
                                                       user_image_path)
        return new_image_path

    def __dirs_tree_init(self) -> None:
        content_content = os.listdir(content_abs)
        if TOPICS_VOLUME not in content_content:
            os.mkdir(topics_abs)
        if RES_VOLUME not in content_content:
            os.mkdir(results_abs)
        if TEMP_VOLUME not in content_content:
            os.mkdir(temp_abs)

import asyncio
import os

from settings.config import (RES_VOLUME, TEMP_VOLUME, TOPICS_VOLUME,
                             content_abs, new_image_sizes, noise_degrees,
                             results_abs, temp_abs, topics, topics_abs)
from .image_assembly import ImagerEngine
from .parse import DownloaderFonwall


class ImagerModel:
    def __init__(self) -> None:
        self.parser = DownloaderFonwall()
        self.ies = self.__get_imager_engines()
        self.__dirs_tree_init()

    async def get_new_image(self, data):
        try:
            topic_kw = topics[data['topic_name']]
            noise_degree = noise_degrees[data['noise_degree']]
            new_image_size = new_image_sizes[data['new_image_size']]
            user_image_path = data['image_path']
        except:
            return None
        await asyncio.sleep(10)
        new_image_path = self.ies[topic_kw].make_image(noise_degree,
                                                       new_image_size,
                                                       user_image_path)
        return new_image_path

    def __get_imager_engines(self):
        ies = dict()
        print('Начинаем прогрузку в оперативу')
        for topic_kw in topics.values():
            ies[topic_kw] = ImagerEngine(topic_kw)
            print(f'{topic_kw} прогружены')
        print('Все фото прогружены в оперативку')
        return ies

    def __dirs_tree_init(self) -> None:
        content_content = os.listdir(content_abs)
        if TOPICS_VOLUME not in content_content:
            os.mkdir(topics_abs)
        if RES_VOLUME not in content_content:
            os.mkdir(results_abs)
        if TEMP_VOLUME not in content_content:
            os.mkdir(temp_abs)

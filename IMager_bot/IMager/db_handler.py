import logging
import os
import sqlite3
from typing import Optional

from PIL import Image
from settings.config import content_abs, db_abs, topics_abs

logger = logging.getLogger(__name__)


class ImagerDB:
    def __init__(self):
        self.db_init()
        self.connection = sqlite3.connect(db_abs)
        self.cursor = self.connection.cursor()

    def db_init(self):
        if not os.path.exists(content_abs):
            os.makedirs(content_abs)
        if not os.path.exists(db_abs):
            with open(db_abs, 'w') as _:
                logger.info('Создана БД')

    def create_table(self, table_name: str) -> None:
        try:
            request_text = (f'CREATE TABLE IF NOT EXISTS {table_name}('
                            'r INTEGER NOT NULL,'
                            'g INTEGER NOT NULL,'
                            'b INTEGER NOT NULL,'
                            'img_name TEXT PRIMARY KEY);')
            logger.info(f'Таблица ({table_name}) успешно создана')
            self.cursor.execute(request_text)
        except Exception as er:
            logger.error(f'Ошибка создания таблицы {table_name}: {er}')

    def db_delete(self) -> None:
        try:
            os.remove(db_abs)
            logger.info('Удалена БД')
        except Exception as er:
            logger.error(f'Ошибка удаления БД: {er}')

    def drop_table(self, table_name: str) -> None:
        request_text = f'DROP TABLE {table_name};'
        try:
            self.cursor.execute(request_text)
            logger.info(f'Таблица ({table_name}) успешно удалена')
        except sqlite3.OperationalError:
            logger.error(f'Обшибка удаления таблицы - {table_name}')

    def fill_db(self, keyword: str) -> None:
        self.drop_table(keyword)
        self.create_table(keyword)
        self.__passing_keyword_images(keyword)

    def get_images(self, keyword) -> list[list[int]]:
        request_text = f'SELECT * FROM {keyword}'
        self.cursor.execute(request_text)
        result = self.cursor.fetchall()
        return result

    def get_tables(self):
        request_text = "SELECT name FROM sqlite_master WHERE type='table';"
        self.cursor.execute(request_text)
        tables = [response[0] for response in self.cursor.fetchall()]
        return tables

    def _get_rgb_attrs(self, image_path: str):
        with Image.open(image_path) as image:
            avg_rgb = image.resize((1, 1)).load()
        return avg_rgb

    def __get_avg_colors(self, image_path: str) -> Optional[tuple[int]]:
        try:
            rgb = self._get_rgb_attrs(image_path)
            attrs = (rgb[0, 0][0], rgb[0, 0][1], rgb[0, 0][2])
            return attrs
        except Exception as er:
            logger.warning(f'Ошибка чтения изображения ({image_path}): {er}')

    def __passing_keyword_images(self, keyword: str) -> None:
        kw_volume = os.path.join(topics_abs, keyword)
        images_names = os.listdir(kw_volume)
        for image_name in images_names:
            image_path = os.path.join(kw_volume, image_name)
            image_attrs = self.__get_avg_colors(image_path)
            if image_attrs is not None:
                image_attrs += (image_name, )
                request = ('INSERT INTO '
                           f'{keyword}('
                           'r,'
                           'g,'
                           'b,'
                           'img_name)'
                           f'VALUES {image_attrs}')
                try:
                    self.cursor.execute(request)
                except Exception as er:
                    logger.error(f'Ошибка чтения таблицы: {er}')
        self.connection.commit()

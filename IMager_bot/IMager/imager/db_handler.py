import sqlite3
import os

from settings.config import DB_NAME, db_abs, content_abs, topics_abs
from .image_assembly import ImageEngine as IE


class ImagerDB:
    def __init__(self):
        self.db_init()
        self.connection = sqlite3.connect(db_abs)
        self.cursor = self.connection.cursor()
        self.image_handler = IE()

    def db_init(self):
        if DB_NAME not in os.listdir(content_abs):
            with open(db_abs, 'w') as _:
                print('Создана БД')

    def create_table(self, table_name: str) -> None:
        request_text = (f'CREATE TABLE IF NOT EXISTS {table_name}('
                        'r INTEGER NOT NULL,'
                        'g INTEGER NOT NULL,'
                        'b INTEGER NOT NULL,'
                        'img_name TEXT PRIMARY KEY);')
        self.cursor.execute(request_text)

    def db_delete(self) -> None:
        try:
            os.remove(db_abs)
        except:
            pass

    def drop_table(self, table_name: str) -> None:
        request_text = f'DROP TABLE {table_name};'
        try:
            self.cursor.execute(request_text)
        except sqlite3.OperationalError:
            pass

    def fill_db(self, keyword: str) -> None:
        self.drop_table(keyword)
        self.create_table(keyword)
        self.__passing_keyword_images(keyword)

    def __passing_keyword_images(self, keyword: str) -> None:
        kw_volume = os.path.join(topics_abs, keyword)
        images_names = os.listdir(kw_volume)
        for image_name in images_names:
            image_path = os.path.join(kw_volume, image_name)
            image_attrs = self.image_handler.get_avg_colors(image_path)
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
                except Exception as e:
                    print(e)
        self.connection.commit()

import sqlite3
import os

import config
import image_assembly as ia
import parse


DB_ROOT = config.CONTENT_ROOT
DB_NAME = config.DB_NAME
DB_PATH = DB_ROOT + DB_NAME
VOLUMES_PATH = parse.VOLUMES_PATH

class ImagerDB:
    def __init__(self):
        self.db_init()
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()
        self.image_handler = ia.ImageHandler()

    def db_init(self):
        if DB_NAME not in os.listdir(DB_ROOT):
            with open(DB_PATH, 'w') as db_file:
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
            os.remove(DB_PATH)
        except:
            pass

    def drop_table(self, table_name: str) -> None:
        request_text = f'DROP TABLE {table_name}';
        try:
            self.cursor.execute(request_text)
        except sqlite3.OperationalError:
            pass

    def fill_db(self, keyword: str) -> None:
        self.drop_table(keyword)
        self.create_table(keyword)
        self.__passing_keyword_images(keyword)


    def __passing_keyword_images(self, keyword: str) -> None:
        kw_volume = f'{VOLUMES_PATH}/{keyword}'
        images_names = os.listdir(kw_volume)
        executables = list()
        for image_name in images_names:
            image_path = f'{kw_volume}/{image_name}'
            image_attrs = self.image_handler.get_avg_colors(image_path)
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

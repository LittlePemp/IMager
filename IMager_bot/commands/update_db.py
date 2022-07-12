import os

from IMager.db_handler import ImagerDB as IDB
from settings.config import topics_abs

idb = IDB()
tables = idb.get_tables()

topics = os.listdir(topics_abs)
print('Начинается заполнение')
for topic in topics:
    idb.fill_db(topic)
    print(f'{topic} загружен в БД!')

import os

from IMager.db_handler import ImagerDB as IDB
from settings.config import topics_abs
from settings.command_exceptions import NotTopicsVolume

idb = IDB()
tables = idb.get_tables()
try:
    topics = os.listdir(topics_abs)
except FileNotFoundError:
    raise NotTopicsVolume('Загрузите картинки')
print('Начинается заполнение')
for topic in topics:
    idb.fill_db(topic)
    print(f'{topic} загружен в БД!')

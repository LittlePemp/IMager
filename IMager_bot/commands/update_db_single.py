import os

from IMager.db_handler import ImagerDB as IDB
from settings.config import topics_abs
from settings.command_exceptions import NotTopicsVolume

idb = IDB()
print('Выберите имя директории:')
try:
    topics = os.listdir(topics_abs)
except FileNotFoundError:
    raise NotTopicsVolume('Загрузите картинки')
for topic_id, topic_name in enumerate(topics):
    print(f'{topic_id}: {topic_name}')
topic_id = input()
while not (topic_id.isdigit() and (0 <= int(topic_id) < len(topics))):
    print('Введите предложенный вариант')
    topic_id = input()
topic_id = int(topic_id)
topic_name = topics[topic_id]
idb.fill_db(topic_name)

import logging
import os

from IMager.db_handler import ImagerDB as IDB
from IMager.image_assembly import ImagerEngine as IE
from settings.config import (new_image_sizes, noise_degrees, results_abs,
                             temp_abs, topics_abs)

logger = logging.getLogger(__name__)

if not os.path.exists(topics_abs):
    os.mkdir(topics_abs)
    logger.info(f'Путь создан: {topics_abs}')
if not os.path.exists(results_abs):
    os.mkdir(results_abs)
    logger.info(f'Путь создан: {results_abs}')
if not os.path.exists(temp_abs):
    os.mkdir(temp_abs)
    logger.info(f'Путь создан: {temp_abs}')

idb = IDB()
tables = idb.get_tables()
print('Выберите набор картинок для заполнения:')
for topic_id, topic_name in enumerate(tables):
    print(f'{topic_id}: {topic_name}')
choice_id = input()
while not (choice_id.isdigit() and (0 <= int(choice_id) < len(tables))):
    print('Введите предложенный вариант:')
    choice_id = input()
choice_id = int(choice_id)
topic_kw = tables[choice_id]

print('Введите абсолютный путь к собираемому изображению (*.jpg, *.jpeg):')
test_main_img = input()
while not os.path.exists(test_main_img) or test_main_img[-1] != 'g':
    print('Проверьте корректность пути:')
    test_main_img = input()

noise_degree = noise_degrees['Среднее']
new_image_size = new_image_sizes['Большое']
image_path = test_main_img

print('Стартуем...')
ie = IE(topic_kw)
new_image_path = ie.make_image(noise_degree, new_image_size, test_main_img)
print(f'Результат: ({new_image_path})')

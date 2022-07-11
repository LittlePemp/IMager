from IMager.db_handler import ImagerDB
from IMager.parse import DownloaderFonwall as DF
from transliterate import slugify


def get_info(tables):
    tables = idb.get_tables()
    search_name = ''
    while not search_name:
        search_name = input('Введите тему скачиваемых картинок: ')
    default_table_name = slugify(search_name + 'a')[:-1]
    print('В какую таблицу сохраним результаты: ')
    if default_table_name not in tables:
        print(f'0: Создать новую ({default_table_name})')
    for table_id, table_name in enumerate(tables):
        print(f'{table_id + 1}: {table_name}')
    analog_id = input()
    while not (analog_id.isdigit() and (0 <= int(analog_id) <= len(tables))):
        print('Введите предложенный вариант')
        analog_id = input()
    analog_id = int(analog_id)
    if analog_id == 0:
        analog = default_table_name
    else:
        analog = tables[analog_id - 1]
    return search_name, analog


df = DF()
idb = ImagerDB()
tables = idb.get_tables()
search_name, analog = get_info(tables)
print('Парсим...')
df.parse(search_name, analog=analog)
print('Качаем... Для остановки скачивания прожмите (Ctrl + c)')
df.download_from_cache()

print('Скачали что могли. Сечас заполним БД')
idb.fill_db(analog)
print('Все прошло успешно!')

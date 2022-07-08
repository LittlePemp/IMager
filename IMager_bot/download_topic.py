from IMager.imager.db_handler import ImagerDB
from IMager.imager.parse import DownloaderFonwall as DF

if __name__ == '__main__':
    df = DF()
    anlg = 'koty'
    search_name = 'Кошки'
    print('Парсим...')
    df.parse(search_name, analog=anlg)
    print('Качаем...')
    df.download_from_cache()

    print('Скачали что могли. Сечас заполним БД')
    idb = ImagerDB()
    idb.fill_db(anlg)

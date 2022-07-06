from IMager.imager.db_handler import ImagerDB
from IMager.imager.parse import DownloaderFonwall as DF

if __name__ == '__main__':
    topic_name = input('Введите название темы: ')
    print('OK. Чтобы остановить парсинг прожмите комбинацию (Ctrl + C)')
    df = DF()
    df.parse(topic_name)
    df.download_from_cache()
    
    print('Скачали что могли. Сечас заполним БД')
    idb = ImagerDB()
    idb.fill_db(df.links.slug_keyword)

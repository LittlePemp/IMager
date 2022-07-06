import sys
from os.path import abspath, join


# sys settings
host_platform = sys.platform
dotenv_path = join(abspath(''), '.env')

# GENERAL
CONTENT_VOLUME = 'content'
content_abs = abspath('content')

# TG KEYBOARDS
topics = {'Котики': 'Koty', 'Аниме': 'Anime'}
noise_degrees = {'Нет': (0, 0), 'Среднеe': (20, 50), 'Сильно': (60, 100)}
new_image_sizes = {'Маленькое': 25, 'Среднее': 50, 'Большое': 100}

# TG VOLUMES
USERS_IMAGES = 'users_images'
users_images_abs = join(content_abs, USERS_IMAGES)

# PARSER VOLUMES
IMG_VOLUMES_NAME = 'images_volume'
img_bolumes_abs = join(content_abs, IMG_VOLUMES_NAME)

# IMAGER VOLUMES
TEMP_VOLUME = 'TEMP'
TOPICS_VOLUME = 'topics'

# DEFAULT_RESOURCE_VOLUME_NAME = 'resources'
RES_VOLUME = 'results'
temp_abs = join(content_abs, TEMP_VOLUME)
topics_abs = join(content_abs, TOPICS_VOLUME)
results_abs = join(content_abs, RES_VOLUME)


# IMAGE_ASSEMBLY
CROPPED_POSTFIX = 'cr.png'
RESULT_POSTFIX = 'res.png'
TEMPLATE_POSTFIX = 'tmpl.png'
RGB_SIZE = 256
DISCR_BLOCK = 32
mini_size = 45
blocks_cnt = RGB_SIZE // DISCR_BLOCK

# DB HANDLER
DB_NAME = 'imager.db'
db_abs = join(content_abs, DB_NAME)

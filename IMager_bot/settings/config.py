import sys
from os.path import abspath, join


# sys settings
host_platform = sys.platform
dotenv_path = join(abspath(''), '.env')

# GENERAL
CONTENT_VOLUME = 'content'
content_abs = abspath('content')

# TG KEYBOARDS
topics = ['Котики', 'Аниме']
noise_degrees = ['Нет', 'Средне', 'Сильно']

# TG VOLUMES
USERS_PHOTOS = 'users_photos'
users_photos_abs = join(content_abs, USERS_PHOTOS)

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

# DB HANDLER
DB_NAME = 'imager.db'
db_abs = join(content_abs, DB_NAME)

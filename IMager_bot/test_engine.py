from IMager.imager.model import ImagerModel as IM
from settings.config import topics, noise_degrees, new_image_sizes


im = IM()

test_main_img = 'C:\\Users\\David\\Desktop\\Projects\\IMager\\content\\users_images\\123.jpg'
data = {
    'topic_name': 'Котики',
    'noise_degree': 'Сильно',
    'new_image_size': 'Маленькое',
    'image_path': test_main_img,
}

new_image_path = im.get_new_image(data)


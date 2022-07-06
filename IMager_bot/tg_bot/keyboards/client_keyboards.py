from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from settings.config import topics, noise_degrees, new_image_sizes

to_start_button = KeyboardButton('В начало')

# Topic buttons
topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for topic in topics.keys():
    topic_keyboard.add(topic)
topic_keyboard.add(to_start_button)

# Noise degree buttons
noise_degrees_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for noise_degree in noise_degrees.keys():
    noise_degrees_keyboard.insert(noise_degree)
noise_degrees_keyboard.add(to_start_button)

# Image size buttons
new_image_size_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for new_image_size in new_image_sizes.keys():
    new_image_size_keyboard.insert(new_image_size)
new_image_size_keyboard.add(to_start_button)

# Photo buttons
photo_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
photo_keyboard.add(to_start_button)

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from settings.config import topics


to_start_button = KeyboardButton('Начало')

# Topic buttons
topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
for topic in topics:
    topic_keyboard.add(topic)

# Noise degree buttons
noise_degrees_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True)

for noise_degree in range(8):  # INCONFIG
    noise_degrees_keyboard.insert(str(noise_degree))
noise_degrees_keyboard.add(to_start_button)

photo_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True)
photo_keyboard.add(to_start_button)

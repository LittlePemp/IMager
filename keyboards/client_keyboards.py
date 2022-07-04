from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

to_start_button = KeyboardButton('Начало')

# Topic buttons
cats_button = KeyboardButton('Котики')
anime_button = KeyboardButton('Аниме')

topic_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
topic_keyboard.add(cats_button).add(anime_button).add(to_start_button)

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

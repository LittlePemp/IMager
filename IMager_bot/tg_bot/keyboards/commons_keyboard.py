from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_button = KeyboardButton('/Начать')
help_button = KeyboardButton('/Поддержать')
support_button = KeyboardButton('/Помощь')

common_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
common_keyboard.add(start_button).add(help_button).insert(support_button)

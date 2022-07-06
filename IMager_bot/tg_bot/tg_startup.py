import os

from aiogram.utils import executor
from settings.config import users_photos_abs

from tg_bot.create_bot import get_dp
from tg_bot.handlers import client, commons


def make_user_volume():
    if not os.path.exists(users_photos_abs):
        os.makedirs(users_photos_abs)


async def on_startup(_):
    make_user_volume()
    print('START BOT')


def start_bot():
    dp = get_dp()
    client.register_handlers(dp)
    commons.register_handlers(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

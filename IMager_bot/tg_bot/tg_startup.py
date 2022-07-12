import logging
import os

from aiogram.utils import executor
from settings.config import users_images_abs

from tg_bot.create_bot import get_dp
from tg_bot.handlers import client, commons

logger = logging.getLogger(__name__)


def make_user_volume():
    if not os.path.exists(users_images_abs):
        os.makedirs(users_images_abs)


async def on_startup(_):
    make_user_volume()
    logger.info('START BOT')


def start_bot():
    dp = get_dp()
    client.register_handlers(dp)
    commons.register_handlers(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

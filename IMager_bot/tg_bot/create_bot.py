import logging
import os

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv
from settings.config import dotenv_path


def get_dp():
    load_dotenv(dotenv_path)

    TOKEN = os.environ.get('TOKEN')
    logging.basicConfig(level=logging.INFO)

    storage = MemoryStorage()

    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=storage)
    return dp

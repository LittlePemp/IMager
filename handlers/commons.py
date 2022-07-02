from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import common_keyboard


async def command_start(message: types.Message):
    await message.answer(
        'Привет! Я IMager, Бот, который создаст тебе картинку'
        ' из других картинок! Используй кнопочки снизу ⬇ '
        'и следуй инструкциям 😉',
        reply_markup=common_keyboard)


async def command_devsupport(message: types.Message):
    await message.answer(
        'Привет! Помогите',
        reply_markup=common_keyboard)


async def unknown_answer(message: types.Message):
    await message.reply(
        'Я не знаю такой команды(\nЖмякните на предложенный выбор',
        reply_markup=common_keyboard)


def register_handlers(dp: Dispatcher):
    ''' Регистрируем без декораоров '''
    dp.register_message_handler(command_start, commands=[
                                                         'start',
                                                         'help',
                                                         'Помощь'])
    dp.register_message_handler(command_devsupport, commands=[
                                                              'devsupport',
                                                              'Поддержать'])
    dp.register_message_handler(unknown_answer)

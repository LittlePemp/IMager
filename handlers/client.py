from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from datetime import datetime
import time

from keyboards import topic_keyboard, noise_degrees_keyboard, common_keyboard

from create_bot import bot


topics_various = ['Котики', 'Аниме']  # INCONFIG
uncorrect_answer = 'Пожалуйста, выберите из предложенного'
IMAGES_VOLUME = '../images/'
name_format = IMAGES_VOLUME + '%Y%m%d_%H%M%s.jpg'


class FSMImager(StatesGroup):
    topic_name = State()
    noise_degree = State()
    photo = State()


async def start_imager(message: types.Message):
    await FSMImager.topic_name.set()
    await message.reply(
        'Выберите набор картинок для заполнения',
        reply_markup=topic_keyboard)


async def read_topic(message: types.Message, state: FSMContext):
    if message.text not in topics_various:
        await message.reply(
            uncorrect_answer,
            reply_markup=topic_keyboard)
    else:
        async with state.proxy() as data:
            data['topic_name'] = message.text
        await FSMImager.next()
        await message.reply(
            'Выберите степень шума* (Рекомендуется 5)\n\n'
            '* Степень шума повлияет на вариативность картинок. '
            'Чем больше степень, тем жвее получится картинка, '
            'пока она разлечима',
            reply_markup=noise_degrees_keyboard)


async def read_noise_degree(message: types.Message, state: FSMContext):
    if not (message.text.isdigit() and (0 <= int(message.text) <= 7)):
        await message.reply(uncorrect_answer)
    else:
        async with state.proxy() as data:
            data['noise_degree'] = message.text
        await FSMImager.next()
        await message.reply(
            'Загрузите фото',
            reply_markup=types.ReplyKeyboardRemove())


async def read_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await download_image(message)
        data['photo_path'] = '123'  # photo_path
    # Test
    await message.reply('Фото успешно загружено. Ожидайте...')
    time.sleep(5)
    await message.answer(
        'Тут возвращается фото',
        reply_markup=common_keyboard)
    await state.finish()


async def download_image(message: types.Message):
    now = datetime.now()
    photo_path = now.strftime(name_format)
    await message.photo[2].download(destination_file=photo_path)  # [2] is LQ


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_imager,
        commands=['Начать'],
        state=None)
    dp.register_message_handler(
        read_topic,
        state=FSMImager.topic_name)
    dp.register_message_handler(
        read_noise_degree,
        state=FSMImager.noise_degree)
    dp.register_message_handler(
        read_photo,
        content_types=['photo'],
        state=FSMImager.photo)

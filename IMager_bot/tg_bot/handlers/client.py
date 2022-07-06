import os
import time
from datetime import datetime

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from settings.config import host_platform, topics, users_images_abs, noise_degrees, new_image_sizes
from tg_bot.keyboards import (common_keyboard, noise_degrees_keyboard,
                              topic_keyboard, new_image_size_keyboard)
from IMager.imager.model import ImagerModel

uncorrect_answer = 'Пожалуйста, выберите из предложенного'
if 'win' in host_platform:
    name_format = os.path.join(users_images_abs, '%Y%m%d_%H%M%S.jpg')
else:
    name_format = os.path.join(users_images_abs, '%Y%m%d_%H%M%s.jpg')

im = ImagerModel()
waited_buff = set()


def to_start(handler):
    async def wrapper_do_twice(message: types.Message, state=None):
        if 'В начало' == message.text:
            await state.finish()
            await message.answer(
                'Начнем с начала...',
                reply_markup=common_keyboard)
        else:
            await handler(message, state)
    return wrapper_do_twice


class FSMImager(StatesGroup):
    topic_name = State()
    noise_degree = State()
    new_image_size = State()
    image = State()


@to_start
async def start_imager(message: types.Message, state=None):
    await FSMImager.topic_name.set()
    await message.reply(
        'Выберите набор картинок для заполнения',
        reply_markup=topic_keyboard)


@to_start
async def read_topic(message: types.Message, state: FSMContext):
    if message.text not in topics.keys():
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


@to_start
async def read_noise_degree(message: types.Message, state: FSMContext):
    if message.text not in noise_degrees.keys():
        await message.reply(uncorrect_answer)
    else:
        async with state.proxy() as data:
            data['noise_degree'] = message.text
        await FSMImager.next()
        await message.reply(
            'Какой будет размер нового фото?',
            reply_markup=new_image_size_keyboard)


@to_start
async def read_new_image_size(message: types.Message, state: FSMContext):
    if message.text not in new_image_sizes.keys():
        await message.reply(uncorrect_answer)
    else:
        async with state.proxy() as data:
            data['new_image_size'] = message.text
        await FSMImager.next()
        await message.reply(
            'Загрузите фото',
            reply_markup=types.ReplyKeyboardRemove())


async def read_image(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if message.from_user.id not in waited_buff:
        waited_buff.add(user_id)

        async with state.proxy() as data:
            image_path = await download_image(message)
            data['image_path'] = image_path
            await message.reply('Фото успешно загружено. Ожидайте...')
            new_image_path = image_path  # im.get_new_image(data)
            await send_new_image(message, new_image_path)
        waited_buff.remove(user_id)
        await state.finish()


async def send_new_image(message: types.Message, new_image_path: str):
    try:
        await message.answer_document(open(new_image_path, 'rb'))
    except:
        await message.answer('Что-то не получилоссь... Повторите позже.', reply_markup=topic_keyboard)


async def download_image(message: types.Message):
    now = datetime.now()
    image_path = now.strftime(name_format)
    await message.photo[2].download(destination_file=image_path)  # [2] is LQ
    return image_path


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
        read_new_image_size,
        state=FSMImager.new_image_size)
    dp.register_message_handler(
        read_image,
        content_types=['photo'],
        state=FSMImager.image)

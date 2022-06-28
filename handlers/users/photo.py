from aiogram import types
from aiogram.utils.exceptions import FileIsTooBig
from loader import dp, bot
from utils import get_photo_name, get_new_file_name, create_user_path


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    try:
        file_path = create_user_path(user_id=message.from_user.id, content_type='photo')
        await message.photo[-1].download(destination_file=f'{file_path}/{get_photo_name()}')
        await bot.send_message(
            text='получил фото',
            chat_id=message.from_user.id
        )
    except FileIsTooBig:
        await bot.send_message(
            text='Я временно не могу сохранять фотографии более <b>20МБ</b>',
            chat_id=message.from_user.id
        )


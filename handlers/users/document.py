from aiogram import types
from aiogram.utils.exceptions import FileIsTooBig
from loader import dp, bot
from utils import get_new_file_name, create_user_path
from pathlib import Path


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def doc_handler(message: types.Message):
    try:
        file_path = create_user_path(user_id=message.from_user.id, content_type='document')
        if not Path.exists(Path(file_path, message.document.file_name)):
            await message.document.download(
                destination_file=Path(file_path, message.document.file_name)
            )
        else:
            await message.document.download(
                destination_file=Path(file_path, get_new_file_name(message.document.file_name))
            )
    except FileIsTooBig:
        await bot.send_message(
            text='Я временно не могу сохранять документы более <b>20МБ</b>',
            chat_id=message.from_user.id
        )
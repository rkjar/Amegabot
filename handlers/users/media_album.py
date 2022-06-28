from aiogram import types
from aiogram.utils.exceptions import FileIsTooBig
from loader import dp, bot
from utils import get_photo_name, get_new_file_name, create_user_path
from pathlib import Path


@dp.message_handler(is_media_group=True, content_types=types.ContentType.ANY)
async def album_handler(message: types.Message, album: list[types.Message]):
    try:
        for file in album:
                file_path = create_user_path(user_id=message.from_user.id, content_type=file.content_type)
                if file.photo:
                    await message.photo[-1].download(
                        destination_file=Path(file_path, get_photo_name())
                    )
                elif file.document:
                    if not Path.exists(Path(file_path, file.document.file_name)):
                        await message.document.download(
                            destination_file=Path(file_path, file.document.file_name)
                        )
                    else:
                        await message.document.download(
                            destination_file=Path(file_path, get_new_file_name(file.document.file_name))
                        )
                else:
                    await bot.send_message(
                        text='Я умею работать только с изображениями и документами',
                        chat_id=message.from_user.id
                    )
    except FileIsTooBig:
        await bot.send_message(
            text='Я временно не могу сохранять файлы более <b>20МБ</b>',
            chat_id=message.from_user.id
        )

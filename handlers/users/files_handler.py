import asyncio
from aiogram import types
from loader import dp, bot
from utils import get_photo_name, get_new_file_name
from pathlib import Path
from aiogram.utils.exceptions import FileIsTooBig


def create_user_path(user_id: int, content_type: str) -> str:
    cur_path = Path(Path.cwd(), 'static', str(user_id), content_type)
    if not Path.exists(cur_path):
        cur_path.mkdir(parents=True, exist_ok=True)
    return cur_path


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
                    await bot.send_message(text='Я умею работать только с изображениями и документами', chat_id=message.from_user.id)
    except FileIsTooBig:
        await bot.send_message(text='Я временно не могу сохранять файлы более <b>20МБ</b>', chat_id=message.from_user.id)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    try:
        file_path = create_user_path(user_id=message.from_user.id, content_type='photo')
        await message.photo[-1].download(destination_file=f'{file_path}/{get_photo_name()}')
        await bot.send_message(text='получил фото',
                               chat_id=message.from_user.id)
    except FileIsTooBig:
        await bot.send_message(text='Я временно не могу сохранять фотографии более <b>20МБ</b>', chat_id=message.from_user.id)



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
        await bot.send_message(text='Получил документ',
                               chat_id=message.from_user.id)
    except FileIsTooBig:
        await bot.send_message(text='Я временно не могу сохранять документы более <b>20МБ</b>',
                               chat_id=message.from_user.id)

@dp.message_handler()
async def text_handler(message: types.Message):
    await asyncio.sleep(10)
    await message.reply(text='hi')




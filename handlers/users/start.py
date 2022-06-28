from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, User
from keyboards.inline import branches_keyboard
from pathlib import Path


DB = User(Path(Path.cwd(), 'static', 'database.db'))


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    # Command '/start' handler
    # Connecting database, adding telegram id to db
    await DB.create_table()
    if not await DB.user_existing(message.from_user.id):
        await DB.add_user(message.from_user.id)

    await bot.send_message(text=f'Отправьте файл до <b>20МБ</b>\n'
                                f'Выберите филиал',
                           chat_id=message.from_user.id,
                           reply_markup=branches_keyboard)
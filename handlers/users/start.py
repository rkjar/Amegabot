from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, User
from keyboards.inline import branches_keyboard
from pathlib import Path


DB = User(Path(Path.cwd(), 'static', 'database.db'))
MSG_ID: int = 0


def get_message_id() -> int:
    global MSG_ID
    return MSG_ID


@dp.message_handler(CommandStart(), state=None)
async def cmd_start(message: types.Message):
    # Command '/start' handler
    # Connecting database, adding telegram id to db
    global MSG_ID
    await DB.create_table()
    if not await DB.user_existing(message.from_user.id):
        await DB.add_user(message.from_user.id)
    branches_markup = await branches_keyboard(message.from_user.id)
    bot_message = await bot.send_message(text=f'Для выполнения вашего заказа\n'
                                              f'выберите филиал из списка ниже:\n',
                                         chat_id=message.from_user.id,
                                         reply_markup=branches_markup)
    MSG_ID = bot_message.message_id
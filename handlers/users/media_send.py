from aiogram import types
from loader import dp, bot


@dp.message_handler(lambda message: message.text and 'Отправить ✉' in message.text)
async def media_send_handler(message: types.Message):
    await bot.delete_message(
        chat_id=message.from_user.id,
        message_id=message.message_id
    )
    ###
    await bot.send_message(
        text='Файлы отправляются в филиал',
        chat_id=message.from_user.id,
        reply_markup=types.ReplyKeyboardRemove()
    )
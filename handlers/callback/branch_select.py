from loader import dp, bot
from aiogram import types
from keyboards.default import main_keyboard
from handlers.users import start
from aiogram.utils.exceptions import MessageNotModified


@dp.callback_query_handler(text_contains='branch_')
async def branch_call(call: types.CallbackQuery):
    MSG_ID = start.get_message_id()
    await start.DB.update_user_branch(telegram_id=call.from_user.id, branch=call.data)
    try:
        text = f"Загрузите файл.\n" \
               f"После загрузки файла, нажмите снизу <i>Отправить</i>\n" \
               f"<b>Максимальный размер файлов 20МБ</b>"
        await bot.delete_message(
            chat_id=call.message.chat.id,
            message_id=MSG_ID
        )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=text,
            reply_markup=main_keyboard
        )

    except MessageNotModified:
        pass
    await bot.answer_callback_query(callback_query_id=call.id)
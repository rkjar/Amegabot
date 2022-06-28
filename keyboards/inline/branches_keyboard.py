from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.users import start

buttons = [
    InlineKeyboardButton(text="Гостиный двор", callback_data="branch_gd"),
    InlineKeyboardButton(text="ТЦ Башкирия", callback_data="branch_bash"),
    InlineKeyboardButton(text="Менделеева", callback_data="branch_men"),
    InlineKeyboardButton(text="ТЦ Олимп", callback_data="branch_olimp"),
    InlineKeyboardButton(text="ТЦ Шатлык", callback_data="branch_shat"),
    InlineKeyboardButton(text="Космонавтов", callback_data="branch_kosmo"),
    InlineKeyboardButton(text="8 марта", callback_data="branch_8marta")
]


async def branches_keyboard(telegram_id: int) -> InlineKeyboardMarkup:
    current_branch = await start.DB.get_user_branch(telegram_id)
    if current_branch:
        for button in buttons:
            if button.text[-1] == "✅" and button.callback_data != current_branch[0][0]:
                button.text = f"{button.text[:-2]}"
            elif button.text[-1] != "✅" and button.callback_data == current_branch[0][0]:
                button.text = f"{button.text} ✅"
            elif button.text[-1] == "✅" and button.callback_data == current_branch[0][0]:
                pass
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

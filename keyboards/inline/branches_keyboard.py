from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons = [
    InlineKeyboardButton(text="Гостиный двор", callback_data="gd"),
    InlineKeyboardButton(text="ТЦ Башкирия", callback_data="bash"),
    InlineKeyboardButton(text="Менделеева", callback_data="men"),
    InlineKeyboardButton(text="ТЦ Олимп", callback_data="olimp"),
    InlineKeyboardButton(text="ТЦ Шатлык", callback_data="shat"),
    InlineKeyboardButton(text="Космонавтов", callback_data="kosmo"),
    InlineKeyboardButton(text="8 марта", callback_data="8marta")
]

branches_keyboard = InlineKeyboardMarkup(row_width=2)
branches_keyboard.add(*buttons)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    KeyboardButton(text='Отправить ✉️')
]

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(*buttons)
import logging
from aiogram import Bot, Dispatcher, types
from data import config
from db import User


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)

from aiogram import types

from app import dp
from loader import bot


@dp.callback_query_handler(text=['bot1'])
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '@PatheticScum_interpret_bot')


@dp.callback_query_handler(text=['bot2'])
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '@PatheticScum_weather_bot')\



@ dp.callback_query_handler(text=['bot3'])
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '@PatheticScum_inherit_bot')

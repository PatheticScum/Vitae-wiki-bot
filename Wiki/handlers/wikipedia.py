from aiogram import types

from app import dp
import wikipedia


@dp.message_handler(commands='wiki')
async def bot_help(message: types.Message):
    await message.answer('Welcome to the bot, type everything that you want to find')


@dp.message_handler(content_types='text')
async def bot_help(message: types.Message):
    result = message.text
    content = wikipedia.search(result)
    await message.answer(content)

from aiogram import types


from app import dp
from loader import db


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    await message.answer("Welcome to the bot. Start searching things from Wikipedia using this bot. ")
    db.create_user_id(chat_id)


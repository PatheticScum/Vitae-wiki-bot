from aiogram import types

from keyboards.inline.bots import bots
from loader import dp


@dp.message_handler(commands='self')
async def command_self(message: types.Message):

    await message.answer("My nickname is Vitae | 硕士 .\n"
                         "As for bot, I created this bot "
                         "absolutely for everyone and you "
                         "can use this bot as much as you "
                         "want 🤙\n"
                         "Hope you will enjoy 😉\n\n"
                         "For contact, use this https://t.me/PatheticScum\n\n",
                         reply_markup=bots)

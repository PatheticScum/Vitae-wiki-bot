from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


from loader import dp


@dp.message_handler(CommandHelp())
async def command_help(message: types.Message):
    text = (f" Well, there are some commands that you can use in this bot:\n\n"
            f"Send the command /start to start the bot .\n\n"
            f"Send the command /help for support .\n\n"
            f"Send the command /self to get to know about me.\n\n"
            f"Send the command /wiki to get to know about Privacy Policy Terms.\n\n")

    await message.answer(text)


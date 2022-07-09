from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "launch the bot"),
            types.BotCommand("help", "settings of bot"),
            types.BotCommand("self", "info about admin"),
            types.BotCommand("clear", "clearing chat history"),
            types.BotCommand("wiki", "wikipedia"),

        ]
    )

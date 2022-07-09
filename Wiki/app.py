import logging

from aiogram import executor

from loader import dp, db

from utils.default_commands import set_default_commands

import handlers


logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):

    db.create_table_users()

    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

from aiogram import types


from app import dp

from loader import bot


@dp.message_handler(commands='clear')
async def accept(message: types.Message):

    try:
        numbers = range(500)
        for num in numbers:
            num += 1
            chat_id = message.from_user.id
            message_id = message.message_id - num

            await bot.delete_message(chat_id, message_id)

    except Exception as error:
        return error

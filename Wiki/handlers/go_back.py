from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


from loader import dp, bot


@dp.message_handler(Text(equals=['Back']))
async def back(msg: types.Message, state: FSMContext):
    chat_id = msg.from_user.id
    message_id = msg.message_id - 1
    await state.finish()
    await bot.delete_message(chat_id, message_id)
    await msg.answer("Send the link in order to download the video 🔗:")
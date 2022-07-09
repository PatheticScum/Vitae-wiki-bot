from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# def main_menu(category_list):
#     bots = InlineKeyboardMarkup(row_width=1)
#     bots.insert(InlineKeyboardButton(text='Translator bot', url='er')
#                 return bots


# bots = InlineKeyboardMarkup(
#     inline_keyboard=[
#         InlineKeyboardButton('Translator Bot', callback_data='1', url='@PatheticScum_interpret_bot'),
#
#         InlineKeyboardButton('Weather Bot', callback_data='2', url='@PatheticScum_weather_bot')
#     ]
# )


bot1 = InlineKeyboardButton('Translator Bot', callback_data='bot1')
bot2 = InlineKeyboardButton('Weather Bot', callback_data='bot2')
bot3 = InlineKeyboardButton('Inherit Bot', callback_data='bot3')


bots = InlineKeyboardMarkup().add(bot1, bot2, bot3)

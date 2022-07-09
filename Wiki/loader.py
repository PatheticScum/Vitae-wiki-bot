from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sql.db_sql import Database
from ADMIN.conf import configuration

bot = Bot(token=configuration.BOT_TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database('ADMIN/users.db')

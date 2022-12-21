import telegram as tg
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import database as db

db.create_tables()

bot = aiogram.Bot(token="")
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

tg.registration(dp=dp)
tg.menu(dp=dp)
tg.look_lesson(dp=dp)
tg.enter2lesson(dp=dp)

aiogram.executor.start_polling(dp, skip_updates=True)
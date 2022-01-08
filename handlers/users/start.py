from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import CHANEL
from loader import dp, bot
from utils.db_api.mongo import users_db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    req_db = users_db.update_one({'user_id': message.from_user.id}, {'$set': {
        "user_id": message.from_user.id,
        "updated": datetime.now(), }
    }, upsert=True)

    if (req_db.matched_count):
        textback = "Assalomu Alaykum, <b>{}</b>!".format(message.from_user.full_name)
    else:
        textback = "Yana sizni ko'rganimdan xursandman, <b>{}</b>".format(message.from_user.first_name)
    count_user = users_db.count()
    await bot.send_message(CHANEL, text="@image2cartoon_bot botni statistikasi: {}".format(str(count_user)))
    await message.answer(textback)

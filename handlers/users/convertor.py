from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import CHANEL
from loader import dp, bot
from utils import photo_link, cartoon


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Iltimos o'z rasmingizni yuboring.")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def converter(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    await bot.send_message(CHANEL, link)
    await msg.answer("Iltimos biroz kuting sizning rasmingiz <b>Sun'iy intellekt</b> tomonidan qayta ishlanmoqda")
    try:
        new_photo = await cartoon(link)
        await msg.reply_photo(photo=new_photo['output_url'], caption='@image2cartoon_bot')
        await bot.send_photo(CHANEL, photo=new_photo['output_url'], caption='@image2cartoon_bot {}'.format(msg.from_user.mention))
    except Exception as ex:
        await bot.send_message(CHANEL, text=str(ex))
        await msg.answer("Rasmdan yuzni aniqlay olmadik, iltimos o'z rasmingizni yuboring.")
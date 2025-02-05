from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp  # loader.py dan `dp` obyektini import qilish

SUPERUSERS = [7150214500]  # ID ni ro‘yxat sifatida saqlash

# agar super user secret deb yozadigan bo'lsa shunday bo'ladi bo'lmasa yo'q 
@dp.message_handler(Text(equals="secret"), user_id=SUPERUSERS)
async def id_filter_example(msg: types.Message):
    await msg.answer("Xush kelibsiz, super user!")

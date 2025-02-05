from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


# bu ishlidi buning uchun manabu linkni qo'ysa 
# bu asosan reklama bergandan keladigan avditoriyani aniqlab beradi 
# https://t.me/ecocalculator_bot?start=kunuz
@dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f"salom {message.from_user.full_name}!\n"
    text += f"sizni {args} tafsiya qildi"
    await message.answer(text)


# bu startni bosganda bo'ladigan xolat commands o'rniga boshqa narsa ham yozsa bo'ladi 
# @dp.message_handler(commands='start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")

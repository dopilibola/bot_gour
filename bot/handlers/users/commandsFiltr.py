from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp




# bu luboy funksiyaga javob beradigan qilsa bo'ladi 
# @dp.message_handler(commands='til')
@dp.message_handler(Command('til'))
async def bot_Langue(nsg: types.Message):
    await nsg.answer(f"Til o'zgardi ")
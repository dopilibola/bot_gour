from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp

@dp.message_handler(commands=['til'])
# @dp.message_handler(Command('til'))
async def bot_Langue(message: types.Message):
    await message.answer(f"til ozgardi!")

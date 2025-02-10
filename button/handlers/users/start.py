# import logging
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
# from keyboards.default.start import menuStart
# from keyboards.default.starcom import menuStartm
# from loader import dp


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     # logging.info(message)
#     # logging.info(f"{message.from_user.username=}")
#     # logging.info(f"{message.from_user.full_name=}")
#     # users = {message.from_user.id:message.from_user.username}
#     await message.answer(f"Salom, {message.from_user.full_name} ", reply_markup=menuStartm)
 

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!\n")
#     await message.answer(f"telefon va loc tasheng, ", reply_markup=menuStart)
#     logging.info(message)
 
import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.starcom import menuStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}, do'konimizga xush kelibsiz!",reply_markup=menuStart)

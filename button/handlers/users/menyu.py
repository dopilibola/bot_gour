from keyboards.default.menu import menu
from keyboards.default.python import menuPython
from aiogram.dispatcher.filters import Command, Text
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(f"kurni tanla ", reply_markup=menu)

@dp.message_handler(text='Telegram bot')
async def show_bot(message: Message):
    await message.answer(f"bot kursini olmoqchimisiz  ", reply_markup=menu)



@dp.message_handler(text='Python')
async def show_python(message: Message):
    await message.answer(f"Mavzuni tanla  ", reply_markup=menuPython)


@dp.message_handler(text='Boshiga')
async def show_python(message: Message):
    await message.answer(f"kurni tanla ", reply_markup=menu)

# bu ochirib yuboradi tugmalarni 
@dp.message_handler(text='orqaga')
async def show_python(message: Message):
    await message.answer(f"124 ", reply_markup=ReplyKeyboardRemove())
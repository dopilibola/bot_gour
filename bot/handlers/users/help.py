from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandSettings

from loader import dp

# helpni bossa shu funkisya ishga tushadi 
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))


# settings bosganda shu funksiya ishga tushadi 
@dp.message_handler(CommandSettings())
async def bot_settings(message: types.Message):
    text = ("sozlamalar")
    
    await message.answer(text)

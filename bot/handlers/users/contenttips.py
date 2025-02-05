from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp




# bu rasmni filtirlaydi agar siga rasm jonatsa uni farqlaydi 
# PHOTO orniga boshqa narsa ham qo'ysa bo'ladi 

# @dp.message_handler(content_types='photo') 
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def bot_Langue(nsg: types.Message):
    await nsg.answer(f"Bu nima rasm ?")


from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


# bu cha tadmin qila oladigan narsalar boshqa odam qila olmidi 
# @dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def bot_Langue(message: types.Message):
    await message.answer(f"rasm o'zgartiremi !")
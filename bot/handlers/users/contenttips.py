from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp






@dp.message_handler(content_types=types.ContentType.PHOTO)
async def bot_Langue(nsg: types.Message):
    await nsg.answer(f"Bu nima rasm ?")

# @dp.message_handler(content_types='photo')
# async def photo_hendler(nsg: types.Message):
#     await nsg.answer('Nima bu rasm')
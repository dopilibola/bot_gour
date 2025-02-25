import io

from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import IsGroup
from filters.admin import AdminFilter
from loader import dp, bot

# pghotoni glavnisini ozgartiradi faqat admin qila oladi 
@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    await message.chat.set_photo(photo=input_file)

# bu gurpani nomini o'zgartiradigan code  
@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_now_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await bot.set_chat_title(message.chat.id, title=title)




# bu camanda description yuboruvchi kamanda hisoblanadi. 
@dp.message_handler(IsGroup(), Command("set_discription", prefixes="!/"), AdminFilter())
async def set_now_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # await bot.set_chat_description(message.chat.id, description=description)
    await message.chat.set_description(description=description)
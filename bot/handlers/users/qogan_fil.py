from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

# bu repley qilganini javobini qaytaradigan hendler 
@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter_example(msg: types.Message):
    await msg.answer(msg.reply_to_message.from_user.id)


# bu o'zini cantaktini yuborsa ishlatadigan hendler 
@dp.message_handler(content_types='contact', is_sender_contact=True)
# @dp.message_handler(filters.IsSenderContact(True), content_types='contact')
async def sender_contact_ex(msg: types.Message):
    await msg.answer('Rahmat kontactiz qabul qilindi')

# bu brov yozgan narsani yuboradigan hendler 
@dp.message_handler(is_forwarded=True)
async def forwarded_ex(msg: types.Message):
    await msg.answer('Brovni xabarini menga yubordizmi ')

# bu chatga olib boradigan filter
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def chat_type_examp(msg: types.Message):
    await msg.answer('bu shaxsiy chat')
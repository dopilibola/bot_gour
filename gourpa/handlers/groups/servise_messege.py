from aiogram import types
from filters import IsGroup
from loader import dp, bot

# gurpaga qoshilsa shu sms keladi 
@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Xush kelibsiz {members}. ")

# guruxdan chiqib ketsa yoki chiqarib yuborsa shu sms keladi 
@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruxni tark etdi")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} guruxdan xaydaldi"
                             f"admin: {message.from_user.get_mention(as_html=True)}.")
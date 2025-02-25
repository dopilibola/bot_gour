import asyncio
import datetime
import re

import aiogram 
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot



# userlar faqat reding qila odladigan rejim 
@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2) #soat yoki daqiqasi
    comment = parsed.group(3) #nima sababi 
    if not time: 
        time = 5
        time = int(time)

        # ban vaqtini hozirgi vaqt bilan hisoblash 
        until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)


        try: 
            await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
            await message.reply_to_message.delete()
        except aiogram.utils.exceptions.BadRequest as err:
            await message.answer(f"Xatolik! {err.args}")
            return
       
        # chat yozish 
        await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozolmidi \n "
                             f"sabab: \n<b>{comment}</b>")
        
        service_message = await message.reply("xabar 5 sekunddan keyin ochib ketadi")
        # ochirib tashlash 
        await asyncio.sleep(5)
        await message.delete()
        await service_message.delete()



# read-only holatdan qayta tiklash 
@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    service_message = await message.reply("xabar 5 sec song ochib ketadi")
    
    await asyncio.sleep(5)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi {member.full_name} tiklandi ")

    # xabarlar ochiramiz 
    await message.delete()
    await service_message.delete()




# ban qiladi 
# @dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
# async def ban_user(message: types.Message):
#     member = message.reply_to_message.from_user
#     member_id = member.id
#     chat_id = message.chat.id
#     await message.chat.kick(user_id=member_id)

#     await message.answer(f"foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
#     service_message = await message.reply("xabar 5sec keyin ochib ketadi ")

#     await asyncio.sleep(5)
#     await message.delete()
#     await service_message.delete()

@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    if message.reply_to_message is None:
        await message.reply("Iltimos, kimnidir bloklash uchun shu odamning xabariga javob qilib /ban buyrug‘ini yozing.")
        return
    
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    try:
        await message.chat.kick(user_id=member_id)
        await message.answer(f"Foydalanuvchi {member.full_name} guruhdan haydaldi.")
        
        service_message = await message.reply("Xabar 5 soniyadan keyin o‘chiriladi.")
        await asyncio.sleep(5)
        
        await message.delete()
        await service_message.delete()
    except Exception as e:
        await message.reply(f"Xatolik yuz berdi: {e}")




# bandan chiqaradi 
@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    if not message.reply_to_message:  # Agar reply-to bo‘lmasa, xatolik haqida xabar beramiz
        await message.reply("❌ Iltimos, ban ochish uchun foydalanuvchining xabariga javoban /unban ni ishlating.")
        return

    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    await message.chat.unban(user_id=member_id)
    await message.answer(f"✅ Foydalanuvchi {member.full_name} bandan chiqarildi.")

    service_message = await message.reply("🕒 Xabar 5 soniyadan keyin o‘chiriladi...")
    await asyncio.sleep(5)

    await message.delete()
    await service_message.delete()

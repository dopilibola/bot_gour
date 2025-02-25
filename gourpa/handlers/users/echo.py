from aiogram import types
from filters import IsPrivate
from loader import dp


# ISPrivate qoyganim uchun guruxda eco bot ishlamayapdi, 
# bu oldin filters filega man narsalar yozib qo'yganman shuning uchun ishlamayotgan bo'lishi mumkun 
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)

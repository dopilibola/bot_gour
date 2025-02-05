from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp

# boshi asalou degandan keyingisino o'qimiydide qolganini javobi ketadi 

@dp.message_handler(Text(contains='asalomu', ignore_case=True))
@dp.message_handler(Text(equals='asalomu', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply('valekum asalom')

# boshqa parametrlar 
# startswith  qaysidir so'z bilan boshlansa
# endswith qaysidir soz bilan tugasa 
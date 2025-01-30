from aiogram import Bot, Dispatcher, executor, types

# Bot tokenini kiriting
BOT_TOKEN = "6534647990:AAHvV4GrtXr0QS5No8RodRkgRz0on9erjDg"

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# /start va /help komandalariga javobberadi qolganlarini h
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Men Echo Botman. Nima yozsangiz, shuni qaytaraman!")

# Oddiy matnli xabarlarga javob  exo botni ishlashi 
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
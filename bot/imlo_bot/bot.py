from checkWords import checkWord12  # Funksiya nomini to'g'rilash
from aiogram import Bot, Dispatcher, executor, types

# Bot tokenini kiriting
BOT_TOKEN = "6534647990:AAHvV4GrtXr0QS5No8RodRkgRz0on9erjDg"

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# /start va /help komandalariga javob
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Men Echo Botman. Nima yozsangiz, shuni qaytaraman!")

# Oddiy matnli xabarlarga javob, Wikipedia orqali
@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord12(word)  # Funksiya nomini to'g'rilash
    if result['available']:
        response = f"! {word.capitalize()}"
    else:
        response = f"? {word.capitalize()}\n"
        for text in result['matches']:
            response += f"! {text.capitalize()}\n"
    await message.answer(response)

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
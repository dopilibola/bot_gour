import wikipedia
from aiogram import Bot, Dispatcher, executor, types

# Bot tokenini kiriting
BOT_TOKEN = "6534647990:AAHvV4GrtXr0QS5No8RodRkgRz0on9erjDg"
wikipedia.set_lang('uz')

# Bot va Dispatcher obyektlarini yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# /start va /help komandalariga javob
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Men Echo Botman. Nima yozsangiz, shuni qaytaraman!")

# Oddiy matnli xabarlarga javob, Wikipedia orqali
@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)  # Yangi kod: message.respond o'rniga respond ni yuboring
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"Ko'plab variantlar mavjud: {e.options}")
    except wikipedia.exceptions.HTTPTimeoutError:
        await message.answer("Wikipedia serveridan javob olishda xatolik yuz berdi.")
    except Exception as e:
        await message.answer("Bu mavzuga oid maqola topilmadi yoki boshqa xatolik yuz berdi.")

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

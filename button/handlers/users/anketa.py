from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states.persondata import PersanolData


@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("toliq ismini kiriting")
    await PersanolData.fullname.set()

@dp.message_handler(state=PersanolData.fullname)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    # await state.update_data(name=fullname)
    await state.update_data(
        {"name": fullname}
    )

    await message.answer("emailingizni kiriting")
    await PersanolData.next()
    # await PersanolData.email.set()


@dp.message_handler(state=PersanolData.email)
async def answer_email(message: types.Message, state: FSMContext):
    
    email = message.text
    await state.update_data(
        {"email": email}
    )

    await message.answer("telefon raqam kirit")
    await PersanolData.next()


@dp.message_handler(state=PersanolData.phoneNum)
async def answer_num(message: types.Message, state: FSMContext):
    
    phone = message.text
    await state.update_data(
        {"phone": phone}
    )

# malumotlarni qa
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = "Quyidagi ma'lumotlar qabul qilinad \n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"telefon - {phone}"
    await message.answer(msg)
    
    await state.finish()
    await state.reset_state(with_data=False)
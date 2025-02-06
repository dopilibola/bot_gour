from aiogram.dispatcher.filters.state import StatesGroup, State

class PersanolData(StatesGroup):  # PersonalData ni to'g'ri aniqlash
    fullname = State()  # To'liq ism
    email = State()  # Email
    phoneNum = State()  # Telefon raqam

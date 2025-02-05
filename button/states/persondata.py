from aiogram.dispatcher.filters.state import StatesGroup, State

class PersanolData(StatesGroup):
    fullname = State()
    email = State()
    phoneNum = State()
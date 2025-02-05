from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from loader import dp
# bu code /xarid bosgandan keyn buyog'iga javob beradigan code 
@dp.message_handler(commands='xarid')
async def set_state(msg: types.Message, state: FSMContext):
    await state.set_state('xarid_state') #xarit_state bu dp jonatadi tipa filter
    await msg.answer('mahsulot tanlang')

@dp.message_handler(state='xarid_state') #bu osha filterni qabul qilib bir marttalik javob beradi 
async def state_exemple(msg: types.Message, state: FSMContext):
    await msg.answer("maxsulot savatga qo'shildi ") 
    await state.finish() #oxirda erore chiqadi sabbabi bu userni datasini yana kimgadir jo'natishi kere bo'lmasa xato chiqarib bervuradi 

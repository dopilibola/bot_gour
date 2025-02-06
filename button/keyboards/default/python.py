from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[  
        [
            KeyboardButton(text='hello word'),
            KeyboardButton(text='kerakli dasturlar '),
        ],
        [
            KeyboardButton(text='orqaga'),
            KeyboardButton(text='Boshiga'),

        ],
    ],
    resize_keyboard=True
)

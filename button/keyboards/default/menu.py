from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



"""
    bu shunday fuksiyaki knopka bo'ladi u knopkani bosganda o'sha matin ko'rinishida kelib tushadi,
    shuning uchun
            KeyboardButton(text='Python'), 
    qilingan
"""
menu = ReplyKeyboardMarkup(
    keyboard=[  # `keybord` emas, `keyboard`
        [
            KeyboardButton(text='Python'),
            KeyboardButton(text='Telegram bot'),
        ],
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[  
        [
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='location', request_location=True),
        ],
    ],
    resize_keyboard=True
)

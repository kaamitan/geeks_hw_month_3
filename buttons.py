# buttosns.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a = True

cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a)

cancel_button = KeyboardButton("Cancel")
cancel.add(cancel_button)


cancel2 = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Отмена"))

submit = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Да"), KeyboardButton("Нет")
)

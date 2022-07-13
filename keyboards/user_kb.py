from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('/Кнопка 1')
b2 = KeyboardButton('/Кнопка 2')
b3 = KeyboardButton('/Кнопка 3')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True)
user_kb.add(b1).add(b2).add(b3)

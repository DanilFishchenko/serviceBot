from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Искать_запчасти')
b2 = KeyboardButton('/Искать_ремонты')
b3 = KeyboardButton('/Другое')
b4 = b3 = KeyboardButton('/Мой_телефон')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

user_kb.add(b1).insert(b2).add(b3)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Запчасти')
b2 = KeyboardButton('/Ремонты')
#b3 = KeyboardButton('/Другое')
# b4 = KeyboardButton('/Телефон', request_contact=True)
# b5 = KeyboardButton('/Локация', request_location=True)

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

user_kb.add(b1).insert(b2)#.add(b3).row(b4, b5)

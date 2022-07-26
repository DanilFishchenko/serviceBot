from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

b1 = KeyboardButton("\U00002699 Поиск запчастей")
b2 = KeyboardButton("\U0001F6E0 Статус ремонта")
# b3 = KeyboardButton('Другое')
b4 = KeyboardButton('\U00000260 Телефон', request_contact=True)  # для авторизации
b5 = KeyboardButton('\U0001F6AB Отмена')
# b6 = InlineKeyboardButton('Фото', url='')

auth_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# in_kb = InlineKeyboardMarkup(row_width=2)

auth_kb.add(b4)
user_kb.add(b1).insert(b2)
kb_cancel.add(b5)
# inl_kb.add(b6)

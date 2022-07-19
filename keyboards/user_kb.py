from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

b1 = KeyboardButton("\U00002699 Запчасти")
b2 = KeyboardButton("\U0001F6E0 Ремонты")
#b3 = KeyboardButton('/Другое')
# b4 = KeyboardButton('/Телефон', request_contact=True)
b5 = KeyboardButton('\U0001F6AB Отмена')
b6 = InlineKeyboardButton(text='Смотреть фото', url=f"https://danil-fishchenko.myjino.ru/photo/зч.21284.jpg")

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
inl_kb = InlineKeyboardMarkup(row_width=1)

user_kb.add(b1).insert(b2)
kb_cancel.add(b5)
inl_kb.add(b6)


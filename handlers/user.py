from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import user_kb
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def command_start(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Привет!', reply_markup=user_kb)
    await message.answer(f'Привет, {message.from_user.full_name}!')
    await bot.send_message(message.from_user.id, 'тут будет поиск запчастей', reply_markup=user_kb)
    await message.delete()


# @dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def command_help(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}! Это бот для проверки наличия запчастей')
    await message.delete()


# @dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def echo(message: types.Message):
    await message.answer(message.text)


async def search_parts(message: types.Message):
    await bot.send_message(message.from_user.id, 'тут будет поиск запчастей')
    await message.delete()


async def search_repairs(message: types.Message):
    await message.answer('тут будет поиск ремонтов')
    await message.delete()


async def search_other(message: types.Message):
    await bot.send_message(message.from_user.id, 'другое', reply_markup=ReplyKeyboardRemove())


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(search_parts, commands=['Искать_запчасти'])
    dp.register_message_handler(search_repairs, commands=['Искать_ремонты'])
    dp.register_message_handler(search_other, commands=['Другое'])
    dp.register_message_handler(echo)

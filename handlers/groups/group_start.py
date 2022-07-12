from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter

from bot import dp


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.GROUP))
async def bot_start(message: types.Message):
    await message.answer(f'Приветствую в нашей группе, {message.from_user.full_name}!')
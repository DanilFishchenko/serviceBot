from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter, CommandHelp

from bot import dp


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

    @dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
    async def send_help(message: types.Message):
        await message.answer("Чем я могу помочь?")
from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter

from bot import dp

@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def echo(message: types.Message):
    await message.answer(message.text)
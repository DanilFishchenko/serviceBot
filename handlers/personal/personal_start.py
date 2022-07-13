from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter, CommandHelp
from keyboards import user_kb
from bot import dp


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def bot_start(message: types.Message):
   try:
    await dp.bot.send_message(message.from_user.id, 'Привет!', reply_markup=user_kb)
   #await message.answer(f'Привет, {message.from_user.full_name}!')
    await message.delete()
   except:
       await message.answer('Что то не так')

    @dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
    async def send_help(message: types.Message):
        await message.answer("Чем я могу помочь?")
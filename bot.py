from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/info", description="Информация")
        ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Чем я могу помочь?")












if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
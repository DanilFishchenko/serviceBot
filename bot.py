from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def set_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand(command="/start", description="Начать"),
        types.BotCommand(command="/help", description="Помощь"),
        types.BotCommand(command="/info", description="Информация")
    ])





if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)

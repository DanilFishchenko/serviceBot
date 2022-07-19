from aiogram.utils import executor
from aiogram import types
from handlers import user
from create_bot import dp

async def set_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand(command="/start", description="Начать"),
        types.BotCommand(command="/help", description="Помощь"),
        types.BotCommand(command="/info", description="Информация"),
        types.BotCommand(command="/Запчасти", description="Поиск запчастей"),
        types.BotCommand(command="/Ремонты", description="Поиск ремонтов")
    ])

async def on_startup(_):
    print('BOT online')

user.register_handlers_user(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

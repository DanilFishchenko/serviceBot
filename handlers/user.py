from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import user_kb, kb_cancel, inl_kb
from aiogram.types import ReplyKeyboardRemove
from queries.user_queries import sp_query
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text


class FSMUser(StatesGroup):
    parts = State()
    repairs = State()


# @dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def command_start(message: types.Message):
    # await bot.send_message(message.from_user.id, 'Привет!', reply_markup=user_kb)
    await bot.send_message(message.from_user.id, f'Привет, {message.from_user.full_name}!', reply_markup=user_kb)
    await message.delete()


# @dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def command_help(message: types.Message):
    await message.answer(f'Добрый день, {message.from_user.full_name}! Это бот для проверки наличия запчастей')
    await message.delete()


async def parts_mode(message: types.Message):
    await FSMUser.parts.set()
    await message.answer('Введите модель BORK', reply_markup=kb_cancel)
    await message.delete()


async def repairs_mode(message: types.Message):
    await message.answer('Введите номер карты брака или сервисное обращение (тут будет поиск ремонтов)', reply_markup=kb_cancel)
    await message.delete()


async def search_parts(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text
    sp_found = sp_query(message.text)
    if not sp_found:
        await message.answer('Ничего не найдено. Введите модель ("Отмена" для возврата)', reply_markup=kb_cancel)
    else:
        for row in sp_found:
            sp_info = f'{row[2]} для {row[3]} {row[5]}\n<i>{row[0]}</i> <b>{row[1]}</b>\nЦена: <b>{row[7]}</b> р.\nОстаток СЦ: <i>{row[4]}</i>\n<a href="https://danil-fishchenko.myjino.ru/photo/{row[0]}.html">Фото</a>'
            # sp_info_formatted = f'{fmt.hide_link(f"http://bork.ru")}{row[2]} для {row[3]} {row[5]}\n<i>{row[0]}</i> <b>{row[1]}</b>\nЦена: <b>{row[7]}</b> р.\nОстаток СЦ: <i>{row[4]}</i>'
            print(sp_info)
            code = row[0]
            await bot.send_message(message.from_user.id, sp_info, parse_mode=types.ParseMode.HTML)
        await message.answer('Новый поиск ("Отмена" для возврата)', reply_markup=kb_cancel)


async def search_repairs(message: types.Message):
    await bot.send_message(message.from_user.id, f'Информация по ремонту {message.text}:')


async def search_other(message: types.Message):
    await bot.send_message(message.from_user.id, 'другое', reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def search_cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, 'Выберите режим', reply_markup=user_kb)


# @dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(search_cancel, commands=['Отмена'], state='*')
    dp.register_message_handler(search_cancel, Text(contains='отмена', ignore_case=True), state='*')
    dp.register_message_handler(parts_mode, Text(contains='Запчасти', ignore_case=True), state=None)
    dp.register_message_handler(search_parts, state=FSMUser.parts)
    dp.register_message_handler(repairs_mode, Text(contains='Ремонты', ignore_case=True), state=None)
    dp.register_message_handler(search_repairs, state=FSMUser.repairs)
    dp.register_message_handler(search_other, commands=['Другое'])
    dp.register_message_handler(echo)

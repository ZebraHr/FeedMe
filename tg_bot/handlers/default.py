from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from aiogram.filters import Command

from tg_bot.config import logger
from tg_bot.loader import dp, bot
# from tg_bot.db.db_commands import add_user
from tg_bot.keyboards import inline as inline_kb
# from ..keyboards.callback_data import ReferralUrlCallback
# from ..states.all_states import StateUser

default_router = Router()

# default_router.message.middleware(ClientMiddleware())
# default_router.callback_query.middleware(ClientMiddleware())


# @referral_router.callback_query(ReferralUrlCallback.filter())
# @referral_router.callback_query(StateUser.referral_url, F.data == 'back_step')
@default_router.callback_query(F.data == 'back_main_menu')
async def back_main_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await main_menu(call.from_user, state)


async def main_menu(user: types.User, state: FSMContext):
    """Главное меню"""
    await state.clear()  # сброса состояния (state) для пользователя
    await bot.send_message(chat_id=user.id, text='Главное меню.', reply_markup=inline_kb.main_menu())


@default_router.message(Command('start'))
async def command_start(message: types.Message, state: FSMContext):
    logger.info(f'Пользователь {message.from_user.full_name} ввел(a) команду /start')
    await message.answer(text='Добро пожаловать.')
    await main_menu(message.from_user, state)


@default_router.message(Command('help'))
async def command_help(message: types.Message):
    await message.answer('Для запуска или перезапуска бота напишите /start')


# изменение состояния
# await state.set_state(StateUser.tariff_info)

# сохранение данных в состояние (в функции прописываем  state: FSMContext)
# await state.update_data(booking_date=date.strftime(str_format_date))

# получение данных в состояния (в функции прописываем  state: FSMContext)
# state_data = await state.get_data()
# date_string = state_data.get('booking_date')

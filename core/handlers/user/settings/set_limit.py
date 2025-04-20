from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from core.states.user_states import SetLimit
from core.keyboards.start_kb import start_kb
from core.keyboards.confirm_kb import confirm_kb

router = Router()

@router.message(F.text == '⚖️ Установить лимит')
async def change_limit(message: Message, state: FSMContext):
    await message.answer('⚖️ *Установим лимит трат.* Введите желаемую сумму:', reply_markup=ReplyKeyboardRemove(), parse_mode='Markdown')
    await state.set_state(SetLimit.SET_LIMIT)

@router.message(SetLimit.SET_LIMIT)
async def set_limit(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)

    data = await state.get_data()

    await message.answer(f'Вы уверены, что хотите установить лимит в *{data["amount"]}*❓', reply_markup=confirm_kb, parse_mode='Markdown')
    await state.set_state(SetLimit.CONFIRM_LIMIT)

@router.message(SetLimit.CONFIRM_LIMIT, F.text == '✅ Да, уверен')
async def confirm_limit_yes(message: Message, state: FSMContext):
    await message.answer('🚀 Лимит успешно установлен!', reply_markup=start_kb)
    await state.clear()
    #TODO Сделать добавление лимита в БД и проверку


@router.message(SetLimit.CONFIRM_LIMIT, F.text == '❌ Нет, назад')
async def confirm_limit_no(message: Message, state: FSMContext):
    await message.answer('↩️ Возвращаемся в главное меню',reply_markup=start_kb)





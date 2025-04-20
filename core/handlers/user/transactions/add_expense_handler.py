from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from core.keyboards.expense_kb import expense_kb
from core.keyboards.start_kb import start_kb
from core.states.user_states import AddExpense

router = Router()

#TODO Сделать валидацию данных
#TODO Сделать проверку на лимит трат

@router.message(F.text == '➖ Добавить расход')
async def add_expense_name(message: Message, state: FSMContext):
    await message.answer('🛒 Введите название товара или услуги:', reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddExpense.ENTER_NAME)


@router.message(AddExpense.ENTER_NAME)
async def add_expense_amount(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('➖ Теперь укажите количество:')
    await state.set_state(AddExpense.ENTER_AMOUNT)


@router.message(AddExpense.ENTER_AMOUNT)
async def add_expense_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await message.answer('💵 Сколько вы потратили?')
    await state.set_state(AddExpense.ENTER_PRICE)


@router.message(AddExpense.ENTER_PRICE)
async def add_expense_category(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('📂 *Выберите категорию расхода:*', reply_markup=expense_kb, parse_mode='Markdown')
    await state.set_state(AddExpense.ENTER_CATEGORY)


@router.message(AddExpense.ENTER_CATEGORY)
async def save_expense_data(message: Message, state: FSMContext):
    await state.update_data(category=message.text)

    #TODO Сделать сохранение data в БД
    data = await state.get_data()
    await message.answer('✅ Расход успешно сохранён!', reply_markup=start_kb)
    await state.clear()




from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.expense_kb import expense_kb
from keyboards.start_kb import start_kb
from states.user_states import AddExpense

router = Router()

#TODO Сделать валидацию данных
#TODO Сделать проверку на лимит трат

@router.message(F.text.lower() == 'добавить расход')
async def add_expense_name(message: Message, state: FSMContext):
    await message.answer('Введите название товара', reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddExpense.ENTER_NAME)


@router.message(AddExpense.ENTER_NAME)
async def add_expense_amount(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Отлично. Теперь введи количество')
    await state.set_state(AddExpense.ENTER_AMOUNT)


@router.message(AddExpense.ENTER_AMOUNT)
async def add_expense_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await message.answer('Супер. Теперь введи сколько ты потратил')
    await state.set_state(AddExpense.ENTER_PRICE)


@router.message(AddExpense.ENTER_PRICE)
async def add_expense_category(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('А теперь выбери категорию:', reply_markup=expense_kb)
    await state.set_state(AddExpense.ENTER_CATEGORY)


@router.message(AddExpense.ENTER_CATEGORY)
async def save_expense_data(message: Message, state: FSMContext):
    await state.update_data(category=message.text)

    #TODO Сделать сохранение data в БД
    data = await state.get_data()
    await message.answer('Записал твои новые траты', reply_markup=start_kb)
    await state.clear()




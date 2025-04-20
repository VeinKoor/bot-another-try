from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.start_kb import start_kb
from keyboards.income_kb import income_kb
from states.user_states import AddIncome

router = Router()

#TODO Сделать валидацию данных

@router.message(F.text.lower() == 'добавить доход')
async def add_income_price(message: Message, state: FSMContext):
    await message.answer('Введите сумму:', reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddIncome.ENTER_INCOME)

@router.message(AddIncome.ENTER_INCOME)
async def add_income_category(message: Message, state: FSMContext):
    await state.update_data(income=message.text)
    await message.answer('Выберите категорию:', reply_markup=income_kb)
    await state.set_state(AddIncome.ENTER_CATEGORY)

@router.message(AddIncome.ENTER_CATEGORY)
async def save_income_data(message: Message, state: FSMContext):
    await state.update_data(category=message.text)

    #TODO Сделать сохранение в бд
    data = await state.get_data()
    await message.answer('Записал твои новые доходы', reply_markup=start_kb)
    await state.clear()





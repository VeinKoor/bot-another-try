from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from states.user_states import ChangeName
from keyboards.start_kb import start_kb

router = Router()

@router.message(F.text.lower() == 'изменить имя')
async def change_name(message: Message, state: FSMContext):
    await message.answer('Введите ваше имя', reply_markup=ReplyKeyboardRemove())
    await state.set_state(ChangeName.SET_NAME)

@router.message(ChangeName.SET_NAME)
async def set_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    #TODO Сделать сохранение data в БД
    data = await state.get_data()
    await message.answer('Имя успешно изменено', reply_markup=start_kb)
    await state.clear()





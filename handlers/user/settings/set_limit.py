from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from states.user_states import SetLimit, ChangeName
from keyboards.start_kb import start_kb
from keyboards.confirm_kb import confirm_kb

router = Router()

@router.message(F.text.lower() == 'установить лимит трат')
async def change_limit(message: Message, state: FSMContext):
    await message.answer('Введите максимальную сумму', reply_markup=ReplyKeyboardRemove())
    await state.set_state(SetLimit.SET_LIMIT)

@router.message(SetLimit.SET_LIMIT)
async def set_limit(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)

    data = await state.get_data()

    await message.answer(f'Вы уверены, что хотите установить лимит в {data['amount']}?', reply_markup=confirm_kb)
    await state.set_state(SetLimit.CONFIRM_LIMIT)

@router.message(SetLimit.CONFIRM_LIMIT, F.text.lower() == 'да')
async def confirm_limit_yes(message: Message, state: FSMContext):
    await message.answer('Вы успешно установили лимит', reply_markup=start_kb)
    await state.clear()
    #TODO Сделать добавление лимита в БД и проверку


@router.message(SetLimit.CONFIRM_LIMIT, F.text.lower() == 'нет')
async def confirm_limit_no(message: Message, state: FSMContext):
    await message.answer('Возврат в меню', reply_markup=start_kb)





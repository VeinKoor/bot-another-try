from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.settings_kb import settings_kb

router = Router()

@router.message(F.text.lower() == 'настройки')
async def profile(message: Message, state: FSMContext):
    await message.answer('Вот что ты можешь настроить:', reply_markup=settings_kb)




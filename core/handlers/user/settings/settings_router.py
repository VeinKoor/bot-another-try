from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.keyboards.settings_kb import settings_kb

router = Router()

@router.message(F.text == '⚙️ Настройки')
async def profile(message: Message, state: FSMContext):
    await message.answer('⚙️ *Что можно настроить:*', reply_markup=settings_kb, parse_mode='Markdown')




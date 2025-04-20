from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.lower() == 'профиль')
async def profile(message: Message):
    await message.answer('Вот твой профиль')

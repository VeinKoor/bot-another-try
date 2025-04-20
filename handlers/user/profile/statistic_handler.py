from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.lower() == 'моя статистика')
async def profile(message: Message):
    await message.answer('Твоя статистика за этот месяц:')

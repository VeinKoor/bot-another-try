from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == '📊 Моя статистика')
async def profile(message: Message):
    await message.answer('📊 *Ваша статистика за этот месяц:*', parse_mode='Markdown')

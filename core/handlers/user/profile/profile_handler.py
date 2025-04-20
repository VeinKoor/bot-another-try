from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == '👤 Профиль')
async def profile(message: Message):
    await message.answer('👤 *Ваш профиль:*', parse_mode='Markdown')

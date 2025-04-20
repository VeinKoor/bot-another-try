from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from core.keyboards.start_kb import start_kb


router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer('👋 *Привет!* Я — твой личный финансовый помощник.\n'
    'Выбирай, что хочешь сделать ⬇️', reply_markup=start_kb, parse_mode='Markdown')
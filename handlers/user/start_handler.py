from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.start_kb import start_kb


router = Router()

@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer('Привет, это бот для учёта финансов\nСмотри функционал ниже⬇️', reply_markup=start_kb)
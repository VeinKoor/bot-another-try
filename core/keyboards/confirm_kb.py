from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

confirm_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='✅ Да, уверен'), KeyboardButton(text='❌ Нет, назад')]], resize_keyboard=True)
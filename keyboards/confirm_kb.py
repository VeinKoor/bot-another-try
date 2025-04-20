from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

confirm_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Да'), KeyboardButton(text='Нет')]], resize_keyboard=True)
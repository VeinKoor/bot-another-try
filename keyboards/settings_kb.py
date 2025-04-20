from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


settings_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Изменить имя'), KeyboardButton(text='Установить лимит трат')]], resize_keyboard=True)
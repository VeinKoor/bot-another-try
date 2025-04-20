from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='👤 Профиль')],
    [KeyboardButton(text='➕ Добавить доход'), KeyboardButton(text='➖ Добавить расход')],
    [KeyboardButton(text='📊 Моя статистика'), KeyboardButton(text='⚙️ Настройки')]], resize_keyboard=True
)
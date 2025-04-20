from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

#TODO Сделать возможность создавать свои категории с добавлением в БД
expense_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Еда'), KeyboardButton(text='Одежда')],
    [KeyboardButton(text='Развлечения'), KeyboardButton(text='Украшения')]], resize_keyboard=True)
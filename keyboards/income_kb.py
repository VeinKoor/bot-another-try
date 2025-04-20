from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

#TODO Сделать возможность создавать свои категории с добавлением в БД
income_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Зарплата'), KeyboardButton(text='Премия')],
    [KeyboardButton(text='Подработка'), KeyboardButton(text='Подарок')]], resize_keyboard=True)
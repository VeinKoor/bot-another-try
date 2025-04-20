from aiogram.fsm.state import StatesGroup, State


class AddIncome(StatesGroup):
    ENTER_INCOME = State()
    ENTER_CATEGORY = State()

class AddExpense(StatesGroup):
    ENTER_NAME = State()
    ENTER_AMOUNT = State()
    ENTER_PRICE = State()
    ENTER_CATEGORY = State()

class Settings(StatesGroup):
    SET_LIMIT = State()

class ChangeName(StatesGroup):
    SET_NAME = State()

class SetLimit(StatesGroup):
    SET_LIMIT = State()
    CONFIRM_LIMIT = State()
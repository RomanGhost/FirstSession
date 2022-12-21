from aiogram.dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    group = State()

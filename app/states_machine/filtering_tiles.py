from aiogram.fsm.state import StatesGroup, State


class Filter(StatesGroup):
    color = State()
    dimensions = State()

from aiogram.fsm.state import StatesGroup, State


# осуществляет сохранение фильтров поиска плитки
class Filter(StatesGroup):
    color = State()
    dimensions = State()

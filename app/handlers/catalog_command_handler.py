from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from app.data.database_example import get_all_types_of_colors, get_all_types_of_dimensions

from app.states_machine.filtering_tiles import Filter

from app.keyboards.catalog_keyboard import choosing_parameters

rt_ctlg = Router()

@rt_ctlg.message(Command("catalog"))
async def catalog(message: Message, state: FSMContext) -> None:
    await state.set_state(Filter.color)
    await message.reply(text="Выберете цвет плитки (воспользуйтесь клавиатурой):",
                        reply_markup=choosing_parameters(get_all_types_of_colors()))

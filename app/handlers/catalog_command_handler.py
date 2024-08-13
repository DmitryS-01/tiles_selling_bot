from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove

from aiogram.utils.media_group import MediaGroupBuilder

from aiogram.fsm.context import FSMContext

from app.data.database_example import get_all_types_of_colors, get_all_types_of_dimensions, get_tiles

from app.states_machine.filtering_tiles import Filter

from app.keyboards.catalog_keyboard import choosing_parameters


rt_ctlg = Router()


@rt_ctlg.message(Filter.color, Command("cancel"))
@rt_ctlg.message(Filter.dimensions, Command("cancel"))
async def cancelling(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.reply(text="Отменено! <u>/catalog</u> вернет Вас к выбору плитки :D",
                        reply_markup=ReplyKeyboardRemove())


@rt_ctlg.message(Command("catalog"))
async def picking_color(message: Message, state: FSMContext) -> None:
    await state.set_state(Filter.color)
    await message.reply(text="Выберете цвет плитки (воспользуйтесь клавиатурой)\n"
                             "<u>/cancel</u> - отмена",
                        reply_markup=choosing_parameters(get_all_types_of_colors()))


@rt_ctlg.message(Filter.color)
async def picking_dimensions(message: Message, state: FSMContext) -> None:
    if message.text in get_all_types_of_colors():
        await state.update_data(color=message.text)
        await state.set_state(Filter.dimensions)
        await message.reply(text="Отлично! Теперь выберите размеры плитки с помощью клавиатуры\n"
                                 "<u>/cancel</u> - отмена",
                            reply_markup=choosing_parameters(get_all_types_of_dimensions(color=(await state.get_data())["color"])))
    else:
        await message.reply(text="Недопустимый цвет! Пожалуйста, воспользуйтесь клавиатурой (<u>/cancel</u> - отмена)")


@rt_ctlg.message(Filter.dimensions)
async def showing_products(message: Message, state: FSMContext, bot: Bot) -> None:
    if message.text in get_all_types_of_dimensions(color=(await state.get_data())["color"]):
        await state.update_data(dimensions=message.text)
        data = await state.get_data()
        await state.clear()

        products = get_tiles(color=data["color"], dimensions=data["dimensions"])
        for tile in products:
            await bot.send_chat_action(chat_id=message.chat.id,
                                       action="typing")
            media_group = MediaGroupBuilder(caption=f"Название: <a href='{tile.link}'>{tile.name}</a>\n"
                                                    f"\n"
                                                    f"Цвет - {tile.color}\n"
                                                    f"Размеры (в мм) - {tile.dimensions}")
            for photo in tile.photos:
                media_group.add_photo(media=photo)
            await bot.send_media_group(chat_id=message.chat.id,
                                       media=media_group.build(),
                                       disable_notification=True)

        await message.reply(
            text=f"Число найденных по Вашим параметрам наименований плитки: {len(products)}.",
            reply_markup=ReplyKeyboardRemove())

    else:
        await message.reply(text="Недопустимые размеры! Пожалуйста, воспользуйтесь клавиатурой! (<u>/cancel</u> - отмена)")

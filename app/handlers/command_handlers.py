from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.keyboards.base_keyboards import admin_link, shop_example

from app.data.database_example import Tile


rt_c = Router()


@rt_c.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.reply(text=f"Привет, <b>{message.from_user.first_name}</b>!\n"
                             f"Этот бот поможет тебе выбрать лучшую плитку во всей России!")
    await message.answer(text="Список доступных команд:\n"
                              "<u>/start</u> - перезапустить бота\n"
                              "<u>/help</u> - связаться с менеджером\n"
                              "<u>/catalog</u> - просмотреть товары по фильтрам")


@rt_c.message(Command("help"))
async def command_help(message: Message) -> None:
    await message.reply(text="Если у тебя что-то не работает, попробуй перезапустить бота командой <u>/start</u>!\n"
                             "Не помогло? Есть дополнительные вопросы? Можешь написать менеджеру, он поможет тебе!",
                        reply_markup=admin_link)


@rt_c.message(Command("test"))
async def shop_test(message: Message) -> None:
    await message.reply_photo(photo="https://www.google.com/imgres?q=bbt%20%D0%BC%D0%B5%D1%80%D1%87&imgurl=https%3A"
                                    "%2F%2Fvm.vse-footbolki.ru%2Fimage%2Fvm%2Fjpg%2F280%2F0%2F3%2F3014%2F3014745"
                                    "%2Fpreviews%2Fpeople_7_manshort_front_black_280.jpg&imgrefurl=https%3A%2F%2Fvse"
                                    "-footbolki.ru%2Fsearch%2F%3Fsearch%3Dbig-baby-tape&docid=FKNB3MQJQErQPM&tbnid"
                                    "=v_USFOZO1dqfdM&vet=12ahUKEwjL2LiJmPCHAxWvGhAIHfcuAc0QM3oFCIUBEAA..i&w=280&h=280"
                                    "&hcb=2&ved=2ahUKEwjL2LiJmPCHAxWvGhAIHfcuAc0QM3oFCIUBEAA",
                              caption="<b>НАЗВАНИЕ</b>\n"
                                      "Пример описания\n"
                                      "\n"
                                      "1/52",
                              reply_markup=shop_example)
    abc = Tile(name="bbt", color="black", about="the best album ever")
    await message.answer(abc.about)

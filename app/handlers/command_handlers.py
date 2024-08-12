from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.keyboards.base_keyboards import admin_link


rt_c = Router()


@rt_c.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.reply(text=f"Привет, <b>{message.from_user.first_name}</b>!\n"
                             f"Этот бот поможет тебе выбрать лучшую плитку во всей России!")
    await message.answer(text="Список доступных команд:\n"
                              "<u>/start</u> - перезапустить бота\n"
                              "<u>/help</u> - связаться с менеджером")


@rt_c.message(Command("help"))
async def command_help(message: Message) -> None:
    await message.reply(text="Если у тебя что-то не работает, попробуй перезапустить бота командой <u>/start</u>!\n"
                             "Не помогло? Есть дополнительные вопросы? Можешь написать менеджеру, он поможет тебе!",
                        reply_markup=admin_link)

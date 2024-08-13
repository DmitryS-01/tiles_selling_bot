from aiogram import Router

from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.keyboards.basic_keyboards import admin_link

rt_c = Router()


# TODO сделать добавление пользователей в БД для реализации рассылки
@rt_c.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.reply_photo(photo="https://www.google.com/imgres?q=%D0%BF%D0%BB%D0%B8%D1%82%D0%BA%D0%B0%20%D1%84%D0"
                                    "%BE%D1%82%D0%BE&imgurl=https%3A%2F%2Fazoriceramica.ru%2Fupload%2Fiblock%2Fa34"
                                    "%2F35z2gkuo6dtxnnjew8elnpm9ihpgx143.jpg&imgrefurl=https%3A%2F%2Fazoriceramica.ru"
                                    "%2Fcollections%2Fcalacatta-ivory%2F&docid=dsRqTRvCjq6I5M&tbnid=UTbE_CEHWjTv-M"
                                    "&vet=12ahUKEwiZ9q_X3PKHAxWZGxAIHaYOAkgQM3oECGcQAA..i&w=1200&h=900&hcb=2&ved"
                                    "=2ahUKEwiZ9q_X3PKHAxWZGxAIHaYOAkgQM3oECGcQAA",
                              caption=f"Привет, <b>{message.from_user.first_name}</b>!\n"
                                      f"Этот бот поможет тебе выбрать лучшую плитку во всей России!")

    await message.answer(text="<i>Это предварительная версия бота с небольшим набором представленной плитки, "
                              "при необходимости бот будет доработан! :D</i>")

    await message.answer(text="Список доступных команд:\n"
                              "<u>/start</u> - перезапустить бота\n"
                              "<u>/help</u> - связаться с менеджером\n"
                              "<u>/catalog</u> - просмотреть товары по фильтрам")


@rt_c.message(Command("help"))
async def command_help(message: Message) -> None:
    await message.reply_photo(
        photo="https://www.google.com/imgres?q=%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80%20%D1%84%D0%BE%D1%82"
              "%D0%BE&imgurl=https%3A%2F%2Fs8.stc.all.kpcdn.net%2Fedu%2Fwp-content%2Fuploads%2F2023%2F08%2Fmenedzher"
              "-proektov-1232.jpg&imgrefurl=https%3A%2F%2Fwww.kp.ru%2Fedu%2Frabota%2Fprofessiya-menedzher-proektov%2F"
              "&docid=_4Y-T26ip_4JlM&tbnid=cNaIEP4CDpQJUM&vet=12ahUKEwjt_YWp3PKHAxVX2SoKHTdgGxcQM3oFCIYBEAA..i&w=1232"
              "&h=770&hcb=2&ved=2ahUKEwjt_YWp3PKHAxVX2SoKHTdgGxcQM3oFCIYBEAA",
        caption="Если у тебя что-то не работает, попробуй перезапустить бота командой <u>/start</u>!\n"
                "Не помогло? Есть дополнительные вопросы? Можешь написать менеджеру, он поможет тебе!",
        reply_markup=admin_link)

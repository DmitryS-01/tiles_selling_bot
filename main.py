import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.handlers.command_handlers import rt_c
from app.handlers.catalog_command_handler import rt_ctlg
from app.handlers.unexpected_messages_handlers import rt_oth

from config import BOT_TOKEN


async def main():
    # чтобы бот при включении не начал отвечать на сообщения, отправленные ему, когда тот был выключен
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(rt_c, rt_ctlg, rt_oth)  # в таком порядке будут обрабатываться сообщения

    # TODO на продакшне убрать логирование (или изменить уровень на более важные сообщения) во избежание лагов
    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


bot = Bot(token=BOT_TOKEN,
          default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

if __name__ == "__main__":
    asyncio.run(main())

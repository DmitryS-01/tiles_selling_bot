from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID


admin_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Перейти к диалогу с менеджером",
                             url=f"tg://user?id={ADMIN_ID}")
    ]
])

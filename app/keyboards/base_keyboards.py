from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID


admin_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Перейти к диалогу с менеджером",
                             url=f"tg://user?id={ADMIN_ID}")
    ]
])

shop_example = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Перейти на сайт",
                             url="https://t.me")
    ],
    [
        InlineKeyboardButton(text="Скопировать ссылку",
                             url="https://t.me"),
        InlineKeyboardButton(text="Связаться с менеджером",
                             url="https://t.me")
    ],
    [
        InlineKeyboardButton(text="Предыдущий",
                             url="https://t.me"),
        InlineKeyboardButton(text="Следующий",
                             url="https://t.me")
    ],
])

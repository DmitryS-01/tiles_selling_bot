from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID

# кнопка с контактом для решения технических проблем (используется в /help)
admin_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Перейти к диалогу с менеджером",
                             url=f"tg://user?id={ADMIN_ID}")
    ]
])

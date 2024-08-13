from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def catalog_kb(url: str) -> InlineKeyboardMarkup:
    catalog = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="На сайт",
                                 url=url)
        ]
    ])

    return catalog


def choosing_parameters(options: list[str]) -> ReplyKeyboardBuilder.as_markup:
    filters = ReplyKeyboardBuilder()
    for option in options:
        filters.add(KeyboardButton(text=option))
    return filters.as_markup(resize_keyboard=True)

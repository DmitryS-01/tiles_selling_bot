from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# конструктор reply-клавиатур
# TODO проверить, что будет при больших количествах кнопок (просмотреть лимиты)
def choosing_parameters(options: list[str]) -> ReplyKeyboardBuilder.as_markup:
    filters = ReplyKeyboardBuilder()
    for option in options:
        filters.add(KeyboardButton(text=option))
    return filters.as_markup(resize_keyboard=True)

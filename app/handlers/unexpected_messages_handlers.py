from aiogram import Router
from aiogram.types import Message, ReactionTypeEmoji

rt_oth = Router()


# так будет отвечать бот на все, что не словилось другими хендлерами
@rt_oth.message()
async def other_message(message: Message) -> None:
    await message.react([ReactionTypeEmoji(emoji="🤔")])

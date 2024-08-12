from aiogram import Router
from aiogram.types import Message, ReactionTypeEmoji, InputFile

rt_oth = Router()


@rt_oth.message()
async def other_message(message: Message) -> None:
    await message.react([ReactionTypeEmoji(emoji="🤔")])

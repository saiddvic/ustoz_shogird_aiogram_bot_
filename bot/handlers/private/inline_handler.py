from aiogram import Router
from aiogram.types import Message

inline_router = Router()
@inline_router.message()
async def inline(message: Message):
    pass

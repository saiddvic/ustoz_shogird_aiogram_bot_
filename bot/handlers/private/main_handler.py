from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from texts import help_btn

main_router = Router()

@main_router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(help_btn)





from aiogram import Router, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_router = Router()

@keyboard_router.message(CommandStart())
async def send_keyboard(message: Message):
    rkb = ReplyKeyboardBuilder()
    rkb.add(
        KeyboardButton(text='Sherik kerak'),
        KeyboardButton(text='Ish joyi kerak'),
        KeyboardButton(text='Hodim kerak'),
        KeyboardButton(text='Ustoz kerak'),
        KeyboardButton(text='Shogird kerak')
    )
    rkb.adjust(2, repeat=True)
    await message.answer(html.bold(f"""Assalom alaykum {message.from_user.full_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!"""
), reply_markup=rkb.as_markup(resize_keyboard=True), parse_mode=ParseMode.HTML)
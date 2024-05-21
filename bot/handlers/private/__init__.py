from aiogram import Router, F
from aiogram.enums import ChatType

from bot.handlers.private.callback_handler import callback_router
from bot.handlers.private.inline_handler import inline_router
from bot.handlers.private.keyboard_handler import keyboard_router
from bot.handlers.private.main_handler import main_router

private_handler_router = Router()
private_handler_router.message.filter(F.chat_type == ChatType.PRIVATE)
private_handler_router.callback_query.filter(F.chat_type == ChatType.PRIVATE)

private_handler_router.include_routers(
    callback_router,
    inline_router,
    keyboard_router,
    main_router
)
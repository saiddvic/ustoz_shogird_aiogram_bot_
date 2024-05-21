from aiogram import Router, html, Bot
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery

from config import database, CHANNEL_ID, ADMIN

callback_router = Router()
@callback_router.callback_query()
async def callback_data(callback: CallbackQuery, bot: Bot):
    callback_ = callback.data.split('_')[0]
    user_id = callback.data.split('_')[2]
    if callback_ == 'confirm':
        for order_id, order_text in database.items():
            orders_user_id = order_id.split('_')[1]
            if orders_user_id == user_id:
                await bot.send_message(chat_id=CHANNEL_ID, text=order_text)
                await bot.send_message(chat_id=int(user_id), text=f"""{html.bold("Arizangiz kanalga joylandi!")}
Tekshirish uchun: @ustozz_shogird
Omad 😁""", parse_mode=ParseMode.HTML)
                await bot.send_message(chat_id=ADMIN, text='Ariza kanalga joylandi!')
    else:
        database.pop(f"order_{user_id}", None)
        await bot.send_message(chat_id=ADMIN, text="Ariza ochirildi!")
        await bot.send_message(chat_id=int(user_id), text=html.bold("Arizangiz qabul qilinmadi‼️"),
                               parse_mode=ParseMode.HTML)










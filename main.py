import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F, html
from aiogram.enums import ContentType, ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove, KeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


from bot.handlers.private import private_handler_router
from config import ADMIN, TOKEN

from states import Form, HodimForm
from texts import *

dp = Dispatcher()

# @dp.message(F.text == 'Ish joyi kerak')
# async def name_handler(callback: CallbackQuery, state: FSMContext):
#
#     await state.set_state(Form.name)
#     await callback.answer(find_job)
#     await callback.answer(html.bold('Ism, familiyangizni kiriting?'), reply_markup=ReplyKeyboardRemove(),
#                           parse_mode=ParseMode.HTML)
#
# @dp.message(F.text == 'Ustoz kerak')
# async def name_handler(callback: CallbackQuery, state: FSMContext):
#
#     await state.set_state(Form.name)
#     await callback.answer(find_teacher)
#     await callback.answer(html.bold('Ism, familiyangizni kiriting?'), reply_markup=ReplyKeyboardRemove(),
#                           parse_mode=ParseMode.HTML)
#
# @dp.message(F.text == 'Sherik kerak')
# async def name_handler(callback: CallbackQuery, state: FSMContext):
#
#     await state.set_state(Form.name)
#     await callback.answer(find_partner)
#     await callback.answer(html.bold('Ism, familiyangizni kiriting?'), reply_markup=ReplyKeyboardRemove(),
#                       parse_mode=ParseMode.HTML)
#
# @dp.message(F.text == 'Hodim kerak')
# async def name_handler(callback: CallbackQuery, state: FSMContext):
#
#     await state.set_state(HodimForm.idora)
#     await callback.answer(find_employee)
#     await callback.answer(html.bold('🎓 Idora nomi?'), reply_markup=ReplyKeyboardRemove(),
#                       parse_mode=ParseMode.HTML)
#
#
# @dp.message(Form.name)
# async def age_handler(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Form.age)
#
#     await message.answer(age, reply_markup=ReplyKeyboardRemove())
#
# @dp.message(HodimForm.idora)
# async def idora_handler(message: Message, state: FSMContext):
#     idora = f"""Xodim kerak:
#
# 🏢 Idora:{message.text}"""
#     await state.update_data(idora=idora)
#     await state.set_state(HodimForm.tech)
#     await message.answer(technology, reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message(Form.age)
# async def tech_handler(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await state.set_state(Form.tech)
#
#     await message.answer(technology, reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message(Form.tech)
# async def phone_num_handler(message: Message, state: FSMContext):
#     await state.update_data(tech=message.text)
#     await state.set_state(Form.phone_num)
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(
#         KeyboardButton(text='Telefon raqam yuborish', request_contact=True)
#     )
#     await message.answer(phone, reply_markup=rkb.as_markup(resize_keyboard=True))
#
# @dp.message(HodimForm.tech)
# async def phone_num_handler(message: Message, state: FSMContext):
#     await state.update_data(tech=message.text)
#     await state.set_state(HodimForm.phone_num)
#     rkb = ReplyKeyboardBuilder()
#     rkb.add(
#         KeyboardButton(text='Telefon raqam yuborish', request_contact=True)
#     )
#     await message.answer(phone, reply_markup=rkb.as_markup(resize_keyboard=True))
#
#
# @dp.message(Form.phone_num, F.content_type == ContentType.CONTACT)
# async def place_handler(message: Message, state: FSMContext):
#     await state.update_data(phone_num=message.contact.phone_number)
#     await state.set_state(Form.place)
#
#     await message.answer(region, reply_markup=ReplyKeyboardRemove())
#
# @dp.message(HodimForm.phone_num, F.content_type == ContentType.CONTACT)
# async def place_handler(message: Message, state: FSMContext):
#     await state.update_data(phone_num=message.contact.phone_number)
#     await state.set_state(HodimForm.place)
#
#     await message.answer(region, reply_markup=ReplyKeyboardRemove())
#
# @dp.message(HodimForm.place)
# async def price_handler(message: Message, state: FSMContext):
#     await state.update_data(place=message.text)
#     await state.set_state(HodimForm.masul)
#
#     await message.answer("✍️Mas'ul ism sharifi?", reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message(HodimForm.masul)
# async def masul_handler(message: Message, state: FSMContext):
#     data = await state.get_data()
#     tg_username = message.from_user.username
#
#     if not tg_username:
#         tg_username = '@'
#     text = f"""{data['idora']}
# 📚 Texnologiya: {data['tech']}
# 🇺🇿 Telegram: {tg_username}
# 📞 Aloqa: +{data['phone_num']}
# 🌐 Hudud: {data['place']}
# ✍️ Mas'ul: {message.text}"""
#     await state.update_data(masul=text)
#     await state.set_state(HodimForm.con_time)
#     await message.answer(f"{contact_time} va 🕰 Ish vaqtini kiriting?", reply_markup=ReplyKeyboardRemove())
#
# @dp.message(Form.place)
# async def price_handler(message: Message, state: FSMContext):
#     await state.update_data(place=message.text)
#     await state.set_state(Form.price)
#
#     await message.answer(price, reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message(Form.price)
# async def job_handler(message: Message, state: FSMContext):
#     await state.update_data(price=message.text)
#     await state.set_state(Form.job)
#
#     await message.answer(profession, reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message(Form.job)
# async def time_handler(message: Message, state: FSMContext):
#     await state.update_data(job=message.text)
#     await state.set_state(Form.time)
#
#     await message.answer(contact_time, reply_markup=ReplyKeyboardRemove())
#
# @dp.message(HodimForm.con_time)
# async def aim_handler(message: Message, state: FSMContext):
#     await state.update_data(con_time=message.text)
#     await state.set_state(HodimForm.maosh)
#
#     await message.answer("💰 Maoshni kiriting?", reply_markup=ReplyKeyboardRemove())
#
# @dp.message(HodimForm.maosh)
# async def maosh_handler(message: Message, state: FSMContext):
#     data = await state.get_data()
#     await state.update_data(maosh=message.text)
#     await state.set_state(HodimForm.final)
#
#     text = f"""{data['masul']}
# 💰 Maosh: {message.text}
#
# #ishJoyi"""
#     database[f'order_{message.from_user.id}'] = text
#     await message.answer(text)
#     ikb = ReplyKeyboardBuilder()
#     ikb.add(
#         KeyboardButton(text='Ha'),
#         KeyboardButton(text="Yo'q")
#     )
#     ikb.adjust(2, repeat=True)
#     await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ikb.as_markup(resize_keyboard=True))
#
#
#
# @dp.message(Form.time)
# async def aim_handler(message: Message, state: FSMContext):
#     await state.update_data(time=message.text)
#     await state.set_state(Form.aim)
#
#     await message.answer(aim_text, reply_markup=ReplyKeyboardRemove())
#
#
# @dp.message(Form.aim)
# async def final_handler(message: Message, state: FSMContext):
#     await state.update_data(aim=message.text)
#     await state.set_state(Form.final)
#     data = await state.get_data()
#     tg_username = message.from_user.username
#
#
#     if not tg_username:
#         tg_username = '@'
#     xodim_text = f"""Ish joyi kerak:
#
# 👨‍💼 Xodim: {data['name']}
# 🕑 Yosh: {data['age']}
# 📚 Texnologiya: {data['tech']}
# 🇺🇿 Telegram: {tg_username}
# 📞 Aloqa: +{data['phone_num']}
# 🌐 Hudud: {data['place']}
# 💰 Narxi: {data['price']}
# 💻 Kasbi: {data['job']}
# 🕰 Murojaat qilish vaqti: {data['time']}
# 🔎 Maqsad: {data['aim']}
#
# #xodim
# """
#     database[f'order_{message.from_user.id}'] = xodim_text
#     await message.answer(xodim_text)
#     ikb = ReplyKeyboardBuilder()
#     ikb.add(
#         KeyboardButton(text='Ha'),
#         KeyboardButton(text="Yo'q")
#     )
#     ikb.adjust(2, repeat=True)
#     await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=ikb.as_markup(resize_keyboard=True))
#
#
# @dp.message(Form.final)
# async def message_handler(message: Message, state: FSMContext):
#     ikb = InlineKeyboardBuilder()
#     if message.text == 'Ha':
#         for order_id, order_text in database.items():
#             user_id = int(order_id.split('_')[1])
#             if user_id == message.from_user.id:
#                 ikb.add(
#                     InlineKeyboardButton(text='Tasdiqlash', callback_data=f"confirm_{order_id}"),
#                     InlineKeyboardButton(text="Delete", callback_data=f"delete_{order_id}")
#                 )
#                 await message.answer(f"""{html.bold("📪 So`rovingiz tekshirish uchun adminga jo`natildi!")}
#
# E'lon 24-48 soat ichida kanalda chiqariladi.""", parse_mode=ParseMode.HTML)
#
#                 await message.bot.send_message(chat_id=ADMIN, text=order_text,
#                                                reply_markup=ikb.as_markup(resize_keyboard=True))
#     elif message.text == "Yo'q":
#         user_id = message.from_user.id
#         database.pop(f"order_{user_id}", None)
#         await message.answer(html.bold("Ariza topshorish to'xtatildi!"), parse_mode=ParseMode.HTML)
#
#     await state.clear()
#
# @dp.message(HodimForm.final)
# async def message_handler(message: Message, state: FSMContext):
#     ikb = InlineKeyboardBuilder()
#     if message.text == 'Ha':
#         for order_id, order_text in database.items():
#             user_id = int(order_id.split('_')[1])
#             if user_id == message.from_user.id:
#                 ikb.add(
#                     InlineKeyboardButton(text='Tasdiqlash', callback_data=f"confirm_{order_id}"),
#                     InlineKeyboardButton(text="Delete", callback_data=f"delete_{order_id}")
#                 )
#                 await message.answer(f"""{html.bold("📪 So`rovingiz tekshirish uchun adminga jo`natildi!")}
#
# E'lon 24-48 soat ichida kanalda chiqariladi.""", parse_mode=ParseMode.HTML)
#
#                 await message.bot.send_message(chat_id=ADMIN, text=order_text,
#                                                reply_markup=ikb.as_markup(resize_keyboard=True))
#     elif message.text == "Yo'q":
#         user_id = message.from_user.id
#         database.pop(f"order_{user_id}", None)
#         await message.answer(html.bold("Ariza topshorish to'xtatildi!"), parse_mode=ParseMode.HTML)
#
#     await state.clear()

async def main() -> None:
    bot = Bot(token=TOKEN)
    dp.include_router(private_handler_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


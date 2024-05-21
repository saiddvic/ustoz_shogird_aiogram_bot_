from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    age = State()
    tech = State()
    phone_num = State()
    place = State()
    price = State()
    job = State()
    time = State()
    aim = State()
    final = State()

class HodimForm(StatesGroup):
    idora = State()
    name = State()
    tech = State()
    phone_num = State()
    place = State()
    price = State()
    con_time = State()
    masul = State()
    maosh = State()
    final = State()

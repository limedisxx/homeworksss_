from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.utils import executor

API_TOKEN = '...'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=('start'))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Рассчитать", "Информация", "Купить"]
    keyboard.add(*[KeyboardButton(text) for text in buttons])
    
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

@dp.message_handler(text='Рассчитать', state=None)
async def main_menu(message: Message):
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'),
                  InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

@dp.callback_query_handler(text='calories')
async def set_age(call: CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: CallbackQuery):
    formula_info = ("Формула Миффлина-Сан Жеора:\n"
                    "Для женщин: 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) - 161")
    await call.message.answer(formula_info)
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    bmr = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша дневная норма калорий: {bmr} ккал.")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message: Message):
    products_info = [
        {"name": "Product1", "description": "Описание 1", "price": 100},
        {"name": "Product2", "description": "Описание 2", "price": 200},
        {"name": "Product3", "description": "Описание 3", "price": 300},
        {"name": "Product4", "description": "Описание 4", "price": 400},
    ]

    for product in products_info:
        await message.answer(f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}")
        # await message.answer_photo(photo=open('path_to_image.jpg', 'rb'))

    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(
        InlineKeyboardButton('Product1', callback_data='product_buying'),
        InlineKeyboardButton('Product2', callback_data='product_buying'),
        InlineKeyboardButton('Product3', callback_data='product_buying'),
        InlineKeyboardButton('Product4', callback_data='product_buying')
    )
    
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
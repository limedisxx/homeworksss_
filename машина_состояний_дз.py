import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.filters import Сommand
from aiogram.utils import executor

# Инициализация бота
API_TOKEN = 'YOUR_API_TOKEN_HERE'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=('start'))
async def start(message: Message):
    await message.answer("Добро пожаловать! Напишите 'Calories', чтобы начать.")

@dp.message_handler(text='Calories', state=None)
async def set_age(message: Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

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

    # Пример формулы Миффлина - Сан Жеора для расчета калорий для женщин
    bmr = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша дневная норма калорий: {bmr} ккал.")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Сommand
from aiogram.types import Message

API_TOKEN = "..."
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! Я бот помогающий твоему здоровью.")
                  
@dp.message_handler()
async def all_messages(message: Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    executor.start_polling(dp, skip_updates=True)
   

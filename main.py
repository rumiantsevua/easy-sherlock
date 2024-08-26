from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import telegram_bot_token
import logging
import asyncio
from googlesearch import search


bot = Bot(token=telegram_bot_token)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привіт 🖐️ це шукач інформації в інтернеті Easy-Sherlock🔍')
    await message.answer('⚡Зараз Бот може шукати тільки перших 3 сайти в Google')
    await message.answer('✏️Напиши що треба знайти')


@dp.message()
async def echo(message: types.Message):
    global user_message
    user_message = message.text  # Сохраняем текст сообщения в переменную
    await message.reply(f"🔍Ваш запит: '{user_message}', шукаю...")
    search_info = search(user_message, num_results=3,
                         advanced=True, sleep_interval=1)
    for res in search_info:
        await message.reply(str(res.description))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

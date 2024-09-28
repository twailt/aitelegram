import html
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from generators import generate

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # Регистрация пользователя в базе данных
    await message.answer("Введи запрос для нейросети")

@router.message()
async def ai(message: Message):
    # Генерация ответа с использованием нейросети Mistral
    res = await generate(message.text)

    # Экранирование HTML символов перед отправкой
    safe_res = html.escape(res)

    await message.answer(safe_res)

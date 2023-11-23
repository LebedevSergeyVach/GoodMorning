from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from parser_weather import hourly_weather_forecast

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    user_id = message.from_user.id
    data, temperature, description, felt_temperature = hourly_weather_forecast()
    await message.reply(f"На улице:\n{data}\n{temperature}\n{description}\n{felt_temperature}")
    print(user_id)


@router.message()
async def message_handler(message: Message):
    await message.answer("Напишите команду")

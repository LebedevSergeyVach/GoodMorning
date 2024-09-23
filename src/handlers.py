from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ID_TELEGRAM

from parser.weather import hourly_weather_forecast

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    """ Start a handler for the given message """
    user_id = message.from_user.id

    if str(message.from_user.id) in ID_TELEGRAM:
        data, answer, temperature, felt_temperature, description, icon = hourly_weather_forecast()

        await message.reply(
            f"{answer}\n{data}\n{temperature}\n{felt_temperature}\n{description} {icon}."
        )
    else:
        await message.reply(
            "Вы не авторизованы для отправки сообщений."
        )

    print(user_id)


@router.message()
async def message_handler(message: Message):
    await message.answer("Напишите команду")

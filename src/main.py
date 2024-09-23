import asyncio
import logging
from datetime import datetime
import datetime

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src import config
from src.handlers import router


async def scheduled(wait_for):
    while True:
        # Получаем текущее время
        current_time = datetime.datetime.now().time()
        # Устанавливаем желаемое время отправки сообщения
        target_time = datetime.time(18, 43, 0)  # 8 утра
        # Вычисляем время до следующего желаемого времени
        delta = datetime.datetime.combine(datetime.date.today(), target_time) - datetime.datetime.combine(datetime.date.today(), current_time)
        # Если текущее время больше или равно желаемому времени, то отправляем сообщение сразу
        if current_time >= target_time:
            await main()
        # Ожидаем до следующего желаемого времени
        await asyncio.sleep(delta.seconds)


async def main():
    bot = Bot(token=config.TELEGRAM_API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

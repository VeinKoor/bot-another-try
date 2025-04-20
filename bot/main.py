import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN

from handlers import add_income_router, add_expense_router, start_router, profile_router, statistic_router, settings_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(add_income_router, add_expense_router, start_router, profile_router, statistic_router, settings_router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error('Error: %s', e)


if __name__ == '__main__':
    asyncio.run(main())
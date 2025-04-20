import asyncio
import logging

from aiogram import Bot, Dispatcher
from core.bot.config import TOKEN

from core.handlers import routers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    for router in routers:
        dp.include_routers(router)

    try:
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        logger.error('Error: %s', e)


if __name__ == '__main__':
    asyncio.run(main())
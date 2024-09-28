import asyncio
from aiogram import Bot, Dispatcher
from app.user import router
from config import TG_TOKEN
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


async def shutdown():
    # Здесь можно закрыть подключения или выполнить другие задачи
    pass

async def main():
    bot = Bot(token=TG_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(router)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

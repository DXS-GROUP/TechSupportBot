import asyncio

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from setproctitle import setproctitle

from db.db import create_connection, create_table
from handlers import bot, dp


async def main() -> None:
    connection = await create_connection()
    await create_table(connection)

    await dp.start_polling(bot)


if __name__ == "__main__":
    setproctitle("TechSupportBot")
    asyncio.run(main())

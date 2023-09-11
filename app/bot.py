import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot
from aiogram.enums import ParseMode

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.send_message(getenv("CHAT_ID"), "hey")
    # And the run events dispatching
    # await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

from os import getenv

from aiogram import Bot
from aiogram.enums import ParseMode

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")


async def send_message(message) -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.send_message(getenv("CHAT_ID"), message)
    await bot.close()

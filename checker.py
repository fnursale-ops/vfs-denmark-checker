import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

async def main():
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text="✅ Telegram test mesajı başarılı. Sistem çalışıyor."
        )
        print("TEST MESAJI GONDERILDI")

    except Exception as e:
        print(e)

asyncio.run(main())

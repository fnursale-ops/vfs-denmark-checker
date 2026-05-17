import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
EMAIL = os.getenv("VFS_EMAIL")
PASSWORD = os.getenv("VFS_PASSWORD")

LOGIN_URL = "https://visa.vfsglobal.com/tur/tr/dnk/login"

bot = Bot(token=TELEGRAM_TOKEN)

async def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

async def check_slots():
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()

        try:
            await page.goto(LOGIN_URL, timeout=120000)

            await page.fill('input[type="email"]', EMAIL)
            await page.fill('input[type="password"]', PASSWORD)

            await page.click('button[type="submit"]')

            await page.wait_for_timeout(15000)

            content = await page.content()

            keywords = [
                "Earliest Available Slot",
                "Available",
                "Select Date"
            ]

            found = any(word in content for word in keywords)

            if found:
                await send_message(
                    "🇩🇰 Danimarka VFS randevusu bulundu!"
                )
                print("SLOT BULUNDU")
            else:
                print("Slot yok")

        except Exception as e:
            print(e)

        finally:
            await browser.close()

asyncio.run(check_slots())
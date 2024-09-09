from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
import asyncio
from config import TOKEN, CHAT_ID

# Ініціалізація бота
bot = Bot(token=TOKEN)

# Налаштування логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функція для відправки повідомлення
async def send_message():
    try:
        await bot.send_photo(chat_id=CHAT_ID,
                             photo='./img.png',  # Шлях до зображення або URL
                             connect_timeout=60,
                             caption="⛈☀️")
        logger.info("Повідомлення успішно відправлено")
    except Exception as e:
        logger.error(f"Помилка при відправленні повідомлення: {e}")

# Ініціалізація планувальника
scheduler = AsyncIOScheduler()

# Додання завдань для різних часів
scheduler.add_job(send_message, 'cron', hour=5, minute=0)
scheduler.add_job(send_message, 'cron', hour=12, minute=0)
scheduler.add_job(send_message, 'cron', hour=17, minute=0)

# Запуск планувальника та асинхронного циклу
if __name__ == '__main__':
    try:
        logger.info("Бот запущений")
        scheduler.start()
        asyncio.get_event_loop().run_forever()  # Запускаємо цикл подій
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот зупинений")

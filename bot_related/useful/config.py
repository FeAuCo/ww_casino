import aiogram
import dotenv
import os

dotenv.load_dotenv()

bot = aiogram.Bot(token=os.getenv('TG_BOT_TOKEN'))
dp = aiogram.Dispatcher()

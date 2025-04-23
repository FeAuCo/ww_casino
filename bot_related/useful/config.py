import aiogram
import dotenv
import ww_casino.bot_related.cfg as cfg

dotenv.load_dotenv()

bot = aiogram.Bot(token=cfg.TG_BOT_TOKEN)
dp = aiogram.Dispatcher()

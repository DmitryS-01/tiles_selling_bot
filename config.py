import os
import dotenv

dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")  # API-токен бота в тг
ADMIN_ID = os.getenv("ADMIN_ID")  # id аккаунта админа в тг (не юзернейм, а ид)

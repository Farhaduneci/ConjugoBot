import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["TOKEN"]
NAME = os.environ["NAME"]

IS_MAINTENANCE = bool(int(os.environ["IS_MAINTENANCE"]))

ADMIN_TELEGRAM_USER_ID = int(os.environ["ADMIN_TELEGRAM_USER_ID"])
LIST_OF_ADMINS = [ADMIN_TELEGRAM_USER_ID]

WEBHOOK = False
# The following configuration is only needed if you setted WEBHOOK to True
WEBHOOK_OPTIONS = {
    "listen": "0.0.0.0",  # IP
    "port": 443,
    "url_path": TOKEN,  # This is recommended for avoiding random people
    # making fake updates to your bot
    "webhook_url": f"https://example.com/{TOKEN}",
}

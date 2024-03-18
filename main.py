import sentry_sdk

from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import filters
from telegram.ext import MessageHandler
from telegram.ext import PicklePersistence

from commands.maintenance import maintenance
from commands.start import start
from commands.conjugate import conjugate
from configurations import settings
from configurations.settings import IS_MAINTENANCE, SENTRY_DSN
from utils import logger


if __name__ == "__main__":
    sentry_sdk.init(dsn=SENTRY_DSN)
    logger.init_logger(f"logs/bot.log")

    persistence = PicklePersistence(filepath="conversation_states.pickle")
    application = (
        Application.builder()
        .token(settings.TOKEN)
        .read_timeout(50)
        .write_timeout(50)
        .get_updates_read_timeout(50)
        .persistence(persistence)
        .build()
    )

    application.add_handler(CommandHandler("start", start))

    if IS_MAINTENANCE:
        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, maintenance)
        )
    else:
        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, conjugate)
        )

    print("Starting to poll...")

    application.run_polling()

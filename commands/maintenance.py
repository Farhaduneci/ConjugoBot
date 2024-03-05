from logging import getLogger

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from utils.decorators import send_action

logger = getLogger(__name__)


@send_action(ChatAction.TYPING)
async def maintenance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:

    # pylint: disable=unused-argument
    await context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Bot is under maintenance. Please try again later.",
    )

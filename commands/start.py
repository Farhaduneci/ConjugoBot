from logging import getLogger
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from constants import messages
from utils.decorators import send_action

logger = getLogger(__name__)


@send_action(ChatAction.TYPING)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:

    # pylint: disable=unused-argument
    await update.message.reply_text(
        text=messages.START_TEXT,
        reply_to_message_id=update.message.id,
    )

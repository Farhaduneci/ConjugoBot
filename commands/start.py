from logging import getLogger
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from utils.decorators import send_action

logger = getLogger(__name__)

START_TEXT = """
Hello and welcome here. 👋

You can send me the present, past and past participle of a verb and I will tell you what the other forms are.
"""


@send_action(ChatAction.TYPING)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:

    # pylint: disable=unused-argument
    await update.message.reply_text(
        text=START_TEXT,
    )

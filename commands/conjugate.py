from logging import getLogger
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes
from constants import messages
from utils.decorators import send_action


import aiosqlite
import asyncio


logger = getLogger(__name__)


async def search_verbs_async(query):
    async with aiosqlite.connect("irregular_verbs.db") as conn:
        cursor = await conn.execute(
            "SELECT * FROM verbs WHERE verbs MATCH ? ORDER BY rank LIMIT 5", (query,)
        )
        results = await cursor.fetchall()
        return results


@send_action(ChatAction.TYPING)
async def conjugate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    search_query = update.message.text
    matching_verbs = await search_verbs_async(search_query)

    if not matching_verbs:
        await update.message.reply_text(
            text=messages.FAILIOR_TEXT,
            reply_to_message_id=update.message.id,
        )
        return

    await update.message.reply_text(
        text=messages.SUCSUSS_TEXT.format(
            verbs="\n".join([" | ".join(row) for row in matching_verbs])
        ),
        reply_to_message_id=update.message.id,
    )

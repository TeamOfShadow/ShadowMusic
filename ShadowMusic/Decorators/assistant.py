import asyncio 
import random
from typing import Dict, List, Union

from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant

from ShadowMusic import MUSIC_BOT_NAME, app
from ShadowMusic.Database import get_assistant, save_assistant
from ShadowMusic.Utilities.assistant import get_assistant_details, random_assistant


def AssistantAdd(mystic):
    async def wrapper(_, message):
        _assistant = await get_assistant(message.chat.id, "assistant")
        if not _assistant:
            ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(message.chat.id, "assistant", assis)
        else:
            ran_ass = _assistant["saveassistant"]
        ASS_ID, ASS_NAME, ASS_USERNAME, ASS_ACC = await get_assistant_details(
            ran_ass
        )
        try:
            b = await app.get_chat_member(message.chat.id, ASS_ID)
            if b.status == "kicked":
                return await message.reply_text(
                    f"Assistant Account [{ASS_ID}] is banned.\nUnban it first to use Music Bot\n\nUsername: @{ASS_USERNAME}"
                )
        except UserNotParticipant:
            if message.chat.username:
                try:
                    await ASS_ACC.join_chat(message.chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
            else:
                try:
                    xxy = await app.export_chat_invite_link(message.chat.id)
                    inv_lnk = str(xxy)
                    inv_lnk = inv_lnk.replace("https://t.me/+","https://t.me/joinchat/")
                    await asyncio.sleep(10)
                    await ASS_ACC.join_chat(inv_lnk)
                    await message.reply(f"{ASSNAME} Joined Successfully") 
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
        return await mystic(_, message)

    return wrapper

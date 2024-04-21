import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from STORMDB.data import STORMS, EMOJI
from config import SUDO_USERS, OWNER_ID

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["emoji"], ["."]))
async def emoji(xspam: Client, e: Message):
    kex = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    if len(kex) == 2:
        ok = await xspam.get_users(kex[1])
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(EMOJI)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    elif e.reply_to_message:
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        counts = int(kex[0])
        for _ in range(counts):
            reply = choice(EMOJI)
            msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.1)

    else:
        await e.reply_text(".ᴇᴍᴏᴊɪ 10 <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ>")

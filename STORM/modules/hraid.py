import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from STORMDB.data import STORMS, HRAID
from config import SUDO_USERS, OWNER_ID

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["hraid"], ["."]))
async def hraid(xspam: Client, message: Message):  
    kex = message.text.split(" ")

    if len(kex) > 2:
        ok = await xspam.get_users(kex[2])
        id = ok.id
        if id in STORMS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        elif id in SUDO_USERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
        else:
            counts = int(kex[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(HRAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    elif message.reply_to_message and (len(kex) == 2):
        user_id = message.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if id in STORMS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        elif id in SUDO_USERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
        else:
            counts = int(kex[1])
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(HRAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".ʜʀᴀɪᴅ 10 <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

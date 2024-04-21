import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from STORMDB.data import STORMS, RAID
from config import SUDO_USERS, OWNER_ID

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], ["."]))
async def raid(xspam: Client, message: Message):  
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
                reply = choice(RAID)
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
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(message.chat.id, msg)
                await asyncio.sleep(0.3)

    else:
        await message.reply_text(".ʀᴀɪᴅ 10 <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

rusers = []

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], ["."]))
async def rraid(xspam: Client, message: Message):
    global rusers
    kex = message.text.split(" ")

    if len(kex) > 1:
        ok = await xspam.get_users(kex[1])
        id = ok.id
        if id in STORMS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
        elif id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        elif id in SUDO_USERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
        else:
            rusers.append(id)
            await message.reply_text("ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if user_id in STORMS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ꜱᴛᴏʀᴍ'ꜱ ᴏᴡɴᴇʀ ☠️")
        elif user_id == OWNER_ID:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ 🥀")
        elif user_id in SUDO_USERS:
            await message.reply_text("ɴᴏᴘᴇ ᴛʜɪꜱ ɢᴜʏꜱ ɪꜱ ꜱᴜᴅᴏ ᴜꜱᴇʀ 💗")
        else:
            rusers.append(user_id)
            await message.reply_text("» ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʀᴇᴘʟʏʀᴀɪᴅ ✅")

    else:
        await message.reply_text(".ʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["drraid", "draid", "dreplyraid"], ["."]))
async def draid(xspam: Client, message: Message):
    global rusers
    kex = message.text.split(" ")

    if len(kex) > 1:
        ok = await xspam.get_users(kex[1])
        id = ok.id
        if id in rusers:
            rusers.remove(id)
            await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if id in rusers:
            rusers.remove(id)
            await message.reply_text("ʀᴇᴘʟʏ ʀᴀɪᴅ ᴅᴇ-ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅")

    else:
        await message.reply_text(".ᴅʀʀᴀɪᴅ <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")

@Client.on_message(~filters.me & filters.incoming)
async def watcher(_, msg: Message):
    global rusers
    id = msg.from_user.id
    if id in rusers:
        reply = choice(RAID)
        await msg.reply_text(reply)

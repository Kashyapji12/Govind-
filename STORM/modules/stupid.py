from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["stupid"], ["."]))
async def stupid(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("ꜱᴛᴜᴘɪᴅ...")
    animation_chars = [
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "ʏᴏᴜʀ ʙʀᴀɪɴ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit(animation_chars[i % 14])

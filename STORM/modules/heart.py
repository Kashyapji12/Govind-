from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["heart", "love"], ["."]))
async def hearts(client: Client, message: Message):
    await message.edit("❤️")
    await asyncio.sleep(0.5)
    await message.edit("❤️ ɪ")
    await asyncio.sleep(0.5)
    await message.edit("❤️ ɪ ʟᴏᴠᴇ")
    await asyncio.sleep(0.5)
    await message.edit("❤️ ɪ ʟᴏᴠᴇ ʏᴏᴜ")
    await asyncio.sleep(3)
    await message.edit("❤️ ɪ ʟᴏᴠᴇ ʏᴏᴜ <3")

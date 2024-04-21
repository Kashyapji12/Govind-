from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["globe", "earth"], ["."]))
async def globe(client: Client, message: Message):
    await message.edit("🌏")
    await asyncio.sleep(0.5)
    await message.edit("🌏")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
    await asyncio.sleep(0.5)
    await message.edit("🌎")
    await asyncio.sleep(0.5)
    await message.edit("🌎")
    await asyncio.sleep(0.5)
    await message.edit("🌎")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
    await asyncio.sleep(0.5)
    await message.edit("🌏")
    await asyncio.sleep(0.5)
    await message.edit("🌍")
    await asyncio.sleep(0.5)
    await message.edit("🌍")

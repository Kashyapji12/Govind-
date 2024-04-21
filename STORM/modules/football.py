from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["football"], ["."]))
async def football(_, e: Message):       
      Fuk = await e.reply("⚽️")

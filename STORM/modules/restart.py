import sys
import datetime
from os import execle, environ
from config import SUDO_USERS
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["instantboot", "restart"], ["."]))
async def restart_bot(_, message: Message):
    msg = await message.edit("ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    args = ["python3", "-m", "STORM"]
    await msg.edit("ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    os.execv(sys.executable, [sys.executable] + args)     

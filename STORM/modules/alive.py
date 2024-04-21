import sys
import datetime
from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS
from pyrogram import Client, filters
from pyrogram.types import Message

KEX = f"""ㅤ ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ ‌🪽
➖➖➖➖➖➖➖➖➖➖➖
**• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** 🐍: `3.11.3`
**• ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀꜱɪᴏɴ** ⚙️: `M2.0`
**• ɢʀᴏᴜᴘ 💫: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🥀](https://t.me/STORM_CHATZ)**
**• ᴄʜᴀɴɴᴇʟ ✨: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🥀](https://t.me/STORM_TECHH)**
**• ꜱᴇɴꜱᴇɪ 🫂: [ꜱᴛᴏʀᴍ 🥀](https://t.me/kexx_XD)**
➖➖➖➖➖➖➖➖➖➖➖"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["."]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=KEX)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.   id, ALIVE_PIC, caption=KEX)    

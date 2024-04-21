from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

CONVERT_TEXT = f"""
**ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}tts` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ....

• `{hl}quotly` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ Qᴜᴏᴛᴇ....

• `{hl}clone` » ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴏʀ ᴄʟᴏɴᴇ ʏᴏᴜʀꜱᴇʟꜰ ᴛᴏ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ

• `{hl}revert` » ᴛᴏ ʀᴇᴠᴇʀᴛ ʏᴏᴜʀ ᴄʟᴏɴᴇ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpconvert"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=CONVERT_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=CONVERT_TEXT) 

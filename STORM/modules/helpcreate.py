from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

CREATE_TEXT = f"""
**ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}create group (name)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ɢʀᴏᴜᴘ....

• `{hl}create channel (name)` » ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ....
"""                                     

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpcreate"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=CREATE_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=CREATE_TEXT)                                

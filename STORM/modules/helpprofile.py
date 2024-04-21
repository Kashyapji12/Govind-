from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

PROFILE_TEXT = f"""
**ᴘʀᴏꜰɪʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ** 

• `{hl}block` » ᴛᴏ ᴀᴅᴅ ꜱᴏᴍᴇᴏɴᴇ ɪɴ ʏᴏᴜʀ ʙʟᴏᴄᴋʟɪꜱᴛ....

• `{hl}unblock` » ᴛᴏ ᴜɴʙʟᴏᴄᴋ ꜱᴏᴍᴇᴏɴᴇ....
    
• `{hl}setname` » ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ɴᴇᴡ ɴᴀᴍᴇ...

• `{hl}setbio` » ᴛᴏ ꜱᴇᴛ ʏᴏᴜʀ ʙɪᴏ...

• `{hl}setpfp` » ᴛᴏ ꜱᴇᴛ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄᴛᴜʀᴇ....

• `{hl}vpfp` » ᴛᴏ ꜱᴇᴛ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄᴛᴜʀᴇ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpprofile"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=PROFILE_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=PROFILE_TEXT)

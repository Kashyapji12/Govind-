from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

VC_TEXT = f"""
**ᴠᴄ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}startvc` » ᴛᴏ ꜱᴛᴀʀᴛ ᴠᴄ....

• `{hl}stopvc` » ᴛᴏ ꜱᴛᴏᴘ ᴠᴄ....

• **ᴠᴄ ꜰɪɢʜᴛ ᴘʟᴜɢɪɴꜱ ᴡᴇʀᴇ ʟᴏᴀᴅᴇᴅ ɪɴ ɴᴇxᴛ ᴜᴘᴅᴀᴛᴇ**

"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpvc"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=VC_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=VC_TEXT) 
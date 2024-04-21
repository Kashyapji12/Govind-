from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

DM_TEXT = f"""
**ᴅᴍ/ᴘᴍ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}nice` » ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴇʟꜰ ᴅᴇꜱᴛʀᴜᴄᴛ ɪᴍɢ/ɴᴏʀᴍᴀʟ ᴍᴇᴅɪᴀ...

• `{hl}setwarns` <ᴄᴏᴜɴᴛ> » ᴛᴏ ꜱᴇᴛ ᴘᴍ ꜱᴘᴀᴍ ᴡᴀʀɴꜱ..

• `{hl}disapprove` » ᴅɪꜱᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ᴛᴏ ᴘᴍ ʏᴏᴜ...

• `{hl}approve` » ᴀᴘᴘʀᴏᴠᴇ ᴜꜱᴇʀ ᴛᴏ ᴘᴍ ʏᴏᴜ...

• `{hl}pmpermit [on | off]` » ᴛᴏ ᴏɴ/ᴏꜰꜰ ᴋᴇx ᴘᴍ ꜱᴇᴄᴜʀɪᴛʏ..

• `{hl}dmspam` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴅᴏ ᴅᴍ ꜱᴘᴀᴍ ᴏɴ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ....

• `{hl}dmraid` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴅᴏ ᴅᴍ ʀᴀɪᴅ ᴏɴ ᴛᴀʀɢᴇᴛᴇᴅ ᴜꜱᴇʀ....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helppm"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=DM_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=DM_TEXT)

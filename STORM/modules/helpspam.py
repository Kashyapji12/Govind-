from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

SPAM_TEXT = f"""
**ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}spam` » ᴛᴏ ꜱᴘᴀᴍ ᴍᴇꜱꜱᴀɢᴇꜱ ʙʏ ᴄᴏᴜɴᴛ....

• `{hl}banall` » ᴛᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ᴏꜰ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛꜱ....

• `{hl}raid` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ....

• `{hl}replyraid` » ᴛᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ ᴏɴ ᴀɴʏᴏɴᴇ....

• `{hl}dreplyraid` » ᴛᴏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇ ʀᴇᴘʟʏʀᴀɪᴅ....

• `{hl}abuse` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴛᴏ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ....

• `{hl}bspam` <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ> » ᴄʜᴇᴄᴋ ʙʏ ʏᴏᴜʀꜱᴇʟꜰ....

• `{hl}hang` <ᴄᴏᴜɴᴛ> » ꜱᴘᴀᴍꜱ ʜᴀɴɢ ᴍꜱɢꜱ ɪɴ ᴄʜᴀᴛ.....
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpspam"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=SPAM_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=SPAM_TEXT)

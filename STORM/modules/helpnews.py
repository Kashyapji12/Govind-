from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

NEWS_TEXT = f"""
**ɪɴᴛᴇʀɴᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}news` » ᴛᴏ ɢᴇᴛ ᴛᴏᴘ 5 ʜᴇᴀᴅʟɪɴᴇꜱ ᴏꜰ ɴᴇᴡꜱ....

• `{hl}weather (ʏᴏᴜʀ ᴄɪᴛʏ)` » ᴛᴏ ɢᴇᴛ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....

• `{hl}ai (ʏᴏᴜʀ Qᴜᴇʀʏ)` » ᴄʜᴇᴄᴋ ʏᴏᴜʀꜱᴇʟꜰ......

• `{hl}google (ʏᴏᴜʀ Qᴜᴇʀʏ)` » ᴄʜᴇᴄᴋ ʏᴏᴜʀꜱᴇʟꜰ......

• `{hl}gitinfo` <username> » ᴛᴏ ɢᴇᴛ ɢɪᴛ ᴀᴄᴄ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ....

• `{hl}video` <ᴠɪᴅᴇᴏ ɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴠɪᴀ [ʏᴏᴜᴛᴜʙᴇ](https://www.youtube.com)...

• `{hl}music` <ᴍᴜꜱɪᴄ ɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴜꜱɪᴄ ᴠɪᴀ ᴍᴘ3...

• `{hl}telegraph` <ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ/ᴛᴇxᴛ> » ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴍᴇᴅɪᴀ /ᴛᴇxᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.

• `{hl}lyrics` <ᴍᴜꜱɪᴄ | ᴀʀᴛɪꜱᴛ ɴᴀᴍᴇ> » ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟʏʀɪᴄꜱ...

• `{hl}download` <ɪɴꜱᴛᴀɢʀᴀᴍ ᴘᴜʙ ʀᴇᴇʟ ᴜʀʟ> » ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴘᴜʙʟɪᴄ ʀᴇᴇʟ/ᴘᴏꜱᴛ/ꜱᴛᴏʀʏ...
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpinternet"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=NEWS_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=NEWS_TEXT) 

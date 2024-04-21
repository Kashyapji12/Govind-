from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

FACTION_TEXT = f"""
**ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅꜱ**

• `{hl}ftyping` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴛʏᴘɪɴɢ....

• `{hl}fvideo` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴠɪᴅ....

• `{hl}faudio` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴀᴜᴅ......

• `{hl}fround` » ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ʀᴏᴜɴᴅ.....

• `{hl}fphoto` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴘɪᴄ....

• `{hl}fsticker` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ꜱᴛɪᴄ...

• `{hl}fdocument` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ᴅᴏᴄ..

• `{hl}flocation` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ꜱᴇɴᴅɪɴɢ ʟᴏᴄ...

• `{hl}fgame` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏꜰ ᴘʟᴀʏɪɴɢ ɢᴀᴍᴇ...

• `{hl}fcontact` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴄᴏɴᴛᴀᴄᴛ..

• `{hl}fscreen` ᴛᴏ ᴘᴇʀꜰᴏʀᴍ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ...

• `{hl}fstop` ᴛᴏ ꜱᴛᴏᴘ ꜰᴀᴋᴇ ᴀᴄᴛɪᴏɴ...
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["helpfaction"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=FACTION_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=FACTION_TEXT) 
from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["bstats"], ["."]))
async def bstats(client, message):
    msg = f"""
    ** ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ **

    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » **[Kᴜɴᴀʟ࿐](https://t.me/kexx_xd)**
    • **ᴠᴇʀꜱɪᴏɴ** » **2.1.0**
    • **ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇꜱ** » **80+**
    • **ᴛᴏᴛᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ** » **107+**  
    • **ʙʀᴀɴᴄʜ** » **2.1.0@main**
    • **ᴜꜱᴇʀʙᴏᴛ ʀᴇᴘᴏ** » **[ꜱᴛᴏʀᴍ-ᴜꜱᴇʀʙᴏᴛ](https://github.com/VARC9210/STORM-USERBOT)**
    • **ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** » **[ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ](https://t.me/STORM_CHATZ)**
    • **ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ** » **[ꜱᴛᴏʀᴍ ᴛᴇᴄʜ](https://t.me/STORM_TECHH)**    
    
    **ʙʏ @kexx_xd**
    """
    await message.edit(msg)

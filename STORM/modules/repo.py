from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["repo"], ["."]))
async def repo(client, message):
    msg = f"""
    ** ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ **

    • **ɢɪᴛʜᴜʙ** » [click here](https://github.com/VARC9210/STORM-USERBOT) 
    • **ꜱᴜᴘᴘᴏʀᴛ** » [click here](https://t.me/STORM_CHATZ) 
    • **ᴜᴘᴅᴀᴛᴇꜱ** » [click here](https://t.me/STORM_TECHH)
    • **ᴅᴇᴠᴇʟᴏᴘᴇʀ** » [click here](https://t.me/kexx_xd)
    
    **ʙʏ @kexx_xd**
    """
    await message.edit(msg)

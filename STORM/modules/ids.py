from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["id"], ["."]))
async def find_id(client, message):
    if message.reply_to_message is None:
        await message.edit(f"ᴄʜᴀᴛ ɪᴅ » `{message.chat.id}`")
    else:
        await message.edit(f"ᴜsᴇʀ ɪᴅ » `{message.reply_to_message.from_user.id}`\nᴄʜᴀᴛ ɪᴅ » `{message.chat.id}`")

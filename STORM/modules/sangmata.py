import asyncio
from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *
from STORM.modules.profile import extract_user
from config import SUDO_USERS

@Client.on_message(filters.command(["sg", "sa", "sangmata"], ".") & filters.me)
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["sg", "sa", "sangmata"], ["."]))
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.edit_text("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ᴀ ᴠᴀʟɪᴅ ᴜꜱᴇʀ.......")
    bot = "SangMata_BOT"
    try:
        await client.send_message(bot, f"allhistory {user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"allhistory {user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await message.edit_text("**ᴛʜɪꜱ ᴘᴇʀꜱᴏɴ ʜᴀꜱ ɴᴇᴠᴇʀ ᴄʜᴀɴɢᴇᴅ ʜɪꜱ ɴᴀᴍᴇ**")
            return
        elif stalk:
            await message.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await message.reply(stalk.text)
            await stalk.delete()

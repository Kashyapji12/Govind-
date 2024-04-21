import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["chance"], [hl]))
async def chance(client, message):
    text = message.text.split(hl + "chance ", maxsplit=1)[1]
    chance_percentage = random.randint(1, 100)
    await message.reply(f"**{text}**\n\n**ᴄʜᴀɴᴄᴇ**: {chance_percentage}%")

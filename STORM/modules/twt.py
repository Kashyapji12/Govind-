import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from STORM.powers import get_text
from config import SUDO_USERS
hl = "."

@Client.on_message(filters.command("tweet", hl) & filters.me)
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["tweet"], ["."]))
async def tweet(client: Client, message: Message):
    text = get_text(message)
    input_str = get_text(message)
    if text:
        if ":" in text:
            stark = input_str.split(":", 1)
        else:
            await message.edit(f"**ᴜsᴀɢᴇ »** \n\n{hl}tweet ᴜsᴇʀɴᴀᴍᴇ:ᴛᴇxᴛ")
            return
    if len(message.command) < 2:
        await message.edit(f"**ᴜsᴀɢᴇ »** {hl}tweet ᴜsᴇʀɴᴀᴍᴇ:ᴛᴇxᴛ")
        return
    tony = stark[0]
    shiva = stark[1]
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={tony}&text={shiva}"
    seg = requests.get(url=url).json()
    tweet = seg["message"]
    await message.edit(f"ᴡᴀɪᴛ ɪ ᴀᴍ ᴛᴡᴇᴇᴛɪɴɢ...💥")
    await client.send_photo(message.chat.id, tweet)
    await message.delete()

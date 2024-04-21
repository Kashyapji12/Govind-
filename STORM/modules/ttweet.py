from pyrogram.types import Message
import requests
from STORM.powers import get_text
from pyrogram import Client, filters
from config import SUDO_USERS
hl = "."

@Client.on_message(filters.command("trumptwt", hl) & filters.me)
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["trumptwt"], ["."]))
async def ttweet(client: Client, message: Message):
    text = get_text(message)
    if not text:
        await message.edit(f"ɢɪᴠᴇ ᴍᴇ sᴏᴍᴛʜɪɴɢ ᴛᴏ ᴛᴡᴇᴇᴛ....")
        return
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}"
    r = requests.get(url=url).json()
    tweet = r["message"]
    await message.edit(f"ᴛʀᴜᴍᴘ ɪs ᴛᴡᴇᴇᴛɪɴɢ....⚡")
    await client.send_photo(message.chat.id, tweet)
    await message.delete()

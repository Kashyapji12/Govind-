import openai
from pyrogram import Client, filters
from config import SUDO_USERS, OPENAIKEY

openai.api_key = OPENAIKEY
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ai"], ["."]))
async def openai_command(client, message):
    prompt = message.text.split(".ai ", maxsplit=1)[1]
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=100
        )
        completion_text = response.choices[0].text.strip()
        await message.reply(completion_text)
    except Exception as e:
        await message.reply(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {e}")

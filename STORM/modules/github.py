import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["gitinfo"], ["."]))
async def githubuser(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text(f". ɢɪᴛɪɴꜰᴏ [ᴜꜱᴇʀɴᴀᴍᴇ]")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("ᴇʀʀᴏʀ: ᴜsᴇʀɴᴀᴍᴇ ɴᴏᴛ ғᴏᴜɴᴅ....")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**• ɪɴꜰᴏ {name}**
**• ᴜsᴇʀɴᴀᴍᴇ:** `{username}`
**• ʙɪᴏ:** `{bio}`
**• ᴘʀᴏғɪʟᴇ ʟɪɴᴋ:** [Here]({url})
**• ᴄᴏᴍᴘᴀɴʏ:** `{company}`
**• ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created_at}`
**• ʀᴇᴘᴏsɪᴛᴏʀɪᴇs:** `{repositories}`
**• ʙʟᴏɢ:** `{blog}`
**• ʟᴏᴄᴀᴛɪᴏɴ:** `{location}`
**• ғᴏʟʟᴏᴡᴇʀs:** `{followers}`
**• ғᴏʟʟᴏᴡɪɴɢ:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)

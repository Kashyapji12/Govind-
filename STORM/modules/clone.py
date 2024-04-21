import os
from pyrogram import *
from pyrogram.types import *
from STORM.helper.basic import edit_or_reply, get_text, get_user
from config import SUDO_USERS

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "404 : Bio Lost")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["clone"], ["."]))
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await message.edit_text("ᴄʟᴏɴɪɴɢ.....")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("ᴡʜᴏᴍ ɪ ꜱʜᴏᴜʟᴅ ᴄʟᴏɴᴇ.....?")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**ɴᴏᴡ ɪ'ᴍ** {f_name}")

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["revert"], ["."]))
async def revert(client: Client, message: Message):
    await message.edit("ʀᴇᴠᴇʀᴛɪɴɢ......")
    r_bio = BIO

    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("ɪ ᴀᴍ ʙᴀᴄᴋ....!")

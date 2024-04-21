from config import SUDO_USERS
from STORMDB.data import GROUP
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["join"], ["."]) & filters.user(SUDO_USERS))
async def join(client: Client, message: Message):
    kex = message.text.split(" ")
    if len(kex) == 1:
        return await message.reply_text("ɴᴇᴇᴅ ᴀ ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ-ɪᴅ ᴏʀ ɪɴᴠɪᴛᴇ ʟɪɴᴋ ᴛᴏ ᴊᴏɪɴ")
    try:
        await client.join_chat(kex[1])
        await message.reply_text(f"ᴊᴏɪɴᴇᴅ ✅")
    except Exception as ex:
        await message.reply_text(f"ᴇʀʀᴏʀ\n\n{str(ex)}")
  

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["leave", "remove"], ["."]))
async def leave(xspam: Client, message: Message):
    kex = message.text.split(" ")
    if len(kex) > 1:
        if kex[1] in GROUP:
            return
        try:
           await xspam.leave_chat(kex[1])
           await message.reply_text(f"ʟᴇꜰᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🥀")
        except Exception as ex:
           await message.reply_text(f"ᴇʀʀᴏʀ\n\n{str(ex)}")
    else:
        chat = message.chat.id
        ok = message.from_user.id
        if chat == ok:
            return await message.reply_text(f"!ʟᴇᴀᴠᴇ <ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ>")
        elif chat in GROUP:
              return
        try:
           await xspam.leave_chat(chat)
           await message.reply_text(f"ʟᴇꜰᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 🥀")
        except Exception as ex:
           await message.reply_text(f"ᴇʀʀᴏʀ\n\n{str(ex)}")

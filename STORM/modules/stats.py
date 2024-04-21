from datetime import datetime
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["mystats", "mystatus"], ["."]))
async def stats(client: Client, message: Message):
    bunny = await message.edit("ᴄᴏʟʟᴇᴄᴛɪɴɢ ꜱᴛᴀᴛꜱ...⚡")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    meh = await client.get_me()
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE:
            u += 1
        elif dialog.chat.type == enums.ChatType.BOT:
            b += 1
        elif dialog.chat.type == enums.ChatType.GROUP:
            g += 1
        elif dialog.chat.type == enums.ChatType.SUPERGROUP:
            sg += 1
            user_s = await dialog.chat.get_member(int(meh.id))
            if user_s.status in (
                enums.ChatMemberStatus.OWNER,
                enums.ChatMemberStatus.ADMINISTRATOR,
            ):
                a_chat += 1
        elif dialog.chat.type == enums.ChatType.CHANNEL:
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await bunny.edit_text(
        """
**ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜱᴛᴀᴛꜱ ʙʏ ꜱᴛᴏʀᴍ**

**• `{}` ᴘʀɪᴠᴀᴛᴇ ᴍᴇssᴀɢᴇs**

**• `{}` ɢʀᴏᴜᴘs**

**• `{}` sᴜᴘᴇʀ ɢʀᴏᴜᴘs**

**• `{}` ᴄʜᴀɴɴᴇʟs**

**• `{}` ᴄʜᴀᴛs ᴜʀ ᴀᴅᴍɪɴ ɪɴ**

**• `{}` ʙᴏᴛs**""".format(
            ms, u, g, sg, c, a_chat, b
        )
    )

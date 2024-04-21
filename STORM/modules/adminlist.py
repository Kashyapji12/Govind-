from pyrogram import Client, filters, enums
from config import SUDO_USERS

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["admins", "adminlist", "staff"], ["."]))
async def allstaff(client, message):
    creator = None
    admins = []
    bots = []
    deleted = []
    ok = await message.edit("ꜰᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴꜱ...")
    async for x in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if x.user.is_bot:
            bots.append(x.user.mention)
        elif x.status.name == "OWNER":
            creator = x.user.mention
        elif x.user.is_deleted:
            deleted.append(x.user.mention)
        else:
            admins.append(x.user.mention)

    txt = f"**{message.chat.title} ꜱᴛᴀꜰꜰ :**"
    txt += "\n\n"
    txt += " 👑**ᴄʀᴇᴀᴛᴏʀ :**"
    txt += "\n"
    txt += f" • {creator}"
    txt += "\n"
    if admins:
        txt += "\n"
        txt += " 👨‍💻**ᴀᴅᴍɪɴꜱ :**"
        txt += "\n"
        for adm in admins:
            txt += f" • {adm}"
            txt += "\n"
    if bots:
        txt += "\n"
        txt += " 🤖**ʙᴏᴛꜱ :**"
        txt += "\n"
        for adm in bots:
            txt += f" • {adm}"
            txt += "\n"
    if deleted:
        txt += "\n"
        txt += " 👻**ᴀᴅᴍɪɴꜱ :**"
        txt += "\n"
        for adm in deleted:
            txt += f" • **None**"
            txt += "\n"
    try:
        await ok.edit(txt)
    except:
        await message.reply(txt)

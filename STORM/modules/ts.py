from pyrogram import Client, filters, enums
from gtts import gTTS
from config import SUDO_USERS

def convert(txt):
    tts = gTTS(txt)
    x = "Kex.mp3"
    tts.save(x)
    return x
  
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["tts"], ["."]))
async def texttospeech(client, message):
    reply = message.reply_to_message
    if not reply:
        if len(message.command) < 2:
            return await message.edit("ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ɢɪᴠᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ...")
    
    if reply:
        if not reply.text and not reply.caption:
            return await message.edit("ᴛᴇxᴛ ɴᴏᴛ ꜰᴏᴜɴᴅ... : (")
        txt = reply.text if reply.text else reply.caption
        path = convert(txt)
    else:
        txt = message.text.split(None, 1)[1]
        path = convert(txt)
    try:
        await message.delete()
    except:
        pass
    try:
        await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
        await message.reply_voice(path)
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    except:
        await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
        await message.reply_audio(path)
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)

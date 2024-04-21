from os import getenv
from random import choice
from pyrogram import filters, Client
from pyrogram.types import Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from config import SESSIONS, API_ID, API_HASH, OWNER_ID

SUDO_USERS = [OWNER_ID]

client = Client(SESSIONS, api_id=API_ID, api_hash=API_HASH)

call_py = PyTgCalls(client)
call_py2 = PyTgCalls(client)
call_py3 = PyTgCalls(client)
call_py4 = PyTgCalls(client)
call_py5 = PyTgCalls(client)

aud_list = [
    "./helpers/AUDIO1",
    "./helpers/AUDIO2",
    "./helpers/AUDIO3",
]

QUEUE = {}

def add_to_queue(chat_id, songname, link, ref, type, quality):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, link, ref, type, quality])
        return int(len(chat_queue) - 1)
    else:
        QUEUE[chat_id] = [[songname, link, ref, type, quality]]


@client.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], ["."]))
async def vcraid(_, e: Message):
    hero = await e.reply_text("» ᴜsᴀɢᴇ: .vcraid [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 
    if inp:
        bot = await hero.edit_text("» sᴛᴀʀᴛɪɴɢ ʀᴀɪᴅ")
        link = f"https://github.com/VARC9210{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"✨ ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n🔊 ᴀᴜᴅɪᴏ: `{songname}` \nᴘᴏsɪᴛɪᴏɴ:`𝟶{pos}`")
        else:
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"✨ ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n🔊 ᴀᴜᴅɪᴏ:`{songname}` \nᴘᴏsɪᴛɪᴏɴ: `ᴏɴɢᴏɪɴɢ`")

@client.on_message(filters.user(SUDO_USERS) & filters.command(["araid"], ["."]))
async def vcraid(_, e: Message):
    hero = await e.reply_text("» ᴜsᴀɢᴇ: .araid [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    replied = e.reply_to_message
    if inp:
        bot = await hero.edit_text("» sᴛᴀʀᴛɪɴɢ ʀᴀɪᴅ")
        link = replied.link
        dl = await replied.download()
        if replied.audio:
            if replied.audio.title:
                songname = replied.audio.title[:35] + "..."
            else:
                songname = replied.audio.file_name[:35] + "..."
        elif replied.voice:
            songname = "Voice Note"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"✨ ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n🔊 ᴀᴜᴅɪᴏ:`{songname}` \nᴘᴏsɪᴛɪᴏɴ:`𝟶{pos}`")
        else:
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl, HighQualityAudio()), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"✨ ʀᴀɪᴅɪɴɢ ɪɴ:** `{chat.title}` \n\n🔊 ᴀᴜᴅɪᴏ:`{songname}` \nᴘᴏsɪᴛɪᴏɴ: `ᴏɴɢᴏɪɴɢ`")


@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], ["."]))
async def ping(_, e: Message):
    hero = await e.reply_text("» ᴜsᴀɢᴇ: .raidend [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            await hero.edit_text("» ᴠᴄ ʀᴀɪᴅ ᴇɴᴅᴇᴅ")
        except Exception as ex:
            await hero.edit_text(f"» ᴇʀʀᴏʀ\n`{ex}`")
    else:
        await hero.edit_text("» ɴo ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ")


@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], ["."]))
async def ping(_, e: Message):
    hero = await e.reply_text("» ᴜsᴀɢᴇ: .raidpause [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.pause_stream(chat_id)
            if call_py2:
                await call_py2.pause_stream(chat_id)
            if call_py3:
                await call_py3.pause_stream(chat_id)
            if call_py4:
                await call_py4.pause_stream(chat_id)
            if call_py5:
                await call_py5.pause_stream(chat_id)
            await hero.edit_text(f"» ᴠᴄ ʀᴀɪᴅ ᴘᴀᴜsᴇᴅ ɪɴ:`{chat.title}`")
        except Exception as e:
            await hero.edit_text(f"» ᴇʀʀᴏʀ\n`{e}`")
    else:
        await hero.edit_text("» ɴᴏ ᴏɴɢᴏɪɴɢ ʀᴀɪᴅ")


@client.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], ["."]))
async def ping(_, e: Message):
    hero = await e.reply_text("» ᴜsᴀɢᴇ: .raidpause [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ᴄʜᴀᴛ_ɪᴅ] ")
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.resume_stream(chat_id)
            if call_py2:
                await call_py2.resume_stream(chat_id)
            if call_py3:
                await call_py3.resume_stream(chat_id)
            if call_py4:
                await call_py4.resume_stream(chat_id)
            if call_py5:
                await call_py5.resume_stream(chat_id)
            await hero.edit_text(f"» ᴠᴄ ʀᴀɪᴅ ʀᴇsᴜᴍᴇᴅ ɪɴ:`{chat.title}`")
        except Exception as e:
            await hero.edit_text(f"» ᴇʀʀᴏʀ\n`{e}`")
    else:
        await hero.edit_text("» ʀᴀɪᴅ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘᴀᴜsᴇᴅ")            

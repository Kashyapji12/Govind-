import asyncio
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
import lyricsgenius
SUDO_USER = SUDO_USERS
hl = "."
genius = lyricsgenius.Genius("jPnYlXn0YEF4xJLJJJ0V2fngWTmyK4c9scfIxFMpofO4-aKIWJ8t9f_11oCeZCLj")
async def search_lyrics(song_title, artist_name):
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            return song.lyrics
        else:
            return f"ʟʏʀɪᴄꜱ ꜰᴏʀ '{song_title}' ʙʏ {artist_name} ɴᴏᴛ ꜰᴏᴜɴᴅ..."
    except Exception as e:
        return f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {str(e)}"
        
@Client.on_message(filters.command(["lyrics", "l"], prefixes=hl) & filters.user(SUDO_USERS))
async def handle_lyrics_command(client: Client, message: Message):
    try:
        # Extract command arguments
        cmd = message.command
        song_title = cmd[1] if len(cmd) > 1 else ""
        artist_name = cmd[2] if len(cmd) > 2 else ""

        if not song_title:
            await message.edit("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ꜱᴏɴɢ ᴛɪᴛʟᴇ...")
            await asyncio.sleep(2)
            await message.delete()
            return

        if not artist_name:
            await message.edit("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇ ᴀʀᴛɪꜱᴛ ɴᴀᴍᴇ..")
            await asyncio.sleep(2)
            await message.delete()
            return

        # Retrieve and send lyrics
        await message.edit(f"ꜰᴇᴛᴄʜɪɴɢ ʟʏʀɪᴄꜱ ꜰᴏʀ '{song_title}' ʙʏ {artist_name}...")
        lyrics = await search_lyrics(song_title, artist_name)
        await message.edit(lyrics)

    except Exception as e:
        await message.edit("ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ʟʏʀɪᴄꜱ....")
        await asyncio.sleep(2)
        await message.delete()

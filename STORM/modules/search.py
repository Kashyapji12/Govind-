import asyncio
import os
import time
from urllib.request import urlretrieve
import requests as r
import wget
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from config import SUDO_USERS
from STORM.helper.basic import edit_or_reply

def get_text(message: Message) -> [None, str]:
    """ᴇxᴛʀᴀᴄᴛ ᴛᴇxᴛ ꜰʀᴏᴍ ᴄᴏᴍᴍᴀɴᴅꜱ"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["video", "v"], ["."]))
async def yt_vid(client: Client, message: Message):
    input_st = message.text
    input_str = input_st.split(" ", 1)[1]
    Man = await edit_or_reply(message, "ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    if not input_str:
        await Man.edit_text(
            "ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ɪɴᴘᴜᴛ...."
        )
        return
    await Man.edit_text(f"ꜱᴇᴀʀᴄʜɪɴɢ {input_str}")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await Man.edit_text(f"**ᴇʀʀᴏʀ :** `{str(e)}`")
        return
    time.time()
    file_path = f"{ytdl_data['id']}.mp4"
    capy = f"**ᴠɪᴅᴇᴏ ɴᴀᴍᴇ** `{vid_title}` \n**ʀᴇQᴜᴇꜱᴛᴇᴅ ꜰᴏʀ** `{input_str}` \n**ᴄʜᴀɴɴᴇʟ** `{uploade_r}` \n**ʟɪɴᴋ** `{url}`"
    await client.send_video(
        message.chat.id,
        video=open(file_path, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=downloaded_thumb,
        caption=capy,
        supports_streaming=True,
    )
    await Man.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)

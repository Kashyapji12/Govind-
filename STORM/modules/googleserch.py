from pyrogram import Client, filters
from config import SUDO_USERS
from bs4 import BeautifulSoup
from googlesearch import search
import requests
from pyrogram.types import Message

def googlesearch(query):
    co = 1
    returnquery = {}
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        url = str(j)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        metas = soup.find_all("meta")
        site_title = None
        for title in soup.find_all("title"):
            site_title = title.get_text()
        metadeta = [
            meta.attrs["content"]
            for meta in metas
            if "name" in meta.attrs and meta.attrs["name"] == "description"
        ]
        returnquery[co] = {"title": site_title, "metadata": metadeta, "url": j}
        co += 1
    return returnquery

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["gs", "google"], ["."]))
async def gs(client: Client, message: Message):
    Man = await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    msg_txt = message.text
    returnmsg = ""
    query = None
    if " " in msg_txt:
        query = msg_txt[msg_txt.index(" ") + 1:]
    else:
        await Man.edit("ɢɪᴠᴇ ᴀ Qᴜᴇʀʏ ᴛᴏ ꜱᴇᴀʀᴄʜ")
        return
    results = googlesearch(query)
    for i in range(1, 10):
        presentquery = results.get(i, {})
        presenttitle = presentquery.get("title", "")
        presentmeta = presentquery.get("metadata", [])
        presenturl = presentquery.get("url", "")
        if not presentmeta:
            presentmeta = ""
        else:
            presentmeta = presentmeta[0]
        returnmsg += f"[{str(presenttitle)}]({str(presenturl)})\n{str(presentmeta)}\n\n"
    await Man.edit(returnmsg)

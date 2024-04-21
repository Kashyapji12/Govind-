from pyrogram import Client, filters
import requests
from config import SUDO_USERS
NEWS_API = "140dd16908d54879b350d0c7378306a5"
api_key = NEWS_API

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["news"], ["."]))
def get_news(client, message):
    try:
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}")
        data = response.json()
        articles = data["articles"]
        news_headlines = "ᴛᴏᴘ ɴᴇᴡꜱ ʜᴇᴀᴅʟɪɴᴇꜱ:\n\n"
        for article in articles[:5]:
            title = article["title"]
            news_headlines += f"📰 {title}\n\n"
        message.edit(news_headlines)
    except Exception as e:
        message.edit(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: `{e}`")

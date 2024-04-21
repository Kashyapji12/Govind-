import random
from pyrogram import Client, filters
from config import SUDO_USERS

hl = "."

@Client.on_message(filters.command(["waifu"], prefixes=hl) & filters.user(SUDO_USERS))
async def waifu(client, message):
    args = message.text.split(" ")[1:]
    wdata = [
        "https://graph.org/file/1e4e2296c7edcb2ae96dd.jpg",
        "https://graph.org/file/9289d8e8a3981b91822b4.jpg",
        "https://graph.org/file/7e64cecf50e9165746a2b.jpg",
        "https://graph.org/file/ece7b21d443fa7051c0c4.jpg",
        "https://graph.org/file/29c158753f4743851bec5.jpg",
        "https://graph.org/file/e934043c60cff51ff705e.jpg",
        "https://graph.org/file/82d456479bbb104cf0129.jpg",
        "https://graph.org/file/66a29a591af76f770d4d3.jpg",
        "https://graph.org/file/94d7d78f8c82b2f529c74.jpg",
        "https://graph.org/file/117a00ef77ec5474dbff9.jpg",
        "https://graph.org/file/1d1cd38d07320446682a9.jpg",
        "https://graph.org/file/f9d43c3953dfe6a5a44d6.jpg",
        "https://graph.org/file/df0effb74bb0a86419235.jpg",
        "https://graph.org/file/c3c58ca40564fe4513471.jpg",
        "https://graph.org/file/07173cd0eb098769fd8cb.jpg",
        "https://graph.org/file/cc3e6ca9fa4bccfa99a32.jpg",
    ]
    waifu_url = random.choice(wdata)
    await message.reply_photo(waifu_url)

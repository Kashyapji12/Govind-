from pyrogram import Client, filters
import requests
from config import SUDO_USERS

WEATHER_API = "fadd97c7821d568d82f1cceaa06c7def"
api_key = WEATHER_API

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["weather"], ["."]))
async def get_weather_info(client, message):
    location = message.text.split(' ', 1)
    if len(location) > 1:
        city = location[1]
        weather_info = fetch_weather_info(city)
        await message.edit(weather_info)
    else:
        await message.edit("ᴘʟᴇᴀꜱᴇ ꜱᴘᴇᴄɪꜰʏ ᴛʜᴇ ᴄɪᴛʏ ꜰᴏʀ ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ...")

def fetch_weather_info(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_info = f"ᴡᴇᴀᴛʜᴇʀ ɪɴ {city}\n\n {description}, \n\n• ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ: {temperature}°C, \n\n• ʜᴜᴍɪᴅɪᴛʏ: {humidity}%, \n\n• ᴡɪɴᴅ ꜱᴘᴇᴇᴅ: {wind_speed} m/s"
            return weather_info
        else:
            return "ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰᴇᴛᴄʜ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰᴏʀ ᴛʜᴇ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴄɪᴛʏ"
    except Exception as e:
        return "ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ꜰᴇᴛᴄʜɪɴɢ ᴡᴇᴀᴛʜᴇʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ"

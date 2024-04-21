import asyncio
from pyrogram import filters, Client 
from pyrogram.types import Message
from config import SUDO_USERS
from STORM.helper.PyroHelpers import ReplyCheck
SUDO_USER = SUDO_USERS
@Client.on_message(
    filters.command(["m", "music"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def send_music(bot: Client, message: Message):
    try:
        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                    message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("ʙᴀʙᴇ ɢɪᴠᴇ ᴀ ꜱᴏɴɢ ɴᴀᴍᴇ")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await bot.get_inline_bot_results("deezermusicbot", song_name)

        try:
            saved = await bot.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
            )

            saved = await bot.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.id
                if message.reply_to_message
                else None
            )
            await bot.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=ReplyCheck(message),
            )

            await bot.delete_messages("me", saved.id)
        except TimeoutError:
            await message.edit("ᴛʜᴀᴛ ᴅɪᴅɴ'ᴛ ᴡᴏʀᴋ ᴏᴜᴛ")
            await asyncio.sleep(2)
        await message.delete()
    except Exception as e:
        print(e)
        await message.edit("ᴇʀʀᴏʀ : ꜰᴀɪʟᴇᴅ ᴛᴏ ꜰɪɴᴅ ꜱᴏɴɢ")
        await asyncio.sleep(2)
        await message.delete()

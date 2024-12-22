from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as c

app = Client(
    "x", 
    api_id=c.api_id, 
    api_hash=c.api_hash,
    bot_token=c.bot_token,
)

app.on_message(filters.command(["start"]))
def start_command(client, message):
    # Reply with a photo
    client.send_photo(
        chat_id=message.chat.id,
        photo="http://ibb.co/2Zy9qCb",
        caption="Alive Baby",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support", url="https://t.me/Anime_X_Isekai_Verse"),
                    InlineKeyboardButton("Channel", url="https://t.me/Anime_X_Isekai")
                ]
            ]
        )
    )

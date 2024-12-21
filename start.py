from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as c

app = Client(
    "x", 
    api_id=c.api_id, 
    api_hash=c.api_hash,
    bot_token=c.bot_token,
)

@app.on_message(filters.command("start"))
def start_command(client, message):
    photo = "http://ibb.co/sRMYPzM"
    caption = "Soon"
    group_button = InlineKeyboardButton("Group", url="https://t.me/Anime_X_Isekai_Verse")
    channel_button = InlineKeyboardButton("Channel", url="https://t.me/Anime_X_Isekai")
    reply_markup = InlineKeyboardMarkup([[group_button, channel_button]])
    
    message.reply_photo(photo, caption=caption, reply_markup=reply_markup)

app.run()

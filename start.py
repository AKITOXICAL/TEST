from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as c
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["referral_bot"]
referrals = db["referrals"]

app = Client(
    "x", 
    api_id=c.api_id, 
    api_hash=c.api_hash,
    bot_token=c.bot_token,
)

@app.on_message(filters.command("start"))
def start_command(client, message):
    photo = "http://ibb.co/sRMYPzM"
    caption = "Wassup Welcome"
    group_button = InlineKeyboardButton("Group", url="https://t.me/Anime_X_Isekai_Verse")
    channel_button = InlineKeyboardButton("Channel", url="https://t.me/Anime_X_Isekai")
    reply_markup = InlineKeyboardMarkup([[group_button, channel_button]])
    
    message.reply_photo(photo, caption=caption, reply_markup=reply_markup)

# Refer command
@app.on_message(filters.command("refer"))
def refer_command(bot, message):
    user_id = message.from_user.id
    referral_link = f"https://t.me/Anime_X_Isekai_Bot{user_id}"
    
    bot.send_photo(chat_id=message.chat.id, photo="computer.jpg", caption=f"Your Referral Link: {referral_link}")
    
    if user_id == message.reply_to_message.from_user.id:
        bot.reply_text(chat_id=message.chat.id, text="Clicking On Own Link Damn.")
    else:
        if referrals.find_one({"user_id": user_id}):
            bot.reply_text(chat_id=message.chat.id, text="You Already Started Bot.")
        else:
            referrals.insert_one({"user_id": user_id, "referrals": 0})

# Myrefer command
@app.on_message(filters.command("myrefer"))
def myrefer_command(bot, message):
    user_id = message.from_user.id
    user_refers = referrals.find_one({"user_id": user_id})["referrals"]
    
    bot.send_photo(chat_id=message.chat.id, photo="computer.jpg", caption=f"You Have Referred {user_refers}")

# Leaderboard command
@app.on_message(filters.command("leaderboard"))
def leaderboard_command(bot, message):
    top_users = referrals.find().sort("referrals", -1).limit(7)
    
    leaderboard_text = "Top 7 Users:\n"
    for index, user in enumerate(top_users, start=1):
        leaderboard_text += f"{index}. User ID: {user['user_id']} - Referrals: {user['referrals']}\n"
    
    bot.send_message(chat_id=message.chat.id, text=leaderboard_text)

app.run()


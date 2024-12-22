from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config as c
import pymongo
import string 

# Connect to MongoDB
client = MongoClient("mongodb+srv://publicDB:publicDBbyKira@public.twckcqf.mongodb.net/?retryWrites=true&w=majority")
db = client["x"]
collection = db["start"]

app = Client(
    "x", 
    api_id=c.api_id, 
    api_hash=c.api_hash,
    bot_token=c.bot_token,
)

# Generate random style
styles = ["Water", "Fire", "Wind", "Earth", "Thunder", "Darkness", "Light", "Nature"]
random_style = random.choice(styles)

# Start command handler
@app.on_message(filters.command(["start"]) & filter.private)
async def start_command(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    chat_id = message.chat.id
    
    # Check if user has already started the bot
    if collection.find_one({"user_id": user_id}):
        await message.reply_text("You have already started the bot. Keep the language in English.")
        return
    
    # Send initial message
    await client.send_photo(chat_id, "http://ibb.co/nrXh1wp", caption="𝗪𝗲𝗹𝗰𝗼𝗺𝗲,\n\n 𝗧𝗼 𝗔𝗻𝗶𝗺𝗲 𝗔𝗸𝗮 𝗜𝘀𝗲𝗸𝗮𝗶 𝗪𝗼𝗿𝗹𝗱.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Begin", callback_data="begin")]]))

# Callback query handler
@app.on_callback_query(filters.regex("^begin$"))
async def begin_callback(client, callback_query):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id
    
    # Send welcome message
    await callback_query.message.reply_text("𝐅𝐨𝐫 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐢𝐧𝐠 𝐀𝐬 𝐀𝐝𝐯𝐞𝐧𝐭𝐮𝐫𝐞𝐫 𝐢𝐧 𝐖𝐨𝐫𝐥𝐝, 𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐍𝐚𝐦𝐞.")
    
    # Save name in database
    @app.on_message(filters.text & filters.private)
    async def save_name(client, message):
        name = message.text
        
        # Check for invalid characters in name
        invalid_chars = [" ", ".", "@", "-", "/", "#"]
        if any(char in name for char in invalid_chars):
            await message.reply_text("You can only include _ in your name.")
            return
        
        # Save name in database
        collection.update_one({"user_id": user_id}, {"$set": {"name": name}})
        
        # Send message to enter username
        await message.reply_text("𝐅𝐨𝐫 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫𝐢𝐧𝐠 𝐀𝐬 𝐀𝐝𝐯𝐞𝐧𝐭𝐮𝐫𝐞𝐫 𝐢𝐧 𝐖𝐨𝐫𝐥𝐝, 𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞.")
    
    # Save username in database
    @app.on_message(filters.text & filters.private)
    async def save_username(client, message):
        username = message.text
        
        # Check for invalid characters in username
        invalid_chars = [" ", ".", "@", "-", "/", "#"]
        if any(char in username for char in invalid_chars):
            await message.reply_text("You can only include _ in your username.")
            return
            
        # Check for emojis in name
        if any(char in emoji.UNICODE_EMOJI for char in name):
            await message.reply_text("You can't use emojis in your name.")
            return
            
        # Check if username is already taken
        if collection.find_one({"username": username}):
            await message.reply_text("Username already taken.")
            return
        
        # Save username in database
        collection.update_one({"user_id": user_id}, {"$set": {"username": username}})
        
        # Send message to choose gender
        await message.reply_text("Choose Your Gender", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Boy", callback_data="boy"), InlineKeyboardButton("Girl", callback_data="girl")]]))
    
    # Save gender in database
    @app.on_callback_query(filters.regex("^boy$"))
    async def save_boy(client, callback_query):
        collection.update_one({"user_id": user_id}, {"$set": {"gender": "Boy"}})
        await callback_query.message.reply_text("Getting Your Own Style")
        await asyncio.sleep(3)
        collection.update_one({"user_id": user_id}, {"$set": {"style": random_style}})
        await callback_query.message.edit_text(f"Your Own Style is {random_style} Style")
        await callback_query.message.reply_photo("http://ibb.co/sRMYPzM", caption="Congrats for entering world", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Group", url="https://t.me/anime_x_isekai"), InlineKeyboardButton("Channel", url="https://t.me/anime_x_isekai")]]))
    
    @app.on_callback_query(filters.regex("^girl$"))
    async def save_girl(client, callback_query):
        collection.update_one({"user_id": user_id}, {"$set": {"gender": "Girl"}})
        await callback_query.message.reply_text("Getting Your Own Style")
        await asyncio.sleep(3)
        collection.update_one({"user_id": user_id}, {"$set": {"style": random_style}})
        await callback_query.message.edit_text(f"Your Own Style is {random_style} Style")
        await callback_query.message.reply_photo("http://ibb.co/sRMYPzM", caption="Congrats for entering world", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Group", url="https://t.me/anime_x_isekai"), InlineKeyboardButton("Channel", url="https://t.me/anime_x_isekai")]]))

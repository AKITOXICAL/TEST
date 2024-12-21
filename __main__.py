from Bot import app
import uvloop

print("Bot is successfully functioning started")


if __name__ == "__main__":
     #uvloop.install()
     app.run()
     with app:
        app.send_message(chat_id=-1002237183191,
           text=f"**Bot Has Been Started Launch Soon**")

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

TOKEN = os.getenv("8325082532:AAEyb69AnnGO8G7I_tkScGzdnIwH_SdVEeA")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋! Main Render pe hosted hoon 🔥")

bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: bot_app.run_polling()).start()
    app.run(host="0.0.0.0", port=10000)

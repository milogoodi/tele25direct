import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

TOKEN = os.getenv("7184786133:AAEmWFEbmeKU-RDWIhO7355ZPZQ91LpP1nU")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! لینک فایل تلگرام رو بفرست تا لینک مستقیم بدم 🎯")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.video or update.message.audio
    if file:
        file_obj = await file.get_file()
        direct_url = file_obj.file_path
        await update.message.reply_text(f"📎 لینک مستقیم: {direct_url}")
    else:
        await update.message.reply_text("فایل ارسال کن، نه متن!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL | filters.Video.ALL | filters.Audio.ALL, handle_file))

print("Bot is running...")
app.run_polling()

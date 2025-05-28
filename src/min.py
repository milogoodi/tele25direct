import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ لطفاً متغیر محیطی BOT_TOKEN را ست کنید.")

# پیام خوش‌آمدگویی با دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 👋\nفایل، صدا یا ویدیوتو بفرست تا برات پردازش کنم.")

# دریافت فایل (سند، ویدیو، صوت، عکس)
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    file_type = "فایل"

    if message.document:
        file_type = "سند"
    elif message.video:
        file_type = "ویدیو"
    elif message.audio:
        file_type = "فایل صوتی"
    elif message.photo:
        file_type = "عکس"

    await update.message.reply_text(f"{file_type} دریافت شد ✅")

# هندل ارور‌ها
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"⚠️ Error: {context.error}")
    if isinstance(update, Update) and update.message:
        await update.message.reply_text("❌ مشکلی پیش آمد. لطفاً دوباره تلاش کنید.")

# ساخت بات
app = ApplicationBuilder().token(TOKEN).build()

# افزودن هندلرها
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(
    filters.Document.ALL | filters.Audio.ALL | filters.Video.ALL | filters.PHOTO,
    handle_file
))

# ارور هندلر
app.add_error_handler(error_handler)

# اجرای بات
app.run_polling()

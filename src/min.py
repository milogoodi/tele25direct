import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

# توکن را از متغیر محیطی بخوان
TOKEN = os.getenv("BOT_TOKEN")

# هندلر برای فرمان /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات خوش آمدید. لطفاً فایل خود را ارسال کنید.")

# هندلر برای دریافت فایل‌ها
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("فایل شما با موفقیت دریافت شد ✅")

# هندلر برای خطاها
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"خطا: {context.error}")
    if isinstance(update, Update) and update.message:
        await update.message.reply_text("متأسفانه مشکلی پیش آمده است ❌")

# ساخت اپلیکیشن و اجرای بات
if name == "main":
    app = ApplicationBuilder().token(TOKEN).build()

    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.Document.ALL | filters.VIDEO | filters.AUDIO | filters.PHOTO,
        handle_file
    ))
    app.add_error_handler(error_handler)

    print("ربات در حال اجراست...")
    app.run_polling()

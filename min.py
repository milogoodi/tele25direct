import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# توکن رباتت رو اینجا بذار
TOKEN = "7917048534:AAEHc0ZnKRhNLnvUFIsTeOIxdh-5DJ4L0PQ"

logging.basicConfig(level=logging.INFO)

def start(update, context):
    update.message.reply_text("سلام! لینک تلگرام رو بفرست تا تبدیلش کنم به لینک مستقیم.")

def handle_message(update, context):
    text = update.message.text
    if "t.me" in text:
        update.message.reply_text("در حال حاضر این فقط یک نمونه‌ی تستی هست :)")
    else:
        update.message.reply_text("لینک تلگرام معتبر نیست.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()

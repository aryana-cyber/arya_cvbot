from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7968292523:AAE5p5Fm2hm56gpogQUv_ZKWJerJsjLfrVY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirim file txt-mu, nanti aku proses.")

async def handle_csv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document
    if document and document.file_name.endswith('.csv'):
        await update.message.reply_text("File CSV diterima! (proses selanjutnya di sini)")
    else:
        await update.message.reply_text("Mohon kirim file dengan format .csv")

if __name__ == "__main__":
    app = ApplicationBuilder().token("7968292523:AAE5p5Fm2hm56gpogQUv_ZKWJerJsjLfrVY").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_csv))

    print("Bot sedang berjalan...")
    app.run_polling()
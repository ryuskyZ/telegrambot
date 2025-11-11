from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#Token Lu 
Token = "8009698240:AAFZrpsS_1Ieg40OzlfnbcVc95hZH7HwqbI"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Halo @{update.effective_user.username} Muka Lu Kaya Memek")

app = ApplicationBuilder().token(Token).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
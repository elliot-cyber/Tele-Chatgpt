import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Masukkan API Key OpenAI
openai.api_key = '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'

# Fungsi untuk menangani pesan dari pengguna
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # Buat permintaan ke OpenAI ChatCompletion (gpt-3.5-turbo)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    # Kirim balasan dari OpenAI ke pengguna
    ai_response = response['choices'][0]['message']['content']
    await update.message.reply_text(ai_response)

# Fungsi untuk command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Halo! Saya bot yang terintegrasi dengan ChatGPT. Tanyakan apa saja!')

# Fungsi utama untuk menjalankan bot
def main():
    # Masukkan Token Bot Telegram
    application = ApplicationBuilder().token('7586237226:AAHPMFLJKX91meJaUdlhQKHvOz2n41PRZnI').build()

    # Command /start
    application.add_handler(CommandHandler('start', start))

    # Tangani semua pesan teks dari pengguna
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    application.run_polling()

# Panggil fungsi main
if __name__ == '__main__':
    main()

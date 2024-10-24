import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# API Key OpenAI yang baru
openai.api_key = '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'

# Fungsi untuk memproses pesan pengguna dan menjawab dari OpenAI
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    try:
        # Kirim pesan ke OpenAI API dengan model 'text-davinci-003'
        response = openai.Completion.create(
            engine="text-davinci-003",  # Gunakan engine yang tersedia
            prompt=user_message,
            max_tokens=150  # Atur sesuai kebutuhan
        )
        
        # Balas ke pengguna dengan hasil dari OpenAI
        await update.message.reply_text(response.choices[0].text.strip())
    
    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Kirimkan pertanyaanmu, dan aku akan mencoba menjawab menggunakan OpenAI.")

if __name__ == '__main__':
    # Token Bot Telegram
    application = Application.builder().token('7586237226:AAHPMFLJKX91meJaUdlhQKHvOz2n41PRZnI').build()

    # Daftar handler untuk menangani command /start dan pesan
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    application.run_polling()

import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# API Key OpenAI
openai.api_key = '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'

# Fungsi untuk memproses pesan pengguna dan menjawab dari OpenAI
async def handle_message(update: Update, context):
    user_message = update.message.text

    # Kirim pesan ke OpenAI API
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=user_message,
        max_tokens=150
    )
    
    # Balas ke pengguna dengan hasil dari OpenAI
    await update.message.reply_text(response.choices[0].text.strip())

# Fungsi untuk command /start
async def start(update: Update, context):
    await update.message.reply_text("Halo! Kirimkan pertanyaanmu, dan aku akan mencoba menjawab menggunakan OpenAI.")

if __name__ == '__main__':
    # Token Bot Telegram
    application = Application.builder().token('7586237226:AAHPMFLJKX91meJaUdlhQKHvOz2n41PRZnI').build()

    # Daftar handler untuk menangani command /start dan pesan
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    application.run_polling()

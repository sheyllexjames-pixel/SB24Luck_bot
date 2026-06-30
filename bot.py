import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Welcome Message in Khmer
WELCOME_TEXT = (
    "Welcome to the official SB24 - ស្ដេច​បក្សី.\n\n"
    "🐓 A trusted digital entertainment platform.\n"
    "👉 Click the button below to get started, Please select a service:"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons
    keyboard = [
        [InlineKeyboardButton("Chat to Admin", url="https://t.me/sb24lucky98999")],
        [InlineKeyboardButton("Deposit money (QR)", callback_data="deposit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "deposit":
        await query.edit_message_text(text="🏦 Please send a message to Admin to receive the QR Code.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    application.run_polling()

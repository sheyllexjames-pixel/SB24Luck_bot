import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Welcome Message in Khmer
WELCOME_TEXT = (
    "សូមស្វាគមន៍មកកាន់ SB24 - ស្ដេច​បក្សី (Official)\n\n"
    "🐓 ជាវេទិកាកម្សាន្តតាមអនឡាញដែលមានទំនុកចិត្តខ្ពស់។"
)

# Service Selection Message
SERVICE_TEXT = "សូមជ្រើសរើសសេវាកម្ម៖"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons layout based on your reference image
    keyboard = [
        [
            InlineKeyboardButton("📩 ឆាតទៅ Admin ↗️", url="https://t.me/sb24lucky98999"),
            InlineKeyboardButton("💰 ដាក់លុយ (QR)", callback_data="deposit")
        ],
        [
            InlineKeyboardButton("🎁 គណនីសាកល្បង", callback_data="trial")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Sends the messages exactly as requested
    await update.message.reply_text(WELCOME_TEXT)
    await update.message.reply_text(SERVICE_TEXT, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "deposit":
        await query.edit_message_text(text="🏦 សូមផ្ញើសារទៅកាន់ Admin ដើម្បីទទួលបានលេខកូដ QR។")
    elif query.data == "trial":
        await query.edit_message_text(text="🎁 នេះគឺជាគណនីសាកល្បងរបស់អ្នក។")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    application.run_polling()

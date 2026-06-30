import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Configuration
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Welcome Message in Khmer
WELCOME_TEXT = (
    "សូមស្វាគមន៍មកកាន់ SB24 - ស្ដេច​បក្សី (Official)\n\n"
    "🐓 វេទិកាកម្សាន្តតាមអនឡាញដែលមានទំនុកចិត្តខ្ពស់។\n"
    "👉 សូមចុចលើប៊ូតុងខាងក្រោមដើម្បីចាប់ផ្តើម។\n\n"
    "សូមជ្រើសរើសសេវាកម្ម៖"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Buttons layout
    keyboard = [
        [InlineKeyboardButton("ជជែកជាមួយ Admin", url="https://t.me/sb24lucky98999")],
        [InlineKeyboardButton("ដាក់ប្រាក់ (QR)", callback_data="deposit")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "deposit":
        # Khmer message when clicking the QR button
        await query.edit_message_text(text="🏦 សូមផ្ញើសារទៅកាន់ Admin ដើម្បីទទួលបានលេខកូដ QR។")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    application.run_polling()

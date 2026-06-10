from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8670701713:AAHjG_tJGbNlZcP3fs_cRCq4S8xbfOgUQtc"
ADMIN_ID = 6363945820

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 TikTok Services", callback_data="tiktok")],
        [InlineKeyboardButton("💰 Price List", callback_data="price")],
        [InlineKeyboardButton("💳 Payment Method", callback_data="payment")],
        [InlineKeyboardButton("📦 Order Status", callback_data="status")],
        [InlineKeyboardButton("🛒 Order Now", callback_data="order")],
        [InlineKeyboardButton("📞 Contact Admin", callback_data="contact")]
    ]

    await update.message.reply_text(
        "🔥 Welcome to SMM BOT 🔥",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tiktok":
        text = "📱 TikTok Services\n✔ Views\n✔ Likes\n✔ Followers"

    elif query.data == "price":
        text = """💰 Price List
10K Views = 60 RS
20K Views = 120 RS
50K Views = 290 RS"""

    elif query.data == "payment":
        text = """💳 Payment Method
EasyPaisa / JazzCash / UPaisa
☎️ 03211393691"""

    elif query.data == "status":
        text = "📦 Order In Progress ⏳"

    elif query.data == "order":
        text = "🛒 Send order: @username service quantity"

    elif query.data == "contact":
        text = "📞 Admin: @yourusername"

    else:
        text = "Invalid Option"

    await query.edit_message_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📥 NEW ORDER:\n{text}\nUser: @{update.message.from_user.username}"
    )

    await update.message.reply_text("✅ Order Received")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8670701713:AAHjG_tJGbNlZcP3fs_cRCq4S8xbfOgUQtc"
ADMIN_ID = 6363945820

# START MENU
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
        "🔥 Welcome to PRO SMM PANEL BOT 🔥",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "tiktok":
        text = """📱 TikTok Services

✔ Views
✔ Likes
✔ Followers

Send order:
@username service quantity"""

    elif query.data == "price":
        text = """💰 TikTok Rate List

👀 Views:
10K = 60 RS
20K = 120 RS
30K = 170 RS
50K = 290 RS

❤️ Likes:
200 = 50 RS
500 = 90 RS
1000 = 170 RS
2000 = 340 RS
3000 = 490 RS
4000 = 630 RS

🫂 Followers:
500 = 550 RS
1000 = 1200 RS
2000 = 2300 RS"""

    elif query.data == "payment":
        text = """💳 PAYMENT METHOD

✔ EasyPaisa
✔ UPaisa
✔ JazzCash

☎️ 03211393691

📌 Payment Screenshot Required ✅"""

    elif query.data == "status":
        text = """📦 Your Orders Placed ✅

📌 Order Status: In Progress

⏳ Complete Time: 31 minutes

🕐 Wait for completion..."""

    elif query.data == "order":
        text = """🛒 ORDER FORMAT

Send like:
@username + service + quantity

Example:
@user 10k views"""

    elif query.data == "contact":
        text = "📞 Admin Contact:\n@yourusername"

    else:
        text = "Invalid Option"

    await query.edit_message_text(text)

# ORDER SYSTEM (ADMIN NOTIFY)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📥 NEW ORDER RECEIVED:\n{text}\n\n👤 User: @{update.message.from_user.username}"
    )

    await update.message.reply_text("✅ Order Received Successfully")

# MAIN
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 SMM Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()

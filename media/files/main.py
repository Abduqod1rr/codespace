from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURATION ---
# Replace this with the token from BotFather
BOT_TOKEN = "8511551380:AAGTZambEDAXGTuKvWrhR4TBBlIAEEXk6hI"
# Replace this with the numeric ID you got from @userinfobot
ADMIN_ID = [7073429195 , 7656221348]


aa=("Assalomu alaykum!\n"
    "Men <b>@egalik_uzz</b> kanalining rasmiy botiman.\n\n"
    "Siz eʼlonni shu yerga yuborishingiz mumkin, men esa uni adminga yuboraman va e'loningiz kanalga chiqariladi.\n\n"
    "<b>Status:<b>\n"
    "•Ijaraga\n"
    "•Sotiladi\n\n"
    "<b>Kategoriyalar:</b>\n"
    "• Texnika, Asbob uskunalar\n"
    "• Qishloq xoʻjaligi, Koʻchmas mulk\n"
    "• Yer maydonlari, Transport, Kitoblar\n\n"
    "<b>E'lon uchun quyidagilarni yuboring:</b>\n"
    "📸 Rasm\n"
    "📌 Sarlavha va Tavsif\n"
    "📍 Hudud\n"
    "💰 Narx\n"
    "📞 Telefon raqam\n"
    "👤 Telegram username\n\n"
    "Savollar uchun: @egalik_admin")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! elonniningizni jonatishingiz mumkin")

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1. Get the user's info and message
    user = update.effective_user
    message_text = update.message.text
    
    # 2. Format the message so you know who sent it
    # Result looks like: "From John (ID: 123): Hello!"
    admin_text = f"[template] shunday holatda\nFrom: {user.first_name} (ID: {user.id})\n\n{message_text}"

    # 3. Send the message to the ADMIN_ID
    # We use context.bot.send_message to target a specific chat ID
    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_text)

    # 4. Reply to the USER to let them know it worked
    await update.message.reply_text("habaringiz adminlarga jonatildi")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handle the /start command
    app.add_handler(CommandHandler("start", start))

    # Handle all text messages that are NOT commands
    # This triggers the forward_to_admin function
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    print("Bot is running...")
    app.run_polling()
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL = "@jggddyhhh"
DEST_CHANNEL_ID = -1002639537406
OWNER_ID = 5818929933

async def forward_channel_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.username == SOURCE_CHANNEL.strip("@"):
        try:
            await context.bot.copy_message(
                chat_id=DEST_CHANNEL_ID,
                from_chat_id=SOURCE_CHANNEL,
                message_id=update.channel_post.message_id
            )
            print("✅ Message copied.")
        except Exception as e:
            print("❌ Error:", e)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    await context.bot.send_message(chat_id=user_id, text=f"👋 Your ID is {user_id}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ChatType.CHANNEL, forward_channel_messages))
app.add_handler(CommandHandler("start", start_command))

print("🤖 Bot is running...")
app.run_polling()
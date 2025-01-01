from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import os

# Replace with your bot token
BOT_TOKEN = "7945809583:AAFSkAn3Zh6x5AHcL6eLAYB8a91L63r0nVI"

# Start command
def start(update: Update, context: CallbackContext) -> None:
    welcome_message = """
Welcome to the Question Paper Bot! 📚  
You can download previous years' question papers for classes 9, 10, 11, and 12.

Use the following commands:
- /class9 - Get question papers for Class 9
- /class10 - Get question papers for Class 10
- /class11 - Get question papers for Class 11
- /class12 - Get question papers for Class 12
"""
    update.message.reply_text(welcome_message)

# Helper function to send papers
def send_papers(update: Update, context: CallbackContext, class_folder: str) -> None:
    folder_path = f"papers/{class_folder}"
    if not os.path.exists(folder_path):
        update.message.reply_text("No papers available for this class yet.")
        return

    files = os.listdir(folder_path)
    if not files:
        update.message.reply_text("No papers available for this class yet.")
        return

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "rb") as file:
            update.message.reply_document(document=file, filename=file_name)

# Handlers for each class
def class9(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "9")

def class10(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "10")

def class11(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "11")

def class12(update: Update, context: CallbackContext) -> None:
    send_papers(update, context, "12")

# Main function
def main() -> None:
    updater = Updater(BOT_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("class9", class9))
    dp.add_handler(CommandHandler("class10", class10))
    dp.add_handler(CommandHandler("class11", class11))
    dp.add_handler(CommandHandler("class12", class12))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

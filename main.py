import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
import handlers
from config import conf, generation_config, safety_settings
import logging
import os
import db

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    # Fetching railway env - DO NOT MODIFY! THIS IS THE ONLY FORMAT THAT WORKS: `os.environ['VARIABLE_NAME']`
    telegram_token = os.environ['BOT_TOKEN']
    gemini_api_key = os.environ['GEMINI_API_KEYS']
    logger.info("BOT_TOKEN and GEMINI_API_KEYS retrieved from environment.")
except KeyError as e:
    logger.critical(f"FATAL: Environment variable {e} is not set!")
    # Stop the application immediately if critical tokens/keys are missing
    raise ValueError(f"Critical environment variable {e} missing.") from e
# --- END ---

async def main():
    # --- Test DB Connection ---
    logger.info("Attempting database connection test...")
    if not db.test_db_connection():
        logger.critical("Database connection test failed. Exiting.")
        # Decide if you want to exit if DB fails. Probably yes for persistence.
        exit(1) # Uncomment this to make the bot stop if DB fails
        # logger.warning("Proceeding without database functionality (if applicable).") # Or just warn and continue
    else:
        logger.info("Database connection test successful.")
    # --- END ---

    # Init bot
    bot = AsyncTeleBot(telegram_token)
    await bot.delete_my_commands(scope=None, language_code=None)
    await bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("start", "Start"),
            telebot.types.BotCommand("gemini", "using gemini-2.0-flash-exp"),
            telebot.types.BotCommand("gemini_pro", "using gemini-1.5-pro"),
            telebot.types.BotCommand("draw", "draw picture"),
            telebot.types.BotCommand("edit", "edit photo"),
            telebot.types.BotCommand("clear", "Clear history (DB if implemented)"), # Prep help text
            telebot.types.BotCommand("switch","switch default model")
        ],
    )
    logger.info("Bot commands set.")

    # Init commands
    logger.info("Registering handlers...")
    bot.register_message_handler(handlers.start,                         commands=['start'],         pass_bot=True)
    bot.register_message_handler(handlers.gemini_stream_handler,         commands=['gemini'],        pass_bot=True)
    bot.register_message_handler(handlers.gemini_pro_stream_handler,     commands=['gemini_pro'],    pass_bot=True)
    bot.register_message_handler(handlers.draw_handler,                  commands=['draw'],          pass_bot=True)
    bot.register_message_handler(handlers.gemini_edit_handler,           commands=['edit'],          pass_bot=True)
    bot.register_message_handler(handlers.clear,                         commands=['clear'],         pass_bot=True)
    bot.register_message_handler(handlers.switch,                        commands=['switch'],        pass_bot=True)
    bot.register_message_handler(handlers.gemini_photo_handler,          content_types=["photo"],    pass_bot=True)
    bot.register_message_handler(
        handlers.gemini_private_handler,
        func=lambda message: message.chat.type == "private",
        content_types=['text'],
        pass_bot=True)
    logger.info("Handlers registered.")

    # Start bot
    logger.info("Starting Gemini_Telegram_Bot polling.")
    await bot.polling(none_stop=True)

if __name__ == '__main__':
    asyncio.run(main())
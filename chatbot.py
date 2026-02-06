import logging
import configparser
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# Import the ChatGPT class from your ChatGPT_HKBU.py file
from ChatGPT_HKBU import ChatGPT

# Global variable to hold the ChatGPT client instance
gpt = None

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle incoming text messages, send them to ChatGPT, 
    and reply with the generated response.
    """
    # Log the incoming update details for debugging
    logging.info("UPDATE: " + str(update))

    # Send a temporary 'Thinking...' message to improve user experience
    loading_message = await update.message.reply_text('Thinking...')

    try:
        # Get the user's message text
        user_text = update.message.text
        
        # Send the message to the ChatGPT client and get the response
        # The gpt object is initialized in the main() function
        response = gpt.submit(user_text)

        # Edit the temporary 'Thinking...' message with the actual AI response
        await loading_message.edit_text(response)
        
    except Exception as e:
        # Log any errors that occur during the API call
        logging.error(f"Error in callback: {e}")
        await loading_message.edit_text("Sorry, I encountered an error while processing your request.")

def main():
    """
    Main entry point for the Telegram chatbot.
    """
    # Configure logging to see initialization and error messages in the terminal
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    # Load configuration from the config.ini file
    logging.info('INIT: Loading configuration...')
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Initialize the ChatGPT client object using the global variable
    global gpt
    gpt = ChatGPT(config)

    # Initialize the Telegram Application with your bot's access token
    logging.info('INIT: Connecting to the Telegram bot...')
    token = config['TELEGRAM']['ACCESS_TOKEN']
    app = ApplicationBuilder().token(token).build()

    # Register a MessageHandler to process all text messages that are not commands
    logging.info('INIT: Registering the message handler...')
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callback))

    # Start the bot and keep it running
    logging.info('INIT: Initialization done! Bot is now polling...')
    app.run_polling()

if __name__ == '__main__':
    main()
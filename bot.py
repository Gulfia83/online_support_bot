import logging

from environs import Env
from google.cloud import api_keys_v2
from google.cloud import dialogflow
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

env = Env()
env.read_env()


def create_api_key(project_id):
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = "My first API key"

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    response = client.create_key(request=request).result()
    return response


def detect_intent_text(project_id, session_id, message_to_dialogflow, language_code='ru'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=message_to_dialogflow, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    serialized_answer = {
        'intention': response.query_result.intent.display_name,
        'confidence': response.query_result.intent_detection_confidence,
        'answer': response.query_result.fulfillment_text
    }
    return serialized_answer


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo_dialogflow(update, context):
    message_to_dialogflow = update.message.text
    session_id = update.effective_chat.id
    serialized_answer = detect_intent_text(project_id, session_id, message_to_dialogflow)
    update.message.reply_text(serialized_answer['answer'])



if __name__ == '__main__':
    tg_bot_token = env.str('TG_BOT_TOKEN')
    project_id = env.str('PROJECT_ID')
    token = create_api_key(project_id)
    print("Successfully created an API key")

    updater = Updater(tg_bot_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo_dialogflow))

    updater.start_polling()
    updater.idle()
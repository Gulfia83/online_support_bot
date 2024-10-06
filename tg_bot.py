import logging

from environs import Env
from telegram import Update, ForceReply, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
      CallbackContext

from dialogflow_scripts import detect_intent_text


logger = logging.getLogger(__name__)


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def handle_dialogflow(update, context):
    message_to_dialogflow = update.message.text
    session_id = update.effective_chat.tg-id
    serialized_answer, _ = detect_intent_text(
        project_id,
        session_id,
        message_to_dialogflow
        )
    update.message.reply_text(serialized_answer)


if __name__ == '__main__':   
    env = Env()
    env.read_env()
    tg_bot_token = env.str('TG_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')

    bot = Bot(tg_bot_token)
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(bot, tg_chat_id))
    logger.info('Бот запущен')

    try:
        updater = Updater(tg_bot_token)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,
                                              handle_dialogflow))

        updater.start_polling()
        updater.idle()
    except Exception as exception:
        logging.exception(exception)

import random
import logging

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env
from telegram import Bot

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


def handle_dialogflow(event, vk_api, project_id):
    reply_text, is_fallback = detect_intent_text(
        project_id,
        f'vk-{event.user_id}',
        event.text
    )

    if not is_fallback:
        vk_api.messages.send(
            user_id=f'vk-{event.user_id}',
            message=reply_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    env = Env()
    env.read_env()

    vk_api_key = env.str('VK_API_KEY')
    tg_bot_token = env.str('TG_BOT_TOKEN')
    tg_chat_id = env.str('TG_CHAT_ID')
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')
    bot = Bot(tg_bot_token)

    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s")
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(bot, tg_chat_id))
    logger.info('VK бот запущен')

    try:
        vk_session = vk.VkApi(token=vk_api_key)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                handle_dialogflow(event, vk_api, project_id)
    except Exception as exception:
        logger.exception(exception)

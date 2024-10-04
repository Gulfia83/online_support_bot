import json
import logging

from environs import Env

from dialogflow_scripts import create_intent


logger = logging.getLogger(__name__)


def load_typical_phrases(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        questions_json = file.read()
    return json.loads(questions_json)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    project_id = env.str('PROJECT_ID')

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
        )
    
    typical_phrases = load_typical_phrases('questions.json')
    for phrase in typical_phrases.keys():
        display_name = phrase
        response = create_intent(
            project_id=project_id,
            display_name=display_name,
            training_phrases_parts=typical_phrases[display_name]['questions'],
            message_texts=typical_phrases[display_name]['answer']
        )
        logging.info("Intent created: {}".format(response))

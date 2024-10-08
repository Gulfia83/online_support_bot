# Telegram и VK боты для онлайн-издательства "Игра глаголов"
Чат-боты для помощи службе поддержки. Они обучены отвечать на стандартные вопросы пользователей с помощью сервиса DialogFlow от Google.

## Ссылки на ботов
- [Телеграм бот ](https://t.me/echo_exam_bot)
- [VK бот ](https://vk.com/club227606236)

## Примеры работы ботов

https://github.com/user-attachments/assets/9788b2b8-daf1-4cb1-abb6-522af87154af

https://github.com/user-attachments/assets/54f35e40-6834-449e-8155-a2b675cd0a28

## Установка
1. Установите Python 3.10.12 и создайте виртуальное окружение, активируйте его:
    
2. Установите необходимые зависимости с помощью `pip`:
    ```sh
    pip install -r requirements.txt
    ```
3. Создайте проект в Google Cloud.
    [создать проект ](https://console.cloud.google.com/projectselector2/home/)
4. Создайте агент в DialogFlow. 
    [создать агента](https://dialogflow.cloud.google.com/#/agent/)
Проследите, чтобы id вашего проекта в Google и id агента совпадали.
5. Получите API-ключ Dialogflow. Для этого запустите скрипт:
    ```sh
    python3 create_api_key.py
    ```
    Информация для авторизации будет сохранена в файл `project_api_key.txt`
6. Добавьте `Intents` в вашего агента DialogFlow. Это можно сделать как вручную (см. документацию), так и с помощью скрипта:
    ```sh
    python3 learning_script.py.py
    ```
    Информацию для обучения поместите в файл `questions.json`, который имеет следующую структуру:
    ```json
    {
        "Устройство на работу": {
            "questions": [
                "Как устроиться к вам на работу?",
                "Как устроиться к вам?",
                "Как работать у вас?",
                "Хочу работать у вас",
                "Возможно-ли устроиться к вам?",
                "Можно-ли мне поработать у вас?",
                "Хочу работать редактором у вас"
            ],
            "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
        }
    }
    ```
7. Получите токен для вашего телеграм-бота и для вашего сообщества в ВК.
8. Создайте файл `.env` и поместите в него следующие переменные окружения:
    ```env
    TG_BOT_TOKEN='токен телеграм бота'
    VK_API_KEY='api-ключ вашего сообщества в ВК'
    TG_CHAT_ID='id чата в телеграм для отправки логов'
    GOOGLE_CLOUD_PROJECT_ID='id проекта в Google Cloud'
    GOOGLE_APPLICATION_CREDENTIALS='путь к файлу с информацией об авторизации в Google Cloud'
    ```
## Запуск
1. Запустите телеграм бота:
    ```sh
    python3 tg_bot.py
    ```
2. Запустите ВК бота:
    ```sh
    python3 vk_bot.py
    ```
***
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](dvmn.org).

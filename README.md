# Telegram and VK bots for the online publishing house "Game of Verbs"
Chat bots to help the support service. They are trained to answer standard user questions using the DialogFlow service from Google.

## Links to bots
- [Telegram bot](https://t.me/echo_exam_bot)
- [VK bot](https://vk.com/club227606236)

## Examples of bots

## Installation
1. Install Python 3.10.12 and create a virtual environment, activate it:

2. Install the necessary dependencies using `pip`:
```sh
pip install -r requirements.txt
```
3. Create a project in Google Cloud.
[create project ](https://console.cloud.google.com/projectselector2/home/)
4. Create an agent in DialogFlow.
[create agent](https://dialogflow.cloud.google.com/#/agent/)
Make sure your Google project id and agent id match.
5. Get Dialogflow API key. To do this, run the script:
```sh
python3 create_api_key.py
```
Authentication information will be saved to the file `project_api_key.txt`
6. Add `Intents` to your DialogFlow agent. This can be done either manually (see the documentation) or using a script:
```sh
python3 learning_script.py.py
```
Place the training information in the `questions.json` file, which has the following structure:
```json
{
"Getting a job": {
"questions": [
"How can I get a job with you?",
"How can I get a job with you?",
"How can I work for you?",
"I want to work for you",
"Is it possible to get a job with you?",
"Can I work for you?",
"I want to work as an editor for you"
],
"answer": "If you want to get a job with us, write a mini-essay about yourself to game-of-verbs@gmail.com and attach your portfolio."
}
}
```
7. Get a token for your telegram bot and for your VK community.
8. Create a `.env` file and put the following environment variables in it:
```env
TG_BOT_TOKEN='telegram bot token'
VK_API_KEY='api key of your VK community'
TG_CHAT_ID='telegram chat id for sending logs'
GOOGLE_CLOUD_PROJECT_ID='Google Cloud project id'
GOOGLE_APPLICATION_CREDENTIALS='path to the file with Google Cloud authorization information'
```
## Launch
1. Launch the telegram bot:
```sh
python3 tg_bot.py
```
2. Launch the VK bot:
```sh
python3 vk_bot.py
```
***
The code is written for educational purposes on the online course for web developers [Devman](dvmn.org).
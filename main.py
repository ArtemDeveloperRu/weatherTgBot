import requests
import json
import telebot
from tok import tgtoken

bot = telebot.TeleBot(tgtoken)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, я рад тебе видеть! Напеши город")

@bot.message_handler(content_types=['text'])
def send_text(message):
    city = message.text.strip().lower()
    API = '9d5ce9cedfe586c9dc707f88e1350ed7'
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)  # Use json.loads instead of json.load
        temp = data["main"]["temp"]
        
        bot.reply_to(message, f"Сейчас погода: {temp}℃")
        
        image ='img/sunny.png' if temp > 5.0 else 'img/sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.send_message(message.chat.id, f"Город {city} не найден")

# Run the bot
bot.polling(none_stop=True)
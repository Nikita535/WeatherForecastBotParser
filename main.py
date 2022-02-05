import telebot
import requests
from bs4 import BeautifulSoup as BS
bot = telebot.TeleBot("Ваш токен")
base_url = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0'
HEADERS = {

   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}




@bot.message_handler(commands=['start'])
def start(message):
    def parser(url):
        session = requests.Session()
        response = session.get(url, headers=HEADERS)
        soup = BS(response.content, 'html.parser')
        items = soup.find_all('div', class_='UQt4rd')

        for weather in items:
            temp = weather.find('span', class_='wob_t TVtOme').text
            prep = weather.find('span', id='wob_pp').text
            hum = weather.find('span', id='wob_hm').text
            speed = weather.find('span', id='wob_ws').text
            message_text=('Температура: '+temp+'\n'
                            +'Вероятность осадков: '+prep+'\n'
                            +'Влажность: '+hum+'\n'
                            +'Ветер: '+speed
                          )

            bot.send_message(message.chat.id, message_text)

    parser(url=base_url)


bot.polling()

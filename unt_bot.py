from pyowm import *
from telegram.ext import *

updater = Updater(token="654158410:AAHgwNVHKOyNdzMV21lYldGOfMXrEMp3zOU")
dispatcher = updater.dispatcher

def startCommnad(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, я бот, который узнает погоду в твоем городе, напиши свой город")

def textMessage(bot, update):
    print(update.message.user_id)
    owm = OWM("94bdcbfba3773e1fb2b262bcd957c66a")
    try:
        city_location = update.message.text
        observation = owm.weather_at_place(city_location)

        w = observation.get_weather()

        temperature = w.get_temperature('celsius')['temp']
        bot.send_message(chat_id=update.message.chat_id, text="В городе " + str(city_location) + " температура " + str(temperature) + " по Цельсию")

    except:
        bot.send_message(chat_id=update.message.chat_id, text="Вы ввели не верный город")
start_command_handler = CommandHandler("start", startCommnad)
text_message = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message)
updater.start_polling(clean=True)
updater.idle()
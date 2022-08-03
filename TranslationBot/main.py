import telebot
from constants import API_KEY
import google_trans_new as gtn


translator = gtn.google_translator()
bot = telebot.TeleBot(API_KEY)


def translate_init(message):
    try:
        msg = message.text
        if len(msg) > 0:
            return True
    except:
        return False


@bot.message_handler(func=translate_init)
def translate(message):
    result = translator.translate(text=message.text, lang_tgt='en')
    msg = message.forward_from.first_name + '\n\n' + result.text
    bot.reply_to(message, msg)


bot.polling()

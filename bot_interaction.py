import telebot
from Init.init import config as cfg
from Database.core import LocalSession
from bot_core import BotCore

bot = telebot.TeleBot(cfg["Bot"]["Token"])
session = LocalSession()
bot_core = BotCore(session)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Hello my dude, it is wednesday bot")
    bot_core.add_new_user(message.from_user.id)


bot.infinity_polling()

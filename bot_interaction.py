import telebot
from Init.init import config as cfg
from Database.core import Session
from bot_core import BotCore, session

bot = telebot.TeleBot(cfg["Bot"]["Token"])
bot_core = BotCore(session)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, "Hello my dude, it is wednesday bot")
    bot_core.add_new_user(message.from_user.id)


@bot.message_handler(commands=['keyboard'])
def give_keyboard_to_user(message):
    keyboard_markup = bot_core.get_keyboard_for_user(message.from_user.id)
    bot.send_message(message.chat.id, "Choose what you want, dude", reply_markup=keyboard_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "kb_dude":
        bot.answer_callback_query(call.id, "DUUUDE!!!")
        bot.edit_message_reply_markup(call.message.chat.id, call.message.id)
    elif call.data == "kb_wednesday":
        bot.answer_callback_query(call.id, "It's wednesday my dude")


@bot.message_handler(commands=["help"])
def helping(message):
    keyboard_markup = bot_core.get_keyboard_for_user(message.from_user.id)
    bot.send_message(message.chat.id, text="", reply_markup=keyboard_markup)


bot.infinity_polling()

import telebot
from django.core.management.base import BaseCommand
from telebot.types import Message

bot = telebot.TeleBot("6658113257:AAE2bGCchqzPqV-sY38x1tcbnMgW3scLjTs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message: Message):
    bot.reply_to(message, message.text)

class Command(BaseCommand):
    help = "Run the bot"
    
    def handle(self, *args, **options):
        bot.polling()
from telebot import TeleBot
from telebot.types import Message

BOT_TOKEN = '7052999075:AAE5goCPc759Y73GOk7eJIp8DyrJop8GpYs'
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, chat_id)
    bot.send_message(chat_id, f"<i>Assalomu alaykum</i>,  {message.from_user.full_name}\n"
                              f"Foydalanuvchi nomingiz: @{message.from_user.username}", parse_mode="HTML")

@bot.message_handler(commands=['help'])
def help(message: Message):
    bot.send_message(message.chat.id, """
    Botdagi buyruq(comanda)lar:
        /start - Botni ishga tushurish.
        /help  - Botdan foydalanish haqida ma'lumot.
        /GetMyData - Foydalanuvchi ma'lumotlarini olish.
    """)

@bot.message_handler(commands=['GetMyData'])
def mydata(message: Message):
    bot.send_message(message.chat.id, f"<b>ID: </b>{message.from_user.id}\n"
                                      f"First name: {message.from_user.first_name if message.from_user.first_name else '-'}\n"
                                      f"Last name: {message.from_user.last_name if message.from_user.last_name else '-'}\n"
                                      f"Username: {message.from_user.username if message.from_user.username else '-'}\n"
                                      f"User is bot: {"User is not bot!" if not message.from_user.is_bot else "User is Bot!"}", parse_mode="HTML")

@bot.message_handler(content_types=['text', 'photo', 'video', 'animation'])
def send_text_group(message: Message):
    bot.copy_message(-1002136578167, message.chat.id, message.message_id)

bot.polling()
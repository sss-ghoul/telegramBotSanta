import telebot
from telebot import types
import datetime
import sqlite3

con = sqlite3.connect("student.db")
cursor = con.cursor()


bot = telebot.TeleBot('6503197973:AAHdYlwaDw4NshV8wjhS_5QUwJ2ICL8gQWE')

user = {}
new_user = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if user_id not in user:
        user[user_id] = {}
    bot.send_message(user_id, "Привет! Я бот для Тайного Санты. Давай начнем!")

    # кнопка "Начать"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item = types.KeyboardButton("Начать")
    markup.add(item)

    bot.send_message(user_id, "Для участия в Тайном Санте, нажми 'Начать'.", reply_markup=markup)

# Обработчик "Начать"
@bot.message_handler(func=lambda message: message.text == "Начать")
def register_user(message):
    user_id = message.chat.id

    bot.send_message(user_id, "Пожалуйста, введи свои данные.")
    bot.send_message(user_id, "1. Ваше ФИО:")
    bot.register_next_step_handler(message, get_fullname)

def get_fullname(message):
    user_id = message.chat.id
    user[user_id]["fullname"] = message.text

    bot.send_message(user_id, "2. Факультет:")
    bot.register_next_step_handler(message, get_faculty)

def get_faculty(message):
    user_id = message.chat.id
    user[user_id]["faculty"] = message.text

    bot.send_message(user_id, "3. Группа:")
    bot.register_next_step_handler(message, get_group)

def get_group(message):
    user_id = message.chat.id
    user[user_id]["group"] = message.text

    bot.send_message(user_id, "4. Список желаний:")
    bot.register_next_step_handler(message, get_wishlist)

def get_wishlist(message):
    user_id = message.chat.id
    user[user_id]["wishlist"] = message.text

    bot.send_message(user_id, "Спасибо за регистрацию!")

    # можно установить дату
    draw_date = datetime.datetime.now() + datetime.timedelta(days=14)
    bot.send_message(user_id, f"Жеребьевка состоится {draw_date.strftime('%Y-%m-%d %H:%M')}.")
    bot.send_message(user_id, f"Количество участников {len(user)}.")
    print(user)


# Запускаем бота
bot.polling()

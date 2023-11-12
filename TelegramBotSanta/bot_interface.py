import telebot
from telebot import types
import datetime
import sqlite3

con = sqlite3.connect("student.db", check_same_thread=False)
cursor = con.cursor()

bot = telebot.TeleBot('6503197973:AAHdYlwaDw4NshV8wjhS_5QUwJ2ICL8gQWE')

user = {}


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if user_id not in user:
        user[user_id] = {}
    bot.send_message(user_id, "Привет! Я бот для Тайного Санты. Давай начнем!")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item = types.KeyboardButton("Начать")
    markup.add(item)

    bot.send_message(user_id, "Для участия в Тайном Санте, нажми 'Начать'.", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Начать")
def register_user(message):
    user_id = message.chat.id

    bot.send_message(user_id, "Пожалуйста, введи свои данные.")
    bot.send_message(user_id, "1. Ваше ФИО:")
    bot.register_next_step_handler(message, get_fullname)


def get_fullname(message):
    user_id = message.chat.id
    user[user_id]["fullname"] = message.text

    bot.send_message(user_id, "2. Группа:")
    bot.register_next_step_handler(message, get_group)


def get_group(message):
    user_id = message.chat.id
    user[user_id]["group"] = message.text

    bot.send_message(user_id, "3. Факультет:")
    bot.register_next_step_handler(message, get_faculty)


def get_faculty(message):
    user_id = message.chat.id
    user[user_id]["faculty"] = message.text

    bot.send_message(user_id, "4. Список желаний:")
    bot.register_next_step_handler(message, get_wishlist)


def get_wishlist(message):
    user_id = message.chat.id
    user[user_id]["wishlist"] = message.text

    bot.send_message(user_id, "Спасибо за регистрацию! Ожидайте результатов.")

    cursor.execute('INSERT INTO Student (Name, study_group, Faculty, Wishes, user_id) VALUES (?, ?, ?, ?, ?)',
                   (user[user_id]["fullname"], user[user_id]["group"], user[user_id]["faculty"],
                    user[user_id]["wishlist"], user_id))
    con.commit()


def send_message(users):
    for i in range(0, len(users)):
        if i == len(users) - 1:
            cursor.execute('SELECT Name, study_group, Faculty, Wishes FROM Student WHERE user_id=?', (users[0],))
            kid = cursor.fetchall()
        else:
            cursor.execute('SELECT Name, study_group, Faculty, Wishes FROM Student WHERE user_id=?', (users[i + 1],))
            kid = cursor.fetchall()

        cursor.execute('SELECT Name FROM Student WHERE user_id=?', (users[i],))
        santa = cursor.fetchall()
        bot.send_message(users[i],
                         f'Привет, {santa[0][0]}! Ваш подопечный - {kid[0][0]} {kid[0][1]} {kid[0][2]} факультет.\nЕго список желаний:\n{kid[0][3]}')


@bot.message_handler(commands=['send_message'])
def send_message_command(message):
    users = []
    cursor.execute('SELECT user_id FROM Student')
    users_id = cursor.fetchall()
    for i in range(0, len(users_id)):
        users.append(users_id[i][0])
    send_message(users)
    users.clear()
    for i in range(0, len(users_id)):
        print(users_id[i])

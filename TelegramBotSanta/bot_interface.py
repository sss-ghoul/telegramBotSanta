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

    bot.send_message(user_id, "Спасибо за регистрацию!")

    cursor.execute('INSERT INTO Student (Name, study_group, Faculty, Wishes) VALUES (?, ?, ?, ?)',
                   (user[user_id]["fullname"], user[user_id]["group"], user[user_id]["faculty"],
                    user[user_id]["wishlist"]))
    con.commit()
    bot.register_next_step_handler(message, result)


def result(message):
    print(1)
    user_id = message.chat.id
    bot.send_message(user_id, f'Готово')

    # cursor.execute('SELECT * FROM Student')
    # students = cursor.fetchall()
    # for i in range(0, len(students)):
    #     if i == len(students)-1:
    #         cursor.execute('INSERT INTO Gift (Santa, Kid) VALUES (?, ?)',
    #                        (students[i][1], students[0][1]))
    #     else:
    #         cursor.execute('INSERT INTO Gift (Santa, Kid) VALUES (?, ?)',
    #                        (students[i][1], students[i+1][1]))
    #
    #
    # cursor.execute('SELECT Santa, Kid FROM Gift WHERE Santa =?', (user[user_id]["fullname"],))
    # student = cursor.fetchall()
    #
    # cursor.execute('SELECT Wishes FROM Student WHERE Name=?', (user[user_id]["fullname"]))
    # wish = cursor.fetchall()
    #
    # bot.send_message(user_id, f'Привет, {student[0][0]}, вы дарите подарок {student[0][1]}. '
    #       f'\nЕго список желаний: {wish[0][0]}')


# Запускаем бота


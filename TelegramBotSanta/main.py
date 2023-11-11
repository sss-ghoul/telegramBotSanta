import sqlite3
import bot_interface

con = sqlite3.connect('student.db')
cursor = con.cursor()

# def result():
#     print(1)
#
#     cursor.execute('SELECT Santa, Kid FROM Gift WHERE Santa =?', (bot_interface.user[user_id]["fullname"],))
#     student = cursor.fetchall()
#
#     cursor.execute('SELECT Wishes FROM Student WHERE Name =?', (name,))
#     wish = cursor.fetchall()


# cursor.execute('DELETE FROM Student WHERE id = ?', (1,))


s = input("Вывести результат? Да/Нет\n")

bot_interface.bot.polling()

if s == 'lf' or s == 'LF' or s == 'Lf' or s == 'да' or s == 'ДА' or s == 'Да':
    bot_interface.result()

con.commit()
con.close()

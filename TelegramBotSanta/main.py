import sqlite3
con = sqlite3.connect("student.db")
cursor = con.cursor()



# while True:
#     Name = input('Введите имя: ')
#     study_group = input('Введите группу: ')
#     Faculty = input('Введите факультет: ')
#     Wishes = input('Введите список желаний: ')
#
#     cursor.execute('INSERT INTO Student (Name, study_group, Faculty, Wishes) VALUES (?, ?, ?, ?)',
#                    (Name, study_group, Faculty, Wishes))
#
#     flag = input("Добавить еще одного? Да/Нет")
#     if flag != 'Да':
#         break



Name = input('Введите имя: ')
study_group = input('Введите группу: ')
Faculty = input('Введите факультет: ')
Wishes = input('Введите список желаний: ')

cursor.execute('INSERT INTO Student (Name, study_group, Faculty, Wishes) VALUES (?, ?, ?, ?)',
              (Name, study_group, Faculty, Wishes))

print()


con.commit()
con.close()

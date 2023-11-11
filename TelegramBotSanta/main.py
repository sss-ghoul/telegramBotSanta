import sqlite3

con = sqlite3.connect('student.db')
cursor = con.cursor()


def result():
    name = input("Введите имя ")

    cursor.execute('SELECT Santa, Kid FROM Gift WHERE Santa =?', (name,))
    student = cursor.fetchall()

    cursor.execute('SELECT Wishes FROM Student WHERE Name =?', (name,))
    wish = cursor.fetchall()

    print(f'Привет, {student[0][0]}, вы дарите подарок {student[0][1]}. '
          f'\nЕго список желаний: {wish[0][0]}')

    # cursor.execute('SELECT * FROM Student')
    # students = cursor.fetchall()
    # for i in range(0, len(students)):
    #     if i == len(students)-1:
    #         cursor.execute('INSERT INTO Gift (Santa, Kid) VALUES (?, ?)',
    #                     (students[i][1], students[0][1]))
    #     else:
    #         cursor.execute('INSERT INTO Gift (Santa, Kid) VALUES (?, ?)',
    #                    (students[i][1], students[i+1][1]))


str = input("Зарегистрироваться? ")
if str == 'Да':
    Name = input('Введите имя: ')
    study_group = input('Введите группу: ')
    Faculty = input('Введите факультет: ')
    Wishes = input('Введите список желаний: ')

    cursor.execute('INSERT INTO Student (Name, study_group, Faculty, Wishes) VALUES (?, ?, ?, ?)',
                   (Name, study_group, Faculty, Wishes))

x = input("Вывести результат? ")
if x == 'да' or x == 'Да':
    result()

con.commit()
con.close()

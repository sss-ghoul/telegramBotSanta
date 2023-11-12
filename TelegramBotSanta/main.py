import sqlite3
import bot_interface

con = sqlite3.connect('student.db')
cursor = con.cursor()

# cursor.execute('DELETE FROM Student WHERE id = ?', (1,))


bot_interface.bot.polling()

con.commit()
con.close()

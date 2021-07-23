import sqlite3

conn = sqlite3.connect("roster.sqlite")
cur = conn.cursor()

cur.execute('''
    SELECT User.name AS user_name, Course.title AS course_title, Member.role
    FROM User JOIN Course JOIN Member
    ON Member.user_id = User.id AND Member.course_id = Course.id
    ORDER BY Course.title, Member.role DESC, User.name;''')

for i in cur:
    print(i)

import json
import sqlite3
from sqlite3.dbapi2 import Cursor

# makes a connection to the database
conn = sqlite3.connect("roster.sqlite")
cur = conn.cursor()

cur.executescript('''CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT    
);

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id)
    );
''')

# makes aure that an appropriate file name is entered
fname = input("Enter filename: ")
if len(fname) < 1:
    fname = 'roster_data.json'

fhand = open(fname,)

data = json.load(fhand)
for i in data:
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (i[0],))
    cur.execute('''SELECT id FROM User WHERE name = ?''', (i[0],))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (i[1],))
    cur.execute('''SELECT id FROM Course WHERE title = ?''', (i[1],))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES (?,?,?)''',
                (user_id, course_id, i[2]))
    conn.commit()

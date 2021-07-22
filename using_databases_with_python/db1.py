import sqlite3


def printtable():
    cur.execute("SELECT * FROM Tracks")
    for row in cur:
        print(row)


conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute(
    'CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Tracks (title,plays)  VALUES (?, ?)', ('Aurora', 4))
conn.commit()

print("Tracks:")
printtable()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)', ('Why?', 101))
conn.commit()

printtable()

cur.execute('DELETE FROM Tracks WHERE plays <= 100')
conn.commit()

printtable()

conn.close()

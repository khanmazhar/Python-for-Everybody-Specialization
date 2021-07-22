import sqlite3

conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Tracks;

    CREATE TABLE Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT
    );

    CREATE TABLE Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT
    );

    CREATE TABLE Tracks (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT,
        genre_id INTEGER,
        album_id INTEGER,
        len INTEGER,
        rating INTEGER,
        count INTEGER
    );

    INSERT INTO Artist (name) VALUES ('Led Zeplin'), ('AC/DC');
    INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2), ("IV",1);
    INSERT INTO Genre (name) VALUES ('Rock'), ('Metal');
    INSERT INTO Tracks (title, genre_id, album_id, len, rating, count) 
    VALUES 
        ('Black Dog', 1,2,297,5,0),
        ('Stair Way', 1,2,482,5,0),
        ('About to Rock',2,1,313,5,0),
        ('Who Made Who', 2,1,207,5,0);
    ''')

conn.commit()

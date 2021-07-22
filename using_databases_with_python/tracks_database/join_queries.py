import sqlite3

conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

cur.execute('''
    SELECT
        Tracks.title, Artist.name, Album.title, Genre.name
    FROM
        Tracks JOIN Artist JOIN Album JOIN Genre
    ON 
        Tracks.album_id = Album.id AND
        Tracks.genre_id = Genre.id AND
        Album.artist_id = Artist.id
''')

conn.commit()
for row in cur:
    print(row)

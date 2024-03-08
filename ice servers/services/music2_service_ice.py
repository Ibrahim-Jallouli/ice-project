import sys
import Ice
from flask import Flask, request
from utils.database import Database
from utils.database import test_database_connection
import Music2

app = Flask(__name__)

db = Database()

class MusicData:
    def __init__(self, id=None, title=None, artist=None, filePath=None):
        self.id = id
        self.title = title
        self.artist = artist
        self.filePath = filePath

class Music2ServiceI(Music2.MusicService2):

    def getAll(self, current=None):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM songs")
            result = cursor.fetchall()
            music_list = [MusicData(row['id'], row['title'], row['artist'], row['filePath']) for row in result]
            
            # Serialize the music data list
            music_data_seq = []
            for music_data in music_list:
                music_data_struct = Music2.MusicData(music_data.id, music_data.title, music_data.artist, music_data.filePath)
                music_data_seq.append(music_data_struct)
            print (music_data_seq)
            
            return music_data_seq
        except Exception as e:
            print(f"Error fetching music: {e}")
            return []
        finally:
            db.close_connection(connection)


    def getById(self, id, current=None):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM songs WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:
                music = MusicData(result['id'], result['title'], result['artist'], result['filePath'])
                return music
            else:
                raise Music2.MusicNotFoundException("Music record not found")
        except Exception as e:
            print(f"Error fetching music by ID: {e}")
            raise Music2.MusicException("Error fetching music by ID")
        finally:
            db.close_connection(connection)
    def searchByArtist(self, artist, current=None):
        # Search music records by artist
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM songs WHERE artist LIKE %s", (f"%{artist}%",))
            result = cursor.fetchall()
            music_list = [MusicData(row['id'], row['title'], row['artist'], row['filePath']) for row in result]
            
            # Serialize the music data list
            music_data_seq = []
            for music_data in music_list:
                music_data_struct = Music2.MusicData(music_data.id, music_data.title, music_data.artist, music_data.filePath)
                music_data_seq.append(music_data_struct)
            print (music_data_seq)
            return music_data_seq
        except Exception as e:
            print(f"Error searching music by artist: {e}")
            return []
        finally:
            db.close_connection(connection)

    def searchByTitle(self, title, current=None):
        connection = db.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM songs WHERE title LIKE %s", (f"%{title}%",))
            result = cursor.fetchall()
            music_list = [MusicData(row['id'], row['title'], row['artist'], row['filePath']) for row in result]
            
            music_data_seq = []
            for music_data in music_list:
                music_data_struct = Music2.MusicData(music_data.id, music_data.title, music_data.artist, music_data.filePath)
                music_data_seq.append(music_data_struct)
            print (music_data_seq)
            return music_data_seq
        except Exception as e:
            print(f"Error searching music by title: {e}")
            return []
        finally:
            db.close_connection(connection)



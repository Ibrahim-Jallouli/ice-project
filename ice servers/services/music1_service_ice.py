import sys
import Ice
from utils.database import Database
import Music1

db = Database()

class Music1ServiceI(Music1.MusicService):
    def createMusic(self, title, artist, filePath, current=None):
        try:
            if not title or not artist or not filePath:
                return False
            connection = db.get_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO songs (title, artist, filePath) VALUES (%s, %s, %s)", 
                           (title, artist, filePath))
            connection.commit()
            db.close_connection(connection)
            return True
        except Exception as e:
            print(f"Error adding music: {e}")
            return False

    def updateMusic(self, id, title, artist, filePath, current=None):
        try:
            if not title or not artist or not filePath:
                return False

            connection = db.get_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE songs SET title = %s, artist = %s, filePath = %s WHERE id = %s", 
                           (title, artist, filePath, id))
            connection.commit()
            db.close_connection(connection)
            return True
        except Exception as e:
            print(f"Error updating music: {e}")
            return False

    def deleteMusic(self, id, current=None):
        try:
            connection = db.get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM songs WHERE id = %s", (id,))
            connection.commit()
            db.close_connection(connection)
            return True
        except Exception as e:
            print(f"Error deleting music: {e}")
            return False

# database.py
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

class Database:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host='localhost',
            database='music',
            user='root',  
            password='' 
        )

    def get_connection(self):
        return self.connection_pool.get_connection()

    def close_connection(self, connection):
        connection.close()

def test_database_connection():
    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(
            host='localhost',
            database='music',
            user='root',  
            password=''  
        )

        if connection.is_connected():
            print('Connexion à la base de données réussie !')

            # Exemple de requête de test
            cursor = connection.cursor()
            cursor.execute("SELECT VERSION();")
            db_version = cursor.fetchone()
            print("Version de la base de données : ", db_version)

    except Error as e:
        print("Erreur lors de la connexion à la base de données :", e)

    finally:
        # Fermeture de la connexion
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion à la base de données fermée.")

# Note: The test_database_connection function should be defined outside the Database class.

pour lancer les serveurs :
vous devez creer une environnement virtuel et installer les dependances suivantes :

python -m venv env
.\env\Scripts\activate

pip install zeroc-ice

pip install mysql-connector-python

lancer le serveur avec la commande suivante :

python server1.py 

python server2.py

python serverVLC.py



vous devez changer l'emplacement du dossier ou j'ai stocker les musiques avec l'emplacement que vous avez dans votre machine
    MUSIC_DIR = 'C:\\Users\\Ibrahim\\Desktop\\Music\\coldplay\\X&Y'

et bien sur vous devez changer les informations de connexion a la base de données avec les votres.



**cote client :
vous devez avoir javafx d'installer dans votre machine pour lancer le client.

tout les dependances sont dans le fichier pom.xml

j'ai utilisé maven pour gerer le projet.




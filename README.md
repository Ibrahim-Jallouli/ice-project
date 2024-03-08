pour lancer les serveurs :
vous devez creer une environnement virtuel et installer les dependances suivantes :

python -m venv env
.\env\Scripts\activate

pip install flask ( je l'ai pas utilisé mais je l'ai installé)
pip install zeroc-ice
pip install mysql-connector-python



pour verifier si le port est utilisé ou non :

netstat -ano | findstr :10000
tasklist | findstr num


pour lancer ice grid registry et admin :

icegridregistry --Ice.Config=registry.config
icegridadmin --Ice.Config=registry.config




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
j'ai utilisé maven pour gerer les dependances avec JDK 17

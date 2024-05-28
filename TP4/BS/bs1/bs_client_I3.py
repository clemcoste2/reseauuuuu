import socket
import sys

# On définit la destination de la connexion
host = '10.1.1.3'  # IP du serveur
port = 13337               # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect((host, port))
# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

#connexion au serveur
print(f'Connecté avec succès au serveur {host} sur le port {port}')
# Envoi de data bidon
s.sendall(b'Meooooo !')
print("Que veux-tu envoyer au serveur :")


# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

# utilisateur envoie un string
inp = input()
if type(inp) is not str:
    raise TypeError("Ici on veut que des strings !")
elif "meo" not in inp or "waf" not in inp:
    raise TypeError("Ici meo ou waf!")


# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(f"Le serveur a répondu {repr(data)}")

sys.exit(0)


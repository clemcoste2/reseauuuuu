
import socket 

host = '10.1.1.3'  # IP du serveur
port = 9999             # Port choisir par le serveur

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# on récup une string saisie par l'utilisateur
msg = input('Entrer l opration : (exemple x opération y) ')

# on encode le message explicitement en UTF-8 pour récup un tableau de bytes
encoded_msg = msg.encode('utf-8')

# on calcule sa taille, en nombre d'octets
msg_len = len(encoded_msg)

# on encode ce nombre d'octets sur une taille fixe de 4 octets
header = msg_len.to_bytes(4, byteorder='big')

# on peut concaténer ce header avec le message, avant d'envoyer sur le réseau
payload = header + encoded_msg

# on peut envoyer ça sur le réseau
s.send(payload)
s.close()

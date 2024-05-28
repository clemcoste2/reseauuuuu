import socket

# Adresse IP et port du serveur
host = '10.1.1.3'
port = 12345

# Création du socket et liaison à l'adresse et au port
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("Attente de connexion...")
client, client_addr = s.accept()
print(f"Connexion établie avec {client_addr}")

# Réception des données
received_data = b''
while True:
    chunk = client.recv(1024)
    received_data += chunk
    if received_data.endswith(b'<clafin>'):
        break

# Traitement des données reçues
x = int.from_bytes(received_data[1], byteorder='big')
operation = received_data[2].decode()
y = int.from_bytes(received_data[3], byteorder='big')

print(f"Expression reçue : {x} {operation} {y}")

# Fermeture des sockets
client.close()
s.close()
import socket

# Adresse IP et port du serveur
host= '10.1.1.3'
port = 12345

# Création du socket et connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Saisie de l'expression arithmétique
expression = input("Entrez une expression arithmétique simple (ex. 3 + 3) : ")

# Vérification de la validité de l'expression (à implémenter)

# Séparation des composants de l'expression
components = expression.split()

# Vérification du format de l'expression
if len(components) != 3:
    print("Format incorrect. Utilisez x opération y (par exemple 3 + 3).")
else:
    x, operation, y = components
    try:
        x = int(x)
        y = int(y)
        if operation not in ['+', '-', '*']:
            raise ValueError("Opération non autorisée.")
        if x >= 65536 or y >= 65536:
            raise ValueError("Nombres supérieurs à 65535 ne sont pas autorisés.")
        
        # Envoi de l'expression au serveur
        client_socket.sendall(x.to_bytes(4, byteorder='big'))
        client_socket.sendall(operation.encode())
        client_socket.sendall(y.to_bytes(4, byteorder='big'))
        client_socket.sendall(b'<clafin>')  # Séquence de fin
        
    except ValueError as e:
        print(f"Erreur : {e}")

# Fermeture du socket
client_socket.close()
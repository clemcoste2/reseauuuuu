import socket
import sys
import signal

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("Usage : python3 bs_server_II1.py [OPTION] [ARGUMENT]\n\n\t-h, --help \t\t Affiche l'aide\n\t-p, --port \t\t Spécifie le port sur lequel le serveur va écouter\n\n")
    sys.exit(0)

# On choisit une IP et un port où on va écouter
host = '' # string vide signifie, dans ce conetxte, toutes les IPs de la machine
if sys.argv[1] == '-p' or sys.argv[1] == '--port':
    if 0 <= int(sys.argv[2]) <= 65535:
        if 0 <= int(sys.argv[2]) <= 1024:
            raise ValueError("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
            sys.exit(2)
        else:
            port = int(sys.argv[2])
    else:
        raise ValueError("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
        sys.exit(1)
else:
    port = 13337 # port choisi arbitrairement

# On crée un objet socket
# SOCK_STREAM c'est pour créer un socket TCP (pas UDP donc)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# On demande à notre programme de se bind sur notre portd
s.bind((host, port))  

# Place le programme en mode écoute derrière le port auquel il s'est bind
s.listen(1)


# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:
    try:
        conn, addr = s.accept()
        print("Un client vient de se co et son IP c'est", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break

            if b'meo' in data:
                conn.send(b'Meo a toi confrere.')
            elif b'waf' in data:
                conn.send(b'Ptdr t ki ?')
            else:
                conn.send(b'Mes respects humble humain.')

    except socket.error:
        print("Error Occured.")
        break

def signal_handler(sig, frame):
    conn.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

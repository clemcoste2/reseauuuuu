# TP6 : Chat room

## I. Débuts avec l'asynchrone


## 1. Premiers pas

🌞 [SLEEP AND PRINT](./Annexe/sleep_and_print.py)

🌞 [SLEEP AND PRINT ASYNC](./Annexe/sleep_and_print_async.py)

## 2. Web Requests

🌞 [WEB SYNC](./Annexe/web_sync.py)

🌞 [WEB ASYNC](./Annexe/web_async.py)

🌞 **`web_sync_multiple.py`**

- synchrone (PAS asynchrone)
- pareil `web_sync.py` que mais le script prend en argument un fichier qui contient une liste d'URL
- il stocke le résultat dans `/tmp/web_<URL>` où l'URL c'est par exemple `www.ynov.com` (il faudra enlever le `https://` devant car on peut pas mettre de `/` dans un nom de fichier)

🌞 **`web_async_multiple.py`**

- version asynchrone de `web_sync_multiple.py`

🌞 **Mesure !**

- utilisez la technique de votre choix pour chronométrer le temps d'exécution du script
- comparez les deux pour par exemple 10 URLs passées en argument


## II. Chat Room

Document dédié à la partie II. [Chat Room](./chat_room.md)

## III. Bonus

Document dédié à la partie III. [Bonus](./bonus.md)


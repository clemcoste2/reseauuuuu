# TP1 : Maîtrise réseau du poste

Pour ce TP, on va utiliser **uniquement votre poste** (pas de VM, rien, quedal, quetchi).

Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.

C'est un premier TP *chill*, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.

La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

                    

☀️ **Carte réseau WiFi**

```powershell
PS C:\Users\lacos> ipconfig /all
[...]
Carte réseau sans fil Wi-Fi :
   [...]
   Adresse physique . . . . . . . . . . . : 74-D8-3E-49-4E-A4
   [...]
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.77.204(préféré)
   Masque de sous-réseau. . . . . . . . . : 255.255.240.0
   [...]
```
En notation CIDR : `/20`

En notation décimale :`255.255.255.0`

---

☀️ **Déso pas déso**

L'adresse de réseau du LAN auquel vous êtes connectés en WiFi : 10.33.77.204

L'adresse de broadcast : 10.33.79.255

Le nombre d'adresses IP disponibles dans ce réseau : 	4 096

---

☀️ **Hostname**

Le hostname de votre PC :
```powershell
PS C:\Users\lacos> hostname
VivoBook
```
---

☀️ **Passerelle du réseau**

```powershell
PS C:\Users\lacos\Documents> ipconfig /all
[...]
Carte réseau sans fil Wi-Fi :
  [...]
  Passerelle par défaut. . . . . . . . . : fe80::5efa:25ff:fe36:c4b0%4
                                       192.168.1.1
  [...]
```

☀️ **Serveur DHCP et DNS**

```powershell
PS C:\Users\lacos> ipconfig /all
[...]
Carte réseau sans fil Wi-Fi :
   [...]
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
   [...]
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```
---

☀️ **Table de routage**

```powershell
PS C:\Users\lacos> route print
[...]
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.77.204     35
[...]
```
---

![Not sure](./img/notsure.png)

# II. Go further


---

☀️ **Hosts ?**

```powershell
PS C:\Users\lacos> notepad hosts
```
```
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
1.1.1.1     b2.hello.vous
```
```powershell
PS C:\Users\lacos> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=12 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=12 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 11ms, Maximum = 14ms, Moyenne = 12ms
```
---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

```powershell
PS C:\WINDOWS\system32> netstat -a  -n -b | Select-String 77.136.192.85                                                                                                                                                                           TCP    10.33.77.204:64822     77.136.192.85:443      TIME_WAIT  
```

L'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo : 77.136.192.85 

Le port du serveur auquel vous êtes connectés :443

Le port que votre PC a ouvert en local pour se connecter au port du serveur distant : 64822 

---

☀️ **Requêtes DNS**

www.ynov.com :

```powershell
PS C:\Users\lacos> nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  [...]
          104.26.11.233
```

IP `174.43.238.89`:

```powershell
PS C:\Users\lacos> nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```
---

☀️ **Hop hop hop**

Le nombre de machines vos paquets passent quand vous essayez de joindre `www.ynov.com`: 9
```powershell
PS C:\Users\lacos> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.11.233]
avec un maximum de 30 sauts :

  1     1 ms     1 ms     1 ms  10.33.79.254
  2     5 ms     4 ms     4 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     4 ms     5 ms     3 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     5 ms     7 ms     5 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    19 ms    12 ms    13 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    12 ms    11 ms    12 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    12 ms    12 ms    23 ms  141.101.67.48
  8    12 ms    78 ms    11 ms  172.71.124.4
  9    12 ms    28 ms    12 ms  104.26.11.233

Itinéraire déterminé.
```

---

☀️ **IP publique**

```powershell 
PS C:\Users\lacos> Invoke-RestMethod -Uri ('https://ipinfo.io/')

ip       : 195.7.117.146
[...]
```
---

☀️ **Scan réseau**

Il y a de machines dans le LAN auquel vous êtes connectés :

```powershell
PS C:\Users\lacos> nmap -sn 10.33.64.0/20
Nmap done: 4096 IP addresses (672 hosts up) scanned in 162.20 seconds
```

# III. Le requin
---

☀️ **Capture ARP**

📁 fichier `arp.pcap`
[CAPTURE ARP](./SCAN/arp.pcapng)

---

☀️ **Capture DNS**

📁 fichier `dns.pcap`

[CAPTURE DNS](./SCAN/dns.pcapng)

---

☀️ **Capture TCP**

📁 fichier `tcp.pcap`

[CAPTURE TCP](./SCAN/tcp.pcapng)

---


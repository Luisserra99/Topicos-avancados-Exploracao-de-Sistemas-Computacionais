# CRACK THE HASH

https://tryhackme.com/room/crackthehash

## Task1 - 1

Hash: 48bb6e862e54f2a795ffc4e541caed4d

### Solução

- cybercheft

MD5
MD4
MD2
HAVAL-128
RIPEMD-128
Snefru
Tiger-128

- hashcat:
  - 

```
hashcat -m 0 -a 0 t1_1.txt /usr/share/wordlists/rockyou.txt
```

- saída
  - **easy**

## Task1 - 2

Hash: CBFDAC6008F9CAB4083784CBD1874F76618D2A97

### Solução

- cybercheft

SHA-1
SHA-0
FSB-160
HAS-160
HAVAL-160
RIPEMD-160
Tiger-160

- hashcat:
  - sha-1 - mode 100

```
hashcat -m 100 -a 0 t1_2.txt /usr/share/wordlists/rockyou.txt
```

- saída
  - **password123**

## Task1 - 3

Hash: 1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

### Solução

- cybercheft

SHA-256
SHA3-256
BLAKE-256
ECOH-256
FSB-256
GOST
Grøstl-256
HAVAL-256
PANAMA
RIPEMD-256
Snefru

- hashcat:
  - sha-256 - mode 1400

```
hashcat -m 1400 -a 0 t1_3.txt /usr/share/wordlists/rockyou.txt
```

- saída
  - **letmein**

## Task1 - 4

Hash: $2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

### Solução

- hashid

[+] Blowfish(OpenBSD) [Hashcat Mode: 3200]
[+] Woltlab Burning Board 4.x 
[+] bcrypt [Hashcat Mode: 3200]

- hashcat:
  - blowfish - mode 3200
  - filter list of rockyou to get only 4 char words

```
grep -xE '[A-Za-z]{4}' /usr/share/wordlists/rockyou.txt > words4.txt
hashcat -m 3200 -a 0 t1_4.txt words4.txt
```

- saída
  - bleh

## Task1 - 5

Hash: 279412f945939ba78ce0758d3fd83daa

### Solução

- cybercheft

MD5
MD4
MD2
HAVAL-128
RIPEMD-128
Snefru
Tiger-128

- hashcat1:
  - md5 - mode 0

```
hashcat -m 900 -a 0 t1_5.txt /usr/share/wordlists/rockyou.txt
```

- hashcat2:
  - md4 - mode 900

```
hashcat -m 900 -a 0 t1_5.txt /usr/share/wordlists/rockyou.txt
```

- hashcat3:
  - md4 - mode 900
  - 10 letras
  - demoraria 5 dias mesmo com o -O

```
hashcat -m 900 -a 3 t1_5.txt ?l?l?l?l?l?l?l?l?l?l
```

- hashcat4
  - md4 - mode 900
  - baixei a lista do fortinet https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/fortinet-2021_passwords.txt
  - também não funcionou

- hashcat5
  - md4 - mode 900
  - rockyou
  - uso das rules para variações

```
hashcat -m 900 -a 0 t1_5.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- saída
  - **Eternity22**


## Task2 - 1

Hash: F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

### Solução

- cybercheft
  
SHA-256
SHA3-256
BLAKE-256
ECOH-256
FSB-256
GOST
Grøstl-256
HAVAL-256
PANAMA
RIPEMD-256
Snefru

- hashcat:
  - sha-256 - mode 1400

```
hashcat -m 1400 -a 0 t2_1.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- saída
  - **paule**

## Task2 - 2

Hash:

### Solução

- hashid
  
[+] MD2 
[+] MD5 [Hashcat Mode: 0]
[+] MD4 [Hashcat Mode: 900]
[+] Double MD5 [Hashcat Mode: 2600]
[+] LM [Hashcat Mode: 3000]
[+] RIPEMD-128 
[+] Haval-128 
[+] Tiger-128 
[+] Skein-256(128) 
[+] Skein-512(128) 
[+] Lotus Notes/Domino 5 [Hashcat Mode: 8600]
[+] Skype [Hashcat Mode: 23]
[+] Snefru-128 
[+] NTLM [Hashcat Mode: 1000]
[+] Domain Cached Credentials [Hashcat Mode: 1100]
[+] Domain Cached Credentials 2 [Hashcat Mode: 2100]
[+] DNSSEC(NSEC3) [Hashcat Mode: 8300]
[+] RAdmin v2.x [Hashcat Mode: 9900]

- hashcat1:
  - md5 - mode 0

```
hashcat -m 0 -a 0 t2_2.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule -O
```

- hashcat2:
  - md4 - mode 900

```
hashcat -m 900 -a 0 t2_2.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule -O
```

- hashcat3:
  - md5 - mode 2600

```
hashcat -m 2600 -a 0 t2_2.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule -O
```

- hashcat4:
  - md5 - mode 3000

```
hashcat -m 3000 -a 0 t2_2.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- hashcat5:
  - Lotus Notes/Domino 5 - mode 8600
  - demoraria 30 min com o flag -r

```
hashcat -m 8600 -a 0 t2_2.txt /usr/share/wordlists/rockyou.txt -r
```


- hashcat6:
  - ntlm - mode 1000

```
hashcat -m 1000 -a 0 t2_2.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- saída
  - **n63umy8lkf4i**

## Task2 - 3

Hash: $6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

salt: eaReallyHardSalt

### Solução

- hashid

[+] SHA-512 Crypt [Hashcat Mode: 1800]

- hashcat:
  - sha-512 - mode 1800
  - o salt já está no hash
  - daria horas
  - filtrei o rockyou por palavras de 6 digitos
  - ainda sim demorou quase 10 minutos pra rodar

```
grep -xE '[A-Za-z0-9]{6}' /usr/share/wordlists/rockyou.txt > words6.txt
hashcat -m 1800 -a 0 t2_3.txt words6.txt -O  
```

- saída
  - **waka99**


## Task2 - 4

Hash: e5d8870e5bdd26602cab8dbe07a942c8669e56d6

Salt: tryhackme

### Solução

- hashid

[+] SHA-1 [Hashcat Mode: 100]
[+] Double SHA-1 [Hashcat Mode: 4500]
[+] RIPEMD-160 [Hashcat Mode: 6000]
[+] Haval-160 
[+] Tiger-160 
[+] HAS-160 
[+] LinkedIn [Hashcat Mode: 190]
[+] Skein-256(160) 
[+] Skein-512(160) 
[+] SMF ≥ v1.1 [Hashcat Mode: 121]

- hashcat1:
  - sha-1 - mode 110 - pass-salt

```
hashcat -m 110 -a 0 t2_4.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- hashcat2:
  - sha-1 - mode 120 - salt-pass

```
hashcat -m 120 -a 0 t2_4.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- hashcat3:
  - hmac-sha-1 - mode 160 - HMAC-SHA1 (key = $salt)

```
hashcat -m 160 -a 0 t2_4.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best66.rule
```

- saída
  - **481616481616**

# HASSHES ADICIONAIS

## 1

Hash: 482c811da5d5b4bc6d497ffa98491e38

### SOLUÇÃO

- cyberchef:
MD5
MD4
MD2
HAVAL-128
RIPEMD-128
Snefru
Tiger-128

- hashcat:
  - md5 - mode 0

```
hashcat -m 0 -a 0 add1.txt /usr/share/wordlists/rockyou.txt
```

- saída
  - **password123**

## 2

Hash: 861c4f67e887dec85292d36ab05cd7a1a7275228

### SOLUÇÃO

- cyberchef
SHA-1
SHA-0
FSB-160
HAS-160
HAVAL-160
RIPEMD-160
Tiger-160

- hashcat
  - sha1 - mode 100

```
hashcat -m 100 -a 0 add2.txt /usr/share/wordlists/rockyou.txt
```

- saída
  - **easy**

## 3

Hash: 4149c5cc4c378444d116d65ad5ba4099
DICA: apenas letras e números (6 caracteres)

### SOLUÇÃO

- cyberchef

MD5
MD4
MD2
HAVAL-128
RIPEMD-128
Snefru
Tiger-128

- hashcat 1
  - md5 - mode 0

```
hashcat -m 0 -a 3 add3.txt -1 ?d?u?l ?1?1?1?1?1?1
```

- saída
  - exausted

- hashcat 2
  - md4 - mode 900

```
hashcat -m 900 -a 3 add3.txt -1 ?d?u?l ?1?1?1?1?1?1
```

- saída
  - **0ffs3c**


## 4

Hash: cdeb746ec095149627348b61d4140fc58b745875
Salt: satech
DICA: HMAC-SHA1

### SOLUÇÃO

- hashcat
  - hmac-sha1 - with salt - mode 160
  - hash analisado cdeb746ec095149627348b61d4140fc58b745875:satech

```
 hashcat -m 160 -a 0 add4.txt /usr/share/wordlists/rockyou.txt 
```

- saída
  - **ovelha** 

## 5

Hash: 362fda2183b7ac73400a83f6ab2c359451e48adf6c3d46a2963ee2abdf852912
DICA: Apenas letras minúsculas e números (6 caracteres)

### SOLUÇÃO

- cyberchef

SHA-256
SHA3-256
BLAKE-256
ECOH-256
FSB-256
GOST
Grøstl-256
HAVAL-256
PANAMA
RIPEMD-256
Snefru

- hashcat
  - sha-256 mode 1400

```
hashcat -m 1400 -a 3 add5.txt -1 ?d?l ?1?1?1?1?1?1
```

- saída
  - **sawctf**
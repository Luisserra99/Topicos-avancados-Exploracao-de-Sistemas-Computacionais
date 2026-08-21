# Metodologia para Construção de Write-Ups em CTF

*Metodologia de Write-Ups — Segurança Ofensiva*

## 1. Objetivo

Padronizar a documentação técnica de resolução de máquinas e desafios CTF, garantindo que o write-up seja reproduzível, claro e adequado para avaliação e portfólio.

## 2. Estrutura Obrigatória do Documento

O write-up deve conter as seguintes seções, nesta ordem:

### 2.1. Capa

Nome do desafio ou máquina, plataforma (ex.: HackTheBox, TryHackMe, Hacking Club), dificuldade e data de resolução.

### 2.2. Sumário

Índice com as seções e respectivas páginas, gerado automaticamente ou manualmente.

### 2.3. Visão Geral

Parágrafo descrevendo o vetor principal de ataque sem spoiler detalhado. Deve responder: o que é o desafio, qual a superfície de ataque explorada e qual foi o caminho geral até o objetivo.

### 2.4. Reconhecimento

Resultados da enumeração externa: portas abertas, serviços identificados, versões relevantes, tecnologias detectadas. Incluir comandos usados e os trechos de output mais relevantes. Não incluir informações obtidas após o foothold inicial.

### 2.5. Exploração

Descrição técnica do vetor de entrada. Deve incluir o raciocínio que levou à identificação da vulnerabilidade, os payloads ou scripts utilizados (comentados), exploits públicos utilizados e os outputs que confirmam o acesso. Cada passo deve ser justificado, não apenas listado.

### 2.6. Movimentação Lateral (se aplicável)

Aplicável quando há múltiplos usuários ou pivoting entre serviços. Descrever a escalada horizontal com o mesmo padrão da seção anterior.

### 2.7. Escalada de Privilégios

Descrever o vetor de privesc identificado, o processo de enumeração local que o revelou (linpeas, `sudo -l`, capabilities, etc.) e a exploração realizada. Incluir o comando final que comprova o acesso root/SYSTEM.

### 2.8. Conclusão

Resumo técnico de 3 a 5 linhas sintetizando a cadeia de exploração completa, do reconhecimento à flag.

### 2.9. Referências

Espaço destinado às fontes utilizadas para a exploração: links dos repositórios dos exploits públicos e links das CVEs correspondentes.

## 3. Regras de Qualidade

- Todos os comandos devem estar em blocos de código. Exemplo:

  ```bash
  nmap -sC -sV -p- --min-rate 5000 -oN nmap/initial <TARGET_IP>
  ```

- Outputs longos devem ser truncados; manter apenas o trecho relevante para o entendimento.
- IPs reais, senhas capturadas, hashes e tokens devem ser substituídos por placeholders: `<TARGET_IP>`, `<PASSWORD>`, `<HASH>`.
- Flags não devem ser exibidas no corpo do documento; usar `<FLAG>` como placeholder.

## 4. Formatação do PDF

- Fonte: Times New Roman, tamanho 11 ou 12 para corpo, 14 ou 16 para títulos de seção.
- Blocos de código em fonte monoespaçada com fundo destacado (cinza claro ou escuro).
- Imagens e screenshots devem ter legenda descritiva e estar inseridas imediatamente após o texto que as referencia.
- Numeração de páginas obrigatória. Cabeçalho ou rodapé com nome do desafio e autor.
- Margem mínima de 2 cm em todos os lados.

## 5. O que não deve aparecer no write-up

- Prints de tela sem legenda ou contexto.
- Comandos sem explicação do porquê foram executados.
- Seções vazias ou com texto genérico não aplicado ao desafio.
- Informações que identifiquem outros jogadores ou flags de terceiros.

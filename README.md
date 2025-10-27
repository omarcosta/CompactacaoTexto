## Projeto de Compressão de Dados - DSPTI

- **Curso:** Jogos Digitais - Fatec Carapibuíba
- **Disciplina:** DSPTI
- **Professora:** Magali Andreia Rossi
- **Semestre:** 2º Semestre (Noite)
- **Aluno:** Omar Costa

-----

### 1\. Descrição do Projeto

Este projeto consiste no desenvolvimento de dois algoritmos de compressão de dados sem perdas (*lossless*) em Python. O objetivo é aplicar os conceitos teóricos de compressão para ler um arquivo de texto, gerar uma versão comprimida e, em seguida, descomprimir o arquivo de volta ao seu estado original.

Seguindo as diretrizes do projeto, os códigos foram escritos de forma **sequencial** (passo a passo, sem o uso de funções ou classes) e com uma **lógica simples**, visando a clareza e o fácil entendimento para desenvolvedores iniciantes.

### 2\. Técnicas Implementadas

Foram desenvolvidos dois algoritmos distintos, cada um em seu próprio arquivo, conforme a Regra 1.

#### Técnica 1: Repetição de Caracteres (Run-Length)

  * **Arquivo:** `repeticao.py`
  * **Lógica:** Este algoritmo identifica sequências de **4 ou mais** caracteres idênticos e as substitui por uma *tag*, o caractere e o número de repetições.
  * **Tag de Compressão:** `"#"` 
  * **Exemplo:** A string `aaaaa` (5 'a's) é comprimida para `#a5`.
  * **Observação:** Sequências com 3 ou menos caracteres (ex: `aaa`) não são comprimidas e são mantidas em sua forma original, conforme a teoria.

#### Técnica 2: Supressão de Brancos

  * **Arquivo:** `brancos.py`
  * **Lógica:** Este algoritmo identifica *qualquer* sequência de um ou mais caracteres de espaço (`' '`) e a substitui por uma *tag* e o número de espaços.
  * **Tag de Compressão:** `"#"` (Utilizamos `"#"` para manter a consistência e evitar "colisões" com dados reais, como em "vitamina b12", que foi uma reflexão de design).
  * **Exemplo:** Uma sequência de 4 espaços (`        `) é comprimida para `#4`.

### 3\. Decisão de Design: A Regra 12 (Limite de 9)

Uma decisão de design importante foi como implementar a **Regra 12**, que diz: "Não é necessário tratar os valores de dezenas e centenas... A correção considerará o valor de unidade, valores de 0 a 9".

Para manter a lógica "Nível Iniciante", implementamos essa regra da seguinte forma:

1.  **Na Compressão:** O contador interno para de contar ao atingir 9 repetições. Se um texto tiver 12 'a's, o compressor gera dois blocos: `#a9` e `#a3`.
2.  **Na Descompressão:** Isso torna a descompressão muito mais simples. O descompressor sabe que, após a tag e o caractere, haverá **exatamente um** dígito numérico. Ele não precisa de uma lógica complexa para ler números de múltiplos dígitos.

### 4\. Estrutura de Pastas

O projeto segue a estrutura de pastas exigida pela Regra 16:

```
/ (Pasta Raiz)
|
|-- brancos/
|   |-- arquivo.txt
|   |-- compactado_arquivo.txt
|   |-- descompactado_arquivo.txt
|
|-- repeticao/
|   |-- arquivo.txt
|   |-- compactado_arquivo.txt
|   |-- descompactado_arquivo.txt
|
|-- brancos.py
|-- repeticao.py
|-- (Outros arquivos de teoria, regras, etc.)
```

### 5\. Como Usar

1.  Coloque o texto que deseja testar dentro dos arquivos `brancos/arquivo.txt` e `repeticao/arquivo.txt`.

2.  Execute os scripts Python a partir da pasta raiz do projeto:

    ```sh
    # Para executar a compressão de repetição de caracteres
    python repeticao.py

    # Para executar a compressão de supressão de brancos
    python brancos.py
    ```

3.  Os scripts irão ler o `arquivo.txt`, gerar o `compactado_arquivo.txt` e, em seguida, ler o arquivo compactado para gerar o `descompactado_arquivo.txt`, confirmando que o processo foi 100% revertido.
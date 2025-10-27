# 1) DEFINIÇÃO DE VARIÁVEIS
texto_original = "" # Variável para armazenar o texto original lido do arquivo
texto_comprimido = "" # Variável para armazenar o texto comprimido
texto_descompactado = "" # Variável para armazenar o texto descompactado
tag = "#"  # Tag que marca o início de uma sequência comprimida, conforme Teoria.pdf [cite: 117]
caminho_arquivo_original = "repeticao/arquivo.txt"  # Caminho do arquivo que será lido [cite: 2204]
caminho_arquivo_compactado = "repeticao/compactado_arquivo.txt" # Caminho do arquivo que será gravado [cite: 2205]
caminho_arquivo_descompactado = "repeticao/descompactado_arquivo.txt" # Caminho do arquivo que será descompactado
i = 0 # Variável de índice principal para percorrer os textos
contador = 0 # Contador para rastrear o número de repetições, iniciando em 0

# 2) LEITURA DO ARQUIVO
    # WITH abre o arquivo em modo de leitura
    # "r" significa read (apenas ler)
    # encoding utf-8 (reconhece o texto no padrão de escrita Brasil)
with open(caminho_arquivo_original, "r", encoding="utf-8") as f: # Abre o arquivo de origem [cite: 2204]
    texto_original = f.read() # O texto original é definido como a leitura do arquivo
print(f"Lido arquivo original com {len(texto_original)} caracteres.") # Mensagem de feedback

# 3) COMPRESSÃO DO TEXTO (Técnica: Repetição de Caracteres / Run Length) [cite: 97]
print("Iniciando compressão...") # Mensagem de feedback
i = 0 # Zera o índice principal para percorrer o texto original
while i < len(texto_original): # Loop que percorre toda a string original
    char_base = texto_original[i] # Pega o caractere que vamos começar a contar
    contador = 0 # Zera o contador para cada nova sequência de caracteres
    j = i # Inicia um índice 'j' para o loop interno, começando da posição de 'i'
    
    # Loop interno que conta as repetições
    while j < len(texto_original) and texto_original[j] == char_base: # Continua enquanto o caractere for igual E não chegar no fim do texto
        contador += 1 # Incrementa o contador de repetições
        if contador == 9: # Verifica se atingiu o limite da Regra 12 
            break # Se atingiu 9, para de contar este bloco
        j += 1 # Avança o índice do loop interno
    
    # Fim do loop interno - Agora vamos decidir como gravar
    if contador >= 4: # Se a contagem for 4 ou mais, aplica a compressão [cite: 116]
        texto_comprimido += f"{tag}{char_base}{contador}" # Grava a tag, o caractere e o número (ex: #a9)
    else: # Se for 1, 2 ou 3 repetições
        texto_comprimido += char_base * contador # Grava os caracteres de forma literal (ex: ccc)
    
    i += contador # Avança o índice principal 'i' pela quantidade de caracteres que já processamos
print("Compressão finalizada.") # Mensagem de feedback

# 4) GRAVAÇÃO DO ARQUIVO COMPACTADO
    # WITH abre o arquivo em modo de escrita
    # "w" significa write (escrever), apagando o que existia antes
with open(caminho_arquivo_compactado, "w", encoding="utf-8") as f: # Abre o arquivo de destino [cite: 2205]
    f.write(texto_comprimido) # Salva o texto comprimido no arquivo especificado
print(f"Arquivo '{caminho_arquivo_compactado}' gravado com {len(texto_comprimido)} caracteres.") # Mensagem de feedback

# 5) LER O ARQUIVO COMPACTADO PARA DESCOMPACTAR
with open(caminho_arquivo_compactado, "r", encoding="utf-8") as f: # Abre o arquivo compactado em modo de leitura
    texto_comprimido = f.read() # Lê o conteúdo do arquivo compactado
print("Lido arquivo compactado.") # Mensagem de feedback

# 6) DESCOMPRESSÃO DO TEXTO
print("Iniciando descompressão...") # Mensagem de feedback
i = 0 # Zera o índice principal para percorrer o texto comprimido
while i < len(texto_comprimido): # Loop que percorre toda a string comprimida
    char_atual = texto_comprimido[i] # Pega o caractere atual
    
    if char_atual == tag: # Verifica se o caractere é a nossa 'tag' (ex: #)
        # Se for a tag, sabemos que é um bloco comprimido
        char_base = texto_comprimido[i + 1] # O próximo caractere é a letra a ser repetida
        contador_str = texto_comprimido[i + 2] # O caractere seguinte é o número (como string)
        contador = int(contador_str) # Converte o número (string) para inteiro
        
        texto_descompactado += char_base * contador # Adiciona o caractere repetido 'contador' vezes
        i += 3 # Avança o índice em 3 (pulando o '#', o 'char' e o 'numero')
    else:
        # Se não for a tag, é um caractere normal (não comprimido)
        texto_descompactado += char_atual # Adiciona o caractere literal ao resultado
        i += 1 # Avança o índice em 1
print("Descompressão finalizada.") # Mensagem de feedback

# 7) GRAVAÇÃO DO ARQUIVO DESCOMPACTADO
with open(caminho_arquivo_descompactado, "w", encoding="utf-8") as f: # Abre o arquivo final
    f.write(texto_descompactado) # Salva o texto original restaurado
print(f"Arquivo '{caminho_arquivo_descompactado}' gravado com {len(texto_descompactado)} caracteres.") # Mensagem de feedback
print("\nProcesso de Repetição Concluído.") # Mensagem final
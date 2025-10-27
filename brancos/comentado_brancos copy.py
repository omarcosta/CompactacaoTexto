# 1) DEFINIÇÃO DE VARIÁVEIS
texto_original = "" # Variável para armazenar o texto original lido do arquivo
texto_comprimido = "" # Variável para armazenar o texto comprimido
texto_descompactado = "" # Variável para armazenar o texto descompactado
tag = "#"  # Tag que marca a supressão de brancos, conforme Teoria.pdf 
caminho_arquivo_original = "brancos/arquivo.txt"  # Caminho do arquivo que será lido 
caminho_arquivo_compactado = "brancos/compactado_arquivo.txt" # Caminho do arquivo que será gravado 
caminho_arquivo_descompactado = "brancos/descompactado_arquivo.txt" # Caminho do arquivo que será descompactado
i = 0 # Variável de índice principal para percorrer os textos
contador = 0 # Contador para rastrear o número de repetições, iniciando em 0

# 2) LEITURA DO ARQUIVO
    # WITH abre o arquivo em modo de leitura
    # "r" significa read (apenas ler)
    # encoding utf-8 (reconhece o texto no padrão de escrita Brasil)
with open(caminho_arquivo_original, "r", encoding="utf-8") as f: # Abre o arquivo de origem 
    texto_original = f.read() # O texto original é definido como a leitura do arquivo
print(f"Lido arquivo original com {len(texto_original)} caracteres.") # Mensagem de feedback

# 3) COMPRESSÃO DO TEXTO (Técnica: Supressão de Brancos) 
print("Iniciando compressão de brancos...") # Mensagem de feedback
i = 0 # Zera o índice principal para percorrer o texto original
while i < len(texto_original): # Loop que percorre toda a string original
    caractere_analisado = texto_original[i] # Pega o caractere que vamos analisar
    
    if caractere_analisado == ' ': # Verifica se o caractere é um espaço
        # Se for um espaço, vamos contar a sequência
        contador = 0 # Zera o contador para a nova sequência de espaços
        j = i # Inicia um índice 'j' para o loop interno
        
        # Loop interno que conta apenas os espaços
        while j < len(texto_original) and texto_original[j] == ' ': # Continua enquanto for espaço E não chegar no fim
            contador += 1 # Incrementa o contador de espaços
            if contador == 9: # Verifica se atingiu o limite da Regra 12 
                break # Se atingiu 9, para de contar este bloco
            j += 1 # Avança o índice do loop interno
            
        # Fim do loop de contagem de espaços
        texto_comprimido += f"{tag}{contador}" # Grava a tag 'b' e o número (ex: b9) 
        i += contador # Avança o índice principal 'i' pela quantidade de espaços que processamos
    
    else: # Se o caractere NÃO for um espaço
        texto_comprimido += caractere_analisado # Grava o caractere de forma literal
        i += 1 # Avança o índice principal em 1
print("Compressão de brancos finalizada.") # Mensagem de feedback

# 4) GRAVAÇÃO DO ARQUIVO COMPACTADO
    # "w" significa write (escrever), apagando o que existia antes
with open(caminho_arquivo_compactado, "w", encoding="utf-8") as f: # Abre o arquivo de destino 
    f.write(texto_comprimido) # Salva o texto comprimido no arquivo especificado
print(f"Arquivo '{caminho_arquivo_compactado}' gravado com {len(texto_comprimido)} caracteres.") # Mensagem de feedback

# 5) LER O ARQUIVO COMPACTADO PARA DESCOMPACTAR
with open(caminho_arquivo_compactado, "r", encoding="utf-8") as f: # Abre o arquivo compactado em modo de leitura
    texto_comprimido = f.read() # Lê o conteúdo do arquivo compactado
print("Lido arquivo compactado.") # Mensagem de feedback

# 6) DESCOMPRESSÃO DO TEXTO
print("Iniciando descompressão de brancos...") # Mensagem de feedback
i = 0 # Zera o índice principal para percorrer o texto comprimido
while i < len(texto_comprimido): # Loop que percorre toda a string comprimida
    caractere_atual = texto_comprimido[i] # Pega o caractere atual
    
    if caractere_atual == tag: # Verifica se o caractere é a nossa 'tag' (ex: b) 
        # Se for a tag, sabemos que é um bloco de espaços
        contador_str = texto_comprimido[i + 1] # O caractere seguinte é o número (como string)
        contador = int(contador_str) # Converte o número (string) para inteiro
        
        texto_descompactado += ' ' * contador # Adiciona o espaço repetido 'contador' vezes
        i += 2 # Avança o índice em 2 (pulando o 'b' e o 'numero')
    else:
        # Se não for a tag, é um caractere normal (não comprimido)
        texto_descompactado += caractere_atual # Adiciona o caractere literal ao resultado
        i += 1 # Avança o índice em 1
print("Descompressão de brancos finalizada.") # Mensagem de feedback

# 7) GRAVAÇÃO DO ARQUIVO DESCOMPACTADO
with open(caminho_arquivo_descompactado, "w", encoding="utf-8") as f: # Abre o arquivo final
    f.write(texto_descompactado) # Salva o texto original restaurado
print(f"Arquivo '{caminho_arquivo_descompactado}' gravado com {len(texto_descompactado)} caracteres.") # Mensagem de feedback
print("\nProcesso de Brancos Concluído.") # Mensagem final
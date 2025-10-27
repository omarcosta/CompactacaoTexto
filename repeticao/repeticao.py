# 1) DEFINIÇÃO DE VARIÁVEIS
texto_original = "" 
texto_comprimido = "" 
texto_descompactado = "" 
tag = "#"  
caminho_arquivo_original = "repeticao/arquivo.txt"  
caminho_arquivo_compactado = "repeticao/compactado_arquivo.txt" 
caminho_arquivo_descompactado = "repeticao/descompactado_arquivo.txt" 

# 2) LEITURA DO ARQUIVO (Regra 4) [cite: 11]
with open(caminho_arquivo_original, "r", encoding="utf-8") as f: 
    texto_original = f.read() 
print(f"Lido arquivo original com {len(texto_original)} caracteres.") 

# 3) COMPRESSÃO DO TEXTO (Técnica: Repetição de Caracteres / Run Length) [cite: 3208]
print("Iniciando compressão...") 
i = 0 
while i < len(texto_original): 
    caractere_analisado = texto_original[i] 
    contador = 0 
    j = i 
    
    while j < len(texto_original) and texto_original[j] == caractere_analisado: 
        contador += 1 
        if contador == 9: 
            break 
        j += 1 
    
    if contador >= 4: 
        texto_comprimido += f"{tag}{caractere_analisado}{contador}" 
    else: 
        texto_comprimido += caractere_analisado * contador 
    
    i += contador 
print("Compressão finalizada.") 

# 4) GRAVAÇÃO DO ARQUIVO COMPACTADO (Regra 5) [cite: 12]
with open(caminho_arquivo_compactado, "w", encoding="utf-8") as f: 
    f.write(texto_comprimido) 
print(f"Arquivo '{caminho_arquivo_compactado}' gravado com {len(texto_comprimido)} caracteres.") 

# 5) LER O ARQUIVO COMPACTADO PARA DESCOMPACTAR
with open(caminho_arquivo_compactado, "r", encoding="utf-8") as f: 
    texto_comprimido = f.read() 
print("Lido arquivo compactado.") 

# 6) DESCOMPRESSÃO DO TEXTO
print("Iniciando descompressão...") 
i = 0 
while i < len(texto_comprimido): 
    caractere_atual = texto_comprimido[i] 
    
    if caractere_atual == tag: 
        caractere_analisado = texto_comprimido[i + 1] 
        contador_str = texto_comprimido[i + 2] 
        contador = int(contador_str) 
        
        texto_descompactado += caractere_analisado * contador 
        i += 3 
    else:
        texto_descompactado += caractere_atual 
        i += 1 
print("Descompressão finalizada.") 

# 7) GRAVAÇÃO DO ARQUIVO DESCOMPACTADO (Regra 5) [cite: 12]
with open(caminho_arquivo_descompactado, "w", encoding="utf-8") as f: 
    f.write(texto_descompactado) 
print(f"Arquivo '{caminho_arquivo_descompactado}' gravado com {len(texto_descompactado)} caracteres.") 
print("\nProcesso de Repetição Concluído.")
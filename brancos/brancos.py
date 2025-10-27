# 1) DEFINIÇÃO DE VARIÁVEIS
texto_original = "" 
texto_comprimido = "" 
texto_descompactado = "" 
tag = "#"  
caminho_arquivo_original = "brancos/arquivo.txt"  
caminho_arquivo_compactado = "brancos/compactado_arquivo.txt" 
caminho_arquivo_descompactado = "brancos/descompactado_arquivo.txt" 
i = 0 
contador = 0 

# 2) LEITURA DO ARQUIVO
with open(caminho_arquivo_original, "r", encoding="utf-8") as f: 
    texto_original = f.read() 
print(f"Lido arquivo original com {len(texto_original)} caracteres.") 

# 3) COMPRESSÃO DO TEXTO (Técnica: Supressão de Brancos) [cite: 96, 104]
print("Iniciando compressão de brancos...") 
i = 0 
while i < len(texto_original): 
    caractere_analisado = texto_original[i] 
    
    if caractere_analisado == ' ': 
        contador = 0 
        j = i 
        
        while j < len(texto_original) and texto_original[j] == ' ': 
            contador += 1 
            if contador == 9: 
                break 
            j += 1 
            
        texto_comprimido += f"{tag}{contador}" 
        i += contador 
    
    else: 
        texto_comprimido += caractere_analisado 
        i += 1 
print("Compressão de brancos finalizada.") 

# 4) GRAVAÇÃO DO ARQUIVO COMPACTADO
with open(caminho_arquivo_compactado, "w", encoding="utf-8") as f: 
    f.write(texto_comprimido) 
print(f"Arquivo '{caminho_arquivo_compactado}' gravado com {len(texto_comprimido)} caracteres.") 

# 5) LER O ARQUIVO COMPACTADO PARA DESCOMPACTAR
with open(caminho_arquivo_compactado, "r", encoding="utf-8") as f: 
    texto_comprimido = f.read() 
print("Lido arquivo compactado.") 

# 6) DESCOMPRESSÃO DO TEXTO
print("Iniciando descompressão de brancos...") 
i = 0 
while i < len(texto_comprimido): 
    caractere_atual = texto_comprimido[i] 
    
    if caractere_atual == tag: 
        contador_str = texto_comprimido[i + 1] 
        contador = int(contador_str) 
        
        texto_descompactado += ' ' * contador 
        i += 2 
    else:
        texto_descompactado += caractere_atual 
        i += 1 
print("Descompressão finalizada.") 

# 7) GRAVAÇÃO DO ARQUIVO DESCOMPACTADO
with open(caminho_arquivo_descompactado, "w", encoding="utf-8") as f: 
    f.write(texto_descompactado) 
print(f"Arquivo '{caminho_arquivo_descompactado}' gravado com {len(texto_descompactado)} caracteres.") 
print("\nProcesso de Brancos Concluído.")
import re

# Função para limpar texto
def limpar_texto(texto):
    # Remover quebras de linha excessivas e espaços extras
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Abrir o arquivo de dados_formatados.txt para leitura
with open('dados_formatados.txt', 'r', encoding='utf-8') as file:
    dados = file.readlines()

# Abre um novo arquivo para salvar os dados formatados
with open('dados_limpos_formatados.txt', 'w', encoding='utf-8') as file:
    file.write("Dados extraídos e formatados da página de Wikipedia sobre Contabilidade:\n\n")
    
    # Processar cada linha dos dados
    index = 1
    for linha in dados:
        # Limpeza de cada linha
        linha = limpar_texto(linha)
        
        if linha.startswith("Conteúdo"):
            # Escrever o número do processo
            file.write(f"{linha}\n")
        elif linha.startswith("Título"):
            # Escrever o título
            titulo = limpar_texto(linha.split(":")[1])  # Limpar o texto após o ":"
            file.write(f"Título: {titulo}\n")
        elif linha.startswith("Introdução"):
            # Escrever a introdução
            introducao = limpar_texto(linha.split(":")[1])  # Limpar o texto após o ":"
            file.write(f"Introdução: {introducao}\n")
        elif linha.startswith("Links"):
            # Escrever os links
            links = limpar_texto(linha.split(":")[1])  # Limpar o texto após o ":"
            file.write(f"Links: {links}\n")
        
        # Adicionar uma linha de separação entre os processos
        if "Processo" in linha:
            file.write("\n" + "-"*50 + "\n\n")

print("Dados limpos e formatados foram salvos em 'dados_limpos_formatados.txt'.")

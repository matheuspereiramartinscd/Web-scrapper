from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Iniciar o WebDriver (assumindo que o ChromeDriver está no PATH)
driver = webdriver.Chrome()

# Acesse a página de Contabilidade na Wikipedia
url = 'https://pt.wikipedia.org/wiki/Contabilidade'
driver.get(url)

# Aguardar o carregamento da página
driver.implicitly_wait(10)

# Função para coletar os dados
def coletar_dados():
    dados = []

    try:
        # Coletar o título da página
        titulo = driver.find_element(By.ID, 'firstHeading').text
        
        # Coletar o primeiro parágrafo (introdução)
        intro = driver.find_element(By.CSS_SELECTOR, 'div.mw-parser-output > p').text
        
        # Coletar todos os links internos da página
        links = driver.find_elements(By.CSS_SELECTOR, 'div.mw-parser-output a[href^="/wiki/"]')
        
        # Criar uma lista com os links internos
        links_internos = [link.get_attribute('href') for link in links]
        
        # Adicionar os dados coletados
        dados.append([titulo, intro, links_internos])

    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
    
    return dados

# Função para salvar os dados no formato de texto
def salvar_em_texto(dados):
    with open('dados_formatados.txt', 'w', encoding='utf-8') as file:
        # Escreve um cabeçalho
        file.write("Dados extraídos da página de Wikipedia sobre Contabilidade:\n\n")
        
        for index, row in enumerate(dados):
            file.write(f"Conteúdo {index + 1}:\n")
            file.write(f"Título: {row[0]}\n")
            file.write(f"Introdução: {row[1]}\n")
            # Escreve os links internos como uma lista separada por vírgulas
            file.write(f"Links Internos: {', '.join(row[2])}\n")
            file.write("\n" + "-"*50 + "\n\n")

# Coletar os dados da página
dados = coletar_dados()

# Salvar os dados em formato de texto
salvar_em_texto(dados)

# Fechar o navegador após o processo
driver.quit()

print("Dados formatados foram salvos em 'dados_formatados.txt'.")

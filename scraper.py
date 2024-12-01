from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Caminho para o ChromeDriver (certifique-se de colocar o caminho correto)
driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver')  # Altere para o caminho correto do seu chromedriver

# URL do site de jurisprudência (substitua com o site real)
url = 'https://www.exemplo.com/jurisprudencia'
driver.get(url)

# Aguarde o carregamento dinâmico da página
driver.implicitly_wait(10)

# Função para extrair jurisprudência
def coletar_jurisprudencia():
    jurisprudencias = driver.find_elements(By.CLASS_NAME, 'jurisprudencia')
    data = []
    
    for jurisprudencia in jurisprudencias:
        try:
            titulo = jurisprudencia.find_element(By.TAG_NAME, 'h2').text
            resumo = jurisprudencia.find_element(By.TAG_NAME, 'p').text
            data.append([titulo, resumo])
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")
    
    return data

# Função para salvar os dados em um arquivo CSV
def salvar_em_csv(data):
    with open('jurisprudencia.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Título', 'Resumo'])  # Cabeçalho do CSV
        writer.writerows(data)

# Navegação entre páginas, se necessário
def navegar_entre_paginas():
    while True:
        print("Coletando dados da página atual...")
        data = coletar_jurisprudencia()
        salvar_em_csv(data)  # Salva os dados coletados até o momento
        
        # Tenta clicar na próxima página
        try:
            next_page = driver.find_element(By.LINK_TEXT, 'Próxima')
            next_page.click()
            time.sleep(3)  # Aguarde um pouco antes de continuar
        except Exception as e:
            print("Última página alcançada ou erro na navegação.")
            break

# Executando a coleta e navegação
navegar_entre_paginas()

# Encerrando o navegador
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# Iniciar o WebDriver (assumindo que o ChromeDriver está no PATH)
driver = webdriver.Chrome()

# Acesse o site
url = 'https://processo.stj.jus.br/SCON/pesquisar.jsp?preConsultaPP=&pesquisaAmigavel=+%3Cb%3Eprocesso%3C%2Fb%3E&acao=pesquisar&novaConsulta=true&i=1&b=ACOR&livre=processo&filtroPorOrgao=&filtroPorMinistro=&filtroPorNota=&data=&operador=e&thesaurus=JURIDICO&p=true&tp=T&processo=&classe=&uf=&relator=&dtpb=&dtpb1=&dtpb2=&dtde=&dtde1=&dtde2=&orgao=&ementa=&nota=&ref='
driver.get(url)

# Aguardar o carregamento da página
driver.implicitly_wait(10)

# Função para coletar os dados
def coletar_dados():
    # Listar os acórdãos exibidos na página
    acordaos = driver.find_elements(By.CLASS_NAME, 'item-jurisprudencia')

    dados = []
    
    for ac in acordaos:
        try:
            # Extrair informações relevantes: Processo, Relator, Data de Julgamento, Ementa
            processo = ac.find_element(By.CLASS_NAME, 'numeroProcesso').text
            relator = ac.find_element(By.CLASS_NAME, 'relator').text
            data_julgamento = ac.find_element(By.CLASS_NAME, 'dataJulgamento').text
            ementa = ac.find_element(By.CLASS_NAME, 'ementa').text
            
            dados.append([processo, relator, data_julgamento, ementa])
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")
    
    return dados

# Função para salvar em CSV
def salvar_em_csv(dados):
    with open('jurisprudencia.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Processo', 'Relator', 'Data de Julgamento', 'Ementa'])
        writer.writerows(dados)

# Coletar os dados da primeira página
dados = coletar_dados()

# Salvar os dados em um arquivo CSV
salvar_em_csv(dados)

# Caso haja múltiplas páginas, navegar para a próxima
while True:
    try:
        # Encontrar e clicar no link da próxima página
        next_page_button = driver.find_element(By.LINK_TEXT, 'Próxima')
        next_page_button.click()
        
        # Aguardar o carregamento da página
        time.sleep(3)
        
        # Coletar dados da nova página
        dados = coletar_dados()
        salvar_em_csv(dados)
    
    except Exception as e:
        print("Última página alcançada ou erro na navegação.")
        break

# Fechar o navegador após o processo
driver.quit()

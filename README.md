
# Web Scraper: Coletando Dados do Artigo sobre Contabilidade na Wikipedia

Este projeto utiliza o Selenium para realizar scraping da página de Contabilidade na Wikipedia. O script coleta o título do artigo, o primeiro parágrafo (introdução) e todos os links internos contidos no artigo, armazenando essas informações em um arquivo de texto para análise.

## Funcionalidades
- **Coleta do título da página**: Obtém o título principal do artigo sobre Contabilidade.
- **Coleta da introdução**: Extrai o primeiro parágrafo, que fornece uma visão geral do tema.
- **Coleta de links internos**: Obtém todos os links internos presentes no artigo, que levam a outros artigos relacionados dentro da Wikipedia.
- **Armazenamento em arquivo de texto**: Os dados coletados são armazenados de forma estruturada em um arquivo de texto (`dados_formatados.txt`).

## Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para escrever o script.
- **Selenium**: Ferramenta de automação de navegadores para realizar o scraping de dados da página web.
- **ChromeDriver**: Utilizado para controlar o navegador Chrome e realizar as ações de scraping.
- **Wikipedia**: O artigo de Contabilidade na Wikipedia serve como fonte de dados para este projeto.

## Como Rodar o Projeto

### Pré-requisitos
- **Instalar o Python**: Certifique-se de ter o Python instalado. Você pode baixar a versão mais recente no [site oficial do Python](https://www.python.org/downloads/).
- **Instalar o Selenium**: Você pode instalar o Selenium executando o seguinte comando:
  ```bash
  pip install selenium
  ```
- **Instalar o ChromeDriver**: O ChromeDriver é necessário para o Selenium controlar o navegador Chrome. Baixe a versão adequada para o seu sistema operacional e versão do Chrome em [ChromeDriver](https://sites.google.com/chromium.org/driver/).
  Após o download, extraia o arquivo e coloque o executável do ChromeDriver no `PATH` do seu sistema ou forneça o caminho completo ao inicializar o driver.

### Rodando o Script
1. Clone o repositório ou crie o arquivo do script: Crie um arquivo chamado `webscraper.py` e cole o código abaixo:
  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  import time

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
          file.write("Dados extraídos da página de Wikipedia sobre Contabilidade:

")
          
          for index, row in enumerate(dados):
              file.write(f"Conteúdo {index + 1}:
")
              file.write(f"Título: {row[0]}
")
              file.write(f"Introdução: {row[1]}
")
              # Escreve os links internos como uma lista separada por vírgulas
              file.write(f"Links Internos: {', '.join(row[2])}
")
              file.write("
" + "-"*50 + "

")

  # Coletar os dados da página
  dados = coletar_dados()

  # Salvar os dados em formato de texto
  salvar_em_texto(dados)

  # Fechar o navegador após o processo
  driver.quit()

  print("Dados formatados foram salvos em 'dados_formatados.txt'.")
  ```

2. Execute o script:
  No terminal, execute o seguinte comando:
  ```bash
  python webscraper.py
  ```

### Verifique o Arquivo de Saída
Após a execução do script, os dados coletados serão salvos em um arquivo chamado `dados_formatados.txt`. O conteúdo do arquivo será estruturado da seguinte forma:

```txt
Dados extraídos da página de Wikipedia sobre Contabilidade:

Conteúdo 1:
Título: Contabilidade
Introdução: A contabilidade é a ciência que estuda, analisa e controla o patrimônio de uma entidade.
Links Internos: https://pt.wikipedia.org/wiki/Contabilidade, https://pt.wikipedia.org/wiki/Patrim%C3%B4nio, ...

------------------------------------------------------
```

## Considerações Finais
Este projeto é uma implementação simples de Web Scraping usando o Selenium. Ele pode ser expandido para incluir mais funcionalidades, como extração de mais conteúdo ou salvar os dados em diferentes formatos (como CSV ou JSON). A página de Wikipedia usada como exemplo pode ser substituída por outras, caso necessário.

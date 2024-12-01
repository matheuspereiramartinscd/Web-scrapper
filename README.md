
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
1. Clone o repositório

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

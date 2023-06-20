# API de Cotação
# Funcionalidade - Retornar valores diários de abertura/máxima/baixa/fechamento/volume brutos e valores diários de fechamento ajustados
# Funcionalidade - Por padrão outputsize=compact, portanto serão inseridos os 100 últimos valores diários da cotação na tabela criada.
# API Utilizada - https://www.alphavantage.co/documentation/

import pandas as pd
import requests
from io import StringIO

chave_api = 'BU9AAZ0KJ8FTNA0T'

# Requisição inicial da cotação do Itaú - ITUB4.SAO
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=ITUB4.SAO&apikey={chave_api}&datatype=csv'
r = requests.get(url)
# Transformação do texto em um arquivo com StringIO para que ele possa ser lido e armazenado como CSV na variável tabela
tabela = pd.read_csv(StringIO(r.text))
print(tabela)

# Selecionando ações do Itaú, Ambev e Banco do Brasil
acoes = ['ITUB4', 'ABEV3', 'BBAS3']

# Criação de uma tabela vazia para armazenar os dados
compilada = pd.DataFrame()

for acao in acoes:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={acao}.SAO&apikey={chave_api}&datatype=csv'
    r = requests.get(url)
    tabela = pd.read_csv(StringIO(r.text))
    lista_tabelas = [compilada, tabela]
    compilada = pd.concat(lista_tabelas)
        
print(compilada)
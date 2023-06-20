# API de Pesquisa de Endpoint
# Funcionalidade - Retornar simbologia correta na Bolsa de Valores de acordo com a empresa/simbologia apresentada inicialmente pelo usuário
# API Utilizada - https://www.alphavantage.co/documentation/

import pandas as pd
import requests
from io import StringIO

chave_api = 'BU9AAZ0KJ8FTNA0T'

# Solicitar ao usuário qual símbolo/empresa ele deseja pesquisar

def pesquisa_usuario():
    resposta_usuario = input(str('Qual símbolo ou empresa você deseja pesquisar? '))
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={resposta_usuario}&apikey={chave_api}&datatype=csv'
    requisicao = requests.get(url)
    tabela = pd.read_csv(StringIO(requisicao.text))
    print(tabela)

pesquisa_usuario()
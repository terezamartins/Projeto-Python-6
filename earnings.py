# API de Ganhos
# Funcionalidade - Essa API retorna os ganhos anuais e trimestrais (EarningPerShare) da empresa de interesse. Os dados trimestrais também incluem estimativas de analistas e métricas surpresa.
# OBS: Funcionalidade disponível apenas para empresas internacionais por não ser adicionado o .SAO na requisição
# API Utilizada - https://www.alphavantage.co/documentation/
import pandas as pd
import requests
from io import StringIO
import pprint

chave_api = 'BU9AAZ0KJ8FTNA0T'

def pesquisa_usuario():
    resposta_usuario = input(str('Qual símbolo ou empresa você deseja pesquisar? '))
    tipo_ganho = input(str('Qual tipo de ganho gostaria de visualizar?\n[1] Ganhos anuais (Annual Earnings)\n[2] Ganhos trimestrais (Quarterly earnings)\nEscolha a sua opção: '))
    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={resposta_usuario}&apikey={chave_api}'
    r = requests.get(url)
    data = r.json()
    # pprint.pprint(data)
    if tipo_ganho == '1':
        resultado1 = pd.DataFrame(data['annualEarnings'])
        pprint.pprint(resultado1)
    elif tipo_ganho == '2':
        resultado2 = pd.DataFrame(data['quarterlyEarnings'])
        pprint.pprint(resultado2)
    else:
        print('O tipo de ganho especificado não condiz com as opções listadas. Tente novamente.')

pesquisa_usuario()

#resultado = pd.DataFrame(data['annualEarnings'])
#print(resultado)
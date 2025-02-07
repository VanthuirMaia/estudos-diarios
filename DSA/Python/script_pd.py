import pandas as pd

# Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

from pandas import DataFrame

df = DataFrame(dados)

df_novo = pd.DataFrame(dados, columns=['Estado', 'Taxa Desemprego', 'Ano'])
print(df_novo.head())
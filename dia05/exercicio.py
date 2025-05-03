#Selecione a primeira transação de cada cliente no dia
# %%

import pandas as pd
transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.head()

# %%

transacoes['dtCriacao'] = pd.to_datetime(transacoes['dtCriacao'])

# %%

transacoes['dataTransacao'] = transacoes['dtCriacao'].dt.date
transacoes_diarias = (transacoes.sort_values(by='dtCriacao',ascending=True)
                      .drop_duplicates(['idCliente','dataTransacao'],keep='first'))

# %%

transacoes

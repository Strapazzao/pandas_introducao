#%%
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%
#filtro unico
filtro = df['qtdePontos'] >= 50
df[filtro]
#ou
#df[df['qtdePontos'] >= 20]

# %%
#filtro utilizando "and"
filtro_composto = (df['qtdePontos'] >= 50) & (df['qtdePontos'] <= 100)
df[filtro_composto]

# %%
#filtro utilizando "or"
filtro_composto = (df['qtdePontos'] == 1) | (df['qtdePontos'] <= 100)
df[filtro_composto]

# %%
#utilizando "or" e "and" ao mesmo tempo
filtro_composto = (df['qtdePontos'] >= 50) & (df['qtdePontos'] <= 100) | (df['dtCriacao']>= '2025-01-01')
df[filtro_composto]
#dessa forma o pandas sempre faz primeiro as cláusulas do "and", para depois fazer o "or", para colocar or como cláusula primária,
# é necessário colocar entre ()
# filtro_composto = (df['qtdePontos'] >= 50) & ((df['qtdePontos'] <= 100) | (df['dtCriacao']>= '2025-01-01'))
# dessa forma o pandas verifica se pontos <=100 ou criado depois de 2025-01-01, necessitando ter mais de 50 pontos

# %%

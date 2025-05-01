#%%
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%
df.info(memory_usage='deep')

# %%
df.dtypes

# %%
df = df.rename(columns={"qtdePontos":"qtPontos",'descSistemaOrigem':'sistemaOrigem'}) #dicionario possui a chave de como era o nome da coluna, e o valor da chave vai ser o nome nome
df.dtypes

# %%
df['idCliente']


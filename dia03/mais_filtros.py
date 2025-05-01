# %%
import pandas as pd

# %%
df = pd.read_csv("../data/transacao_produto.csv")
# %%
filtro = (df['idProduto'] == 5) | (df['idProduto'] == 11)
df[filtro]

# %%
#outra forma de fazer a mesma coisa
filtro = df['idProduto'].isin([5,11])
df[filtro]
# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.info() #possui valores nulos
# %%
filtro = clientes['dtCriacao'].notna()
clientes[filtro]

# %%
#algumas vezes queremos a negação de um filtro
~clientes['dtCriacao'].notna()
#isso é a mesma coisa que 
clientes['dtCriacao'].isna()
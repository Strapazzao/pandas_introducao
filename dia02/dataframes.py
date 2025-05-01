#%%
import pandas as pd

# %%
df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes.head() #5 primeiros


# %%
df_clientes.tail() #5 últimos

# %%
df_clientes.sample(5) #aleatórios


# %%
df_clientes.shape #atributo que retorna a dimensão linhas/colunas do df

# %%
df_clientes.columns #atributo que retorna o nome das colunas

# %%
df_clientes.index #atributo que retorna o indice (vai de 0 a 2435)

# %%
df_clientes.info(memory_usage='deep') #informações do df

# %%
df_clientes.dtypes #isso é uma série
df_clientes.dtypes['idCliente'] #tipo object
# %%

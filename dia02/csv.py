#%%
import pandas as pd
# %%
#para ler
df = pd.read_csv('../data/clientes.csv')
df.head()
# %%
#para salvar
df.to_parquet('../data/clientes.parquet',index=False)
# %%
#para experimentos
df = pd.read_clipboard()
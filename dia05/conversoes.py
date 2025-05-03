#%%
import pandas as pd
# %%
df = pd.read_csv("../data/clientes.csv")

# %%
#transforma do tipo int para float 
df['qtdePontos'].astype(float)

# %%
#transforma do tipo int para float para depois transformar em string
df['qtdePontos'].astype(float).astype(str)

# %%
#da erro, pois existe o valor 0000-00-00 00:00:00.000 que não pode virar data
pd.to_datetime(df['dtCriacao'])

# %%
df['dtCriacao'].replace({
    '0000-00-00 00:00:00.000':'2025-03-01 09:00:00.000'
    })

#%%
import pandas as pd
# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs
# %%
df_uf = dfs[1]
# %%
df_uf
# %%
df_uf.to_csv('../data/df_uf.csv',index=False)
# %%

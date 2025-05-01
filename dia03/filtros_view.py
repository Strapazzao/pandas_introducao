#%%
import pandas as pd

# %%
cliente = pd.read_csv("../data/clientes.csv")
cliente.head()

filtro = cliente['qtdePontos'] == 0
clientes_0 = cliente[filtro]
clientes_0['flag_1'] = 1
#dessa forma o pandas apresenta uma mensagem de aviso, pois o pandas não cria outro df para fazer o filtro,
# ele apenas cria uma visualização para poupar memória.
# para realizar a operação corretamente e evitar qualquer falha é necessário realizar uma cópia do df

# %%
filtro = cliente['qtdePontos'] == 0
clientes_0 = cliente[filtro].copy()
clientes_0['flag_1'] = 1
clientes_0
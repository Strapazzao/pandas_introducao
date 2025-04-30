#%%
import pandas as pd

# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]
series_idades = pd.Series(idades)
series_idades
#series é a astrutura básica do pandas, é formada pelo índice e o valor
# %%
#acessando valores via indice
print(f'primeiro valor {series_idades[0]}')
print(f'último valor {series_idades[14]}')
#não existe índice -1
# %%
#mesmo ordenando a serie, o índice se mantém o mesmo de quando foi criado
series_idades = series_idades.sort_values()
print(series_idades)
print(f'idade com o index 0 {series_idades[0]}')
print(f'idade com o index 14 {series_idades[14]}')
# %%
#para pegar o primeiro valor por ordenação, é preciso utilziar o atributo iloc[]
print(series_idades)
print(f'idade na linha 0 {series_idades.iloc[0]}')
print(f'idade na linha 14 {series_idades.iloc[14]}')
# %%
indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "André", "André",
]

series_idades = pd.Series(idades,index=indexs)
series_idades
# %%
#agora os índices não são mais números,são nomes
print(series_idades)
print(f'idade no index Téo {series_idades["Téo"]}')
print(f'idade no index Nih {series_idades["Nih"]}')
# %%
#é possivel ter mais de um index
print('idade nos indexs André')
print(series_idades["André"])
# %%
#iloc[] é para navegar nas linhas, loc[] é para navegar no indice, ná serie não faz diferença usar loc
print(series_idades["Téo"])
print(series_idades.loc["Téo"])
# %%

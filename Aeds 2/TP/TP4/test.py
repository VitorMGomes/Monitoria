import pandas as pd


df = pd.read_csv("games.csv")

colunas_com_nulos = df.columns[df.isnull().any()].tolist()

print("Colunas com valores ausentes:", colunas_com_nulos)


print(df.dtypes)
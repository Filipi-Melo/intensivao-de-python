import pandas as pd
from plotly.express import histogram

tabela = pd.read_csv("./telecom_users.csv")
print(tabela)

tabela = tabela.drop("Unnamed: 0",axis=1)
tabela.info()

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")
tabela = tabela.dropna(how="all",axis=1).dropna(how="any",axis=0)
tabela.info()

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True))

for coluna in tabela.columns:
    grafico = histogram(tabela, x=coluna, color="Churn",text_auto=True)
    grafico.show()
input('')
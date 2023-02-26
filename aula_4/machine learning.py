import pandas as pd, seaborn as sn, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

tabela = pd.read_csv("./advertising.csv")

print("Tabela:\n",tabela)
print("\nInformação:\n")
tabela.info()
print("\nCorrelação:\n",tabela.corr())

sn.heatmap(tabela.corr(),cmap="Wistia",annot=True)

x,y = tabela[["TV","Radio","Jornal"]], tabela["Vendas"]

xtreino, xteste, ytreino, yteste=train_test_split(x,y,test_size=0.3)

reglinear,arvoredecisao = LinearRegression(), RandomForestRegressor()

reglinear.fit(xtreino,ytreino)
arvoredecisao.fit(xtreino,ytreino)

previsao1, previsao2 = arvoredecisao.predict(xteste), reglinear.predict(xteste) 

print("\nPontos:")
print("- Arvore de decisão:",r2_score(yteste,previsao1)*100,'%')
print("- Regressão linear:",r2_score(yteste,previsao2)*100,'%')

tabela2 = pd.DataFrame()
tabela2['yteste'] = yteste
tabela2['arvore de decisão']=previsao1
tabela2['regressão linear']=previsao2

print("\nGrafico:\n")
plt.figure(figsize=(15,5))
sn.lineplot(data=tabela2)

tabelanova = pd.read_csv('./novos.csv')
print("Tabela Nova:\n",tabelanova)
print('Predição:',arvoredecisao.predict(tabelanova))

plt.show()
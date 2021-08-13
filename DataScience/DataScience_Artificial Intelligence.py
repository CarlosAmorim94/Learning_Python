#Nosso objetivo é criar um modelo de previsão de vendas a partir do histórico de vendas e investimento em marketing sobre TV, Rádio e Jornal.

# Passo 1 - Importar dados

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #Sempre que importa o seaborn, devemos importar o matplotlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import  metrics

tabela = pd.read_csv('advertising.csv')

# Passo 2 - Análise exploratória
#Vamos tentar visualizar como as informações de cada item estão distribuídas
#Vamos ver a correlação entre cada um dos itens

sns.heatmap(tabela.corr(), cmap="Wistia", annot=True) #Tabela de correlação (cmap="wistia" é cor dos gráficos)(annot=True mostra os números de correlação)
plt.show()

# Passo 3 - Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# Separando em dados de treino e dados de teste"
#Separar as informações em X e Y (Y é quem queremos descobrir, X é o restp)
y = tabela['Vendas']
x = tabela.drop('Vendas', axis=1) #axis=1 é coluna, axis=0 é linha

#Aplicar train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)


# Passo 4 - # Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# Regressão Linear
# RandomForest (Árvore de Decisão)

modelo_regressao_linear = LinearRegression()
modelo_randomforest = RandomForestRegressor()

modelo_regressao_linear.fit(x_train, y_train)
modelo_randomforest.fit(x_train, y_train)

# Passo 5 - Teste da AI e Avaliação do Melhor Modelo
# Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece"

previsao_regressaolinear = modelo_regressao_linear.predict(x_test)
previsao_randomforest = modelo_randomforest.predict(x_test)

print(metrics.r2_score(y_test, previsao_regressaolinear))
print(metrics.r2_score(y_test, previsao_randomforest))

# Passo 6 - Visualização Gráfica das Previsões

#Previsão vencedora é randomforest

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_test'] = y_test
tabela_auxiliar['Regressao linear'] = previsao_regressaolinear
tabela_auxiliar['Random Forest'] = previsao_randomforest

plt.figure(figsize=(15,5))
sns.lineplot(data=tabela_auxiliar)
plt.show()

sns.barplot(x=x_train.columns, y= modelo_randomforest.feature_importances_)
plt.show()


# Passo 7 - Qual a importância de cada variável para as vendas?



#Como fazer uma nova previsão?
#importar uma nova tabela com pandas e rodas a previsão
#previsao = modelo_randomforest.predict(nova_tabela)
#Situação:
#Analisando o histórico dos clientes dos últimos anos, você percebeu que mais de 26% dos clientes que entraram na empresa, cancelaram o contrato.
# A única informação que você tem é um arquivo .csv extraído do sistema da empresa

#Resolução:
#Passo 1: Importar base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')

#Passo 2: Visualizar base de dados
#Entender quais informações vc tem disponível... Descobrir os erros da base de dados

print(tabela.info()) #Verificar as informações da tabela

#Passo 3: Tratamento da base de dados
# Valores que são numeros, mas que o python acha que são textos...
# Valores vazios...
# Excluir informações inúteis
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce") #Transformar a coluna string em numeros
tabela = tabela.drop(["Unnamed: 0", "IDCliente"] , axis=1) #Deletar colunas "inúteis"
#tabela = tabela.drop("IDCliente", axis=1)   #Deletar colunas "inúteis"
tabela = tabela.dropna(how="all" , axis=1) #(how=all = Colunas COMPLETAMENTE  vazias) ... (how=any = colunas com pleo menos 1 valor vazio)
tabela = tabela.dropna(how="any" , axis=0) #(axis=1 = colunas) .... (axis=0 = linhas)
print(tabela.info())

#Passo 4: Análise exploratória (Análise geral)

print(tabela["Churn"].value_counts())                   #Contagem de "Churns" (desistencias)
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) #Formatando em percentual

#Passo 5: Olhando a bade de dados, vamos tentar identificar o motivo do cancelamento

coluna = "FormaPagamento"
grafico = px.histogram(tabela, x=coluna, color="Churn")
grafico.show()


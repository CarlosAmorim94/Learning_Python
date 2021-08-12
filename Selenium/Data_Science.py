# Passo 1 - Entrar na internet

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import plotly.express as px

navegador = webdriver.Chrome()

# Passo 2 - Pegar cotação do dolar
#entrar no google
navegador.get('https://www.google.com/')
#Pegar cotação do Dollar
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dollar") #(.send_keys = Digitar textos) e (.click = clicar)
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#Pegar o número da conversão
cotacaoDolar = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

# Passo 3 - Pegar cotação do euro
#entrar no google
navegador.get('https://www.google.com/')
#Pegar cotação do Euro
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro") #(.send_keys = Digitar textos) e (.click = clicar)
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#Pegar o número da conversão
cotacaoEuro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") #.get_attribute = imformação que vc quer coletar do Xpath)


# Passo 4 - Pegar cotação do ouro
#entrar no site do Melhor Cambio
navegador.get('https://www.melhorcambio.com/ouro-hoje')
#Pegar cotação do Ouro
cotacaoOuro = navegador.find_element_by_xpath('//*[@id="comercial"]').get_attribute("value") #.get_attribute = imformação que vc quer coletar do Xpath)
navegador.quit() #Fechar o navegador

cotacaoOuro = cotacaoOuro.replace(",",".")

print(cotacaoDolar)
print(cotacaoEuro)
print(cotacaoOuro)

# Passo 5 - Importar e atualizar a base de dados

tabela = pd.read_excel('Produtos.xlsx')
print(tabela)

#atualizar cotação
# onde a coluna moeda é igual a dolar

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacaoDolar) #.loc = filtrar e alterar
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacaoEuro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacaoOuro)

print(tabela)
#Atualizar preço de compra = preço de base original * cotação
tabela["Preço de Compra"] = tabela["Preço Base Original"] * tabela["Cotação"]
#Atualizar preço de venda = preço de cmpral * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
#formatando para 2 casas após o ponto
tabela["Preço de Venda"] = tabela["Preço de Venda"].map("{:.2f}".format)

print(tabela)


#Exportar a bade de dados atualizada

tabela.to_excel("Produtos - Resultado Final.xlsx", index=False) #Index=False = Não adiciona a primeira coluna de numeros
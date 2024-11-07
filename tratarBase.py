import pandas as pd


# Carregar o arquivo CSV
dfCell = pd.read_csv("bd/base_dados_smartphones.csv")


#Retorna as marcas em fomato de lista
def mostrar_marcas():
    marcas = dfCell["marca"].tolist()
    return marcas

#Retorna o preço em fomato de lista
def mostrar_preco():
    preco = dfCell["preco"].tolist()
    return preco

#Retorna as avaliações em fomato de lista
def mostrar_avaliacao():
    avaliacoes = dfCell["avaliacao"].tolist()
    return avaliacoes

#Retorna as vendas em fomato de lista
def mostrar_vendas():
    vendas = dfCell["vendas"].tolist()
    return vendas

def modelos(marca):
    modelos = dfCell[dfCell["marca"] == f"{marca}"]["modelo"].unique().tolist()
    return modelos
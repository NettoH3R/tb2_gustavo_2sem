import gradio as gr
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Dados fictícios de exemplo para as marcas, preços e avaliações
marcas = ["Samsung", "Motorola", "Apple", "Xiaomi", "POCO"]
precos = [1500, 1200, 3000, 900, 700, 1600, 2000, 2500, 3500, 800]
avaliacoes = [4.5, 4.0, 5.0, 3.5, 4.2, 3.8, 4.9, 3.0, 5.0, 2.5]

# Quantidade de vendas simulada para treinar o modelo
vendas = [200, 150, 250, 120, 100, 180, 220, 160, 270, 90]



# TEMOS QUE ARRUMAR A LÓGICA DESSA PARTE  ||
#                                        _||_
#                                        \  /
#                                         \/

# Transformando a variável categórica (marcas) em valores numéricos
encoder = LabelEncoder()
marcas_encoded = encoder.fit_transform(marcas * 2)  # Multiplicando para igualar o tamanho dos dados fictícios

# Preparando os dados de entrada
X = np.array(list(zip(marcas_encoded, precos, avaliacoes)))
y = np.array(vendas)

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)

# Função de previsão
def prever_vendas(marca, preco, avaliacao):
    # Transformando a marca em valor numérico
    marca_encoded = encoder.transform([marca])[0]
    # Criando a entrada para o modelo
    entrada = np.array([[marca_encoded, preco, avaliacao]])
    # Fazendo a previsão
    previsao = modelo.predict(entrada)
    return f"Previsão de vendas: {round(previsao[0],0): .0f} unidades"

# Configurando a interface Gradio
interface = gr.Interface(
    fn=prever_vendas,
    inputs=[
        gr.Dropdown(choices=marcas, label="Marca do Celular"),
        gr.Number(label="Preço do Celular (em R$)", value=1500),  # Change 'default' to 'value'
        gr.Slider(minimum=1, maximum=5, step=0.1, label="Avaliação do Cliente"),
    ],
    outputs="text",
    title="Previsão de Vendas de Celulares",
    description="Insira a marca, o preço e a avaliação do cliente para prever as vendas.",
)

# Executando a aplicação Gradio
interface.launch()
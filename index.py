import gradio as gr
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from tratarBase import *

# Dados fictícios de exemplo para as marcas, preços e avaliações
marcas = mostrar_marcas()
precos = mostrar_preco()
avaliacoes = mostrar_avaliacao()

# Quantidade de vendas simulada para treinar o modelo
vendas = mostrar_vendas()

marcasNoRepet = set(marcas)


# Transformando a variável categórica (marcas) em valores numéricos
encoder = LabelEncoder()
marcas_encoded = encoder.fit_transform(marcas)  

# Preparando os dados de entrada
X = np.array(list(zip(marcas_encoded, precos, avaliacoes)))
y = np.array(vendas)

# Treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X, y)



def encontrar_modelos(marca, preco, avaliacao):
    # Criar lista de modelos que correspondem à marca
    modelos_disponiveis = modelos(marca)

    # Filtrando os modelos com base no preço e avaliação mais próximos
    precos_disponiveis = mostrar_preco()
    avaliacoes_disponiveis = mostrar_avaliacao()

    
    # Aqui podemos comparar o preço e a avaliação, retornando os modelos mais próximos
    modelos_proximos = []
    for i, modelo in enumerate(modelos_disponiveis):
        if abs(preco - precos_disponiveis[i]) <= 1000 and abs(avaliacao - avaliacoes_disponiveis[i]) <= 0.3:
            modelos_proximos.append(modelo)
    
    return modelos_proximos



# Função de previsão
def prever_vendas(marca, preco, avaliacao):
    # Transformando a marca em valor numérico
    marca_encoded = encoder.transform([marca])[0]
    # Criando a entrada para o modelo
    entrada = np.array([[marca_encoded, preco, avaliacao]])
    # Fazendo a previsão
    previsao = modelo.predict(entrada)

    # Encontrar os modelos correspondentes
    modelos_correspondentes = encontrar_modelos(marca, preco, avaliacao)

    if round(previsao[0],0) >= 0:
        modelos_str = ", ".join(modelos_correspondentes)
        resposta = f"Modelos que podem se encaixar no padrão sugerido:\n {modelos_str }"

        return f"Previsão de vendas: {round(previsao[0],0): .0f}\n\n " + resposta	
    else:
        return f"Previsão de vendas: 0 unidades"



# Configurando a interface Gradio
interface = gr.Interface(
    fn=prever_vendas,
    inputs=[
        gr.Dropdown(choices=marcasNoRepet, label="Marca do Celular"),
        gr.Number(label="Preço do Celular (em R$)", value=1500),  # Change 'default' to 'value'
        gr.Slider(minimum=1, maximum=5, step=0.1, label="Avaliação do Cliente"),
    ],
    outputs="text",
    title="Previsão de Vendas de Celulares",
    description="Insira a marca, o preço e a avaliação do cliente para prever as vendas.",
)

# Executando a aplicação Gradio
interface.launch()
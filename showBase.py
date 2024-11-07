import pandas as pd
import gradio as gr

# Carregar o arquivo CSV
dfCell = pd.read_csv("bd/base_dados_smartphones.csv")

# Função para exibir o conteúdo do DataFrame
def mostrar_dados():
    return dfCell[["modelo", "marca"]].groupby("marca")["modelo"].apply(list).reset_index()

# Criar a interface Gradio
interface = gr.Interface(
    fn=mostrar_dados,
    inputs=None,
    outputs="dataframe",
    title="Base de Dados de Smartphones",
    description="Visualize os dados de smartphones, incluindo marca, modelo, preço, avaliação e vendas."
)

# Executar a interface
interface.launch()
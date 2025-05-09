from shiny import App, Inputs, Outputs, Session, reactive, ui, render
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Definindo o layout da aplicação
app_ui = ui.page_fluid(
    ui.h2("Minha Aplicação Shiny em Python"),
    
    # Layout com sidebar em vez de layout_sidebar
    ui.row(
        ui.column(4,
            ui.card(
                ui.card_header("Controles"),
                ui.input_slider("n", "Número de observações", 1, 100, 20),
                ui.input_select(
                    "tipo_grafico", 
                    "Tipo de gráfico", 
                    {"barras": "Gráfico de Barras", "linha": "Gráfico de Linha", "pizza": "Gráfico de Pizza"}
                ),
                ui.input_checkbox_group(
                    "opcoes",
                    "Opções",
                    {
                        "mostrar_dados": "Mostrar dados brutos",
                        "mostrar_estatisticas": "Mostrar estatísticas"
                    }
                ),
                ui.br(),
                ui.download_button("download_dados", "Baixar dados")
            )
        ),
        ui.column(8,
            ui.card(
                ui.card_header("Visualização"),
                ui.output_plot("grafico")
            ),
            ui.panel_conditional(
                "input.opcoes.includes('mostrar_dados')",
                ui.card(
                    ui.card_header("Dados"),
                    ui.output_table("tabela")
                )
            ),
            ui.panel_conditional(
                "input.opcoes.includes('mostrar_estatisticas')",
                ui.card(
                    ui.card_header("Estatísticas"),
                    ui.output_ui("estatisticas")
                )
            )
        )
    )
)

# Definindo a lógica do servidor
def server(input: Inputs, output: Outputs, session: Session):
    # Gerar dados de exemplo baseados no input
    @reactive.calc
    def dados():
        n = input.n()
        return pd.DataFrame({
            "x": range(1, n + 1),
            "y": range(n, 0, -1),
            "grupo": [f"Grupo {i % 5 + 1}" for i in range(n)]
        })
    
    # Renderizar o gráfico
    @output
    @render.plot
    def grafico():
        df = dados()
        tipo = input.tipo_grafico()
        
        if tipo == "barras":
            return px.bar(df, x="x", y="y", color="grupo")
        elif tipo == "linha":
            return px.line(df, x="x", y="y", color="grupo")
        elif tipo == "pizza":
            return px.pie(df, values="y", names="grupo")
    
    # Renderizar a tabela
    @output
    @render.table
    def tabela():
        return dados()
    
    # Renderizar estatísticas
    @output
    @render.ui
    def estatisticas():
        df = dados()
        stats = df.describe()
        
        return ui.HTML(f"""
        <div class="estatisticas">
            <p><strong>Média:</strong> {stats.loc['mean', 'y']:.2f}</p>
            <p><strong>Mediana:</strong> {df['y'].median():.2f}</p>
            <p><strong>Desvio Padrão:</strong> {stats.loc['std', 'y']:.2f}</p>
            <p><strong>Mínimo:</strong> {stats.loc['min', 'y']}</p>
            <p><strong>Máximo:</strong> {stats.loc['max', 'y']}</p>
        </div>
        """)
    
    # Download de dados
    @session.download
    def download_dados():
        return {"filename": "dados.csv", "content": dados().to_csv(index=False)}

# Criar a aplicação
app = App(app_ui, server)
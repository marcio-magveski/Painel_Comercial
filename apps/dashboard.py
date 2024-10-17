import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
import pandas as pd
import locale
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from app import app


# Definir a localidade para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Incorporate data
df = pd.read_excel(r"C:\Users\marciobarros\OneDrive - Unimed Vitória\MARCIO\dash\dataset\Tabela_Vendas.xlsx")


layout = html.Div([

    # Navbar para navegação entre páginas
    
    # Título do Dashboard
        html.Div(className='title-container', children=[
            html.H1("Dashboard de Vendas", className='title'),
            dcc.Dropdown(
        id='drop-1',
        options=[{'label': continente, 'value': continente} for continente in df['Continente'].unique()],
        placeholder="Selecione o Continente",
       
        className='dropdown'  # Define largura e exibição inline
    ),
        dcc.Dropdown(
            id='drop-2',
            options=[{'label': ano, 'value': ano} for ano in df['Ano'].unique()],  # Corrigido para 'ano'
            placeholder="Selecione o Ano",
      
            className='dropdown-second'  # Adiciona a classe para o espaço
        )
    ]),

    # Row para os cards
    dbc.Row([
        dbc.Col(
            html.Div(className='card', children=[
                html.H3("Receita Total", className='card-title'),
                # html.P(receita_total_str, className='card-value') 
                html.P(id='receita-output', className='card-value')
            ]),
            width=3
        ),
        dbc.Col(
            html.Div(className='card', children=[
                html.H3("Custo Total", className='card-title'),
                # html.P(custo_total_str, className='card-value')  
                 html.P(id='custo-output', className='card-value') 
            ]),
            width=3
        ),
        dbc.Col(
            html.Div(className='card', children=[
                html.H3("Lucro Total",className='card-title'),
                html.P(id='lucro-output', className='card-value')
            ]),
            width=3
        ),

       dbc.Col(
        html.Div(className='card', children=[
            html.H3("Margem Lucro",className='card-title'),
            html.P(id='margem-output', className='card-value')
        ]),
        width=3
        ),
    ]),


    # Segunda Linha

    dbc.Row([

                dbc.Col(
                    dcc.Graph(id='grafico-receita', className='grafico'),
                    width=6,
                    class_name='col-grafico'
                    
                ),
                dbc.Col(
                    dcc.Graph(id='grafico-receita-pais', className='grafico'),
                    width=6,
                    class_name='col-grafico'
                    
                ),

             
             ]),



#terceira linha
    dbc.Row([

                dbc.Col(
                    dcc.Graph(id='grafico3_1', className='grafico'),
                    width=4,
                    class_name='col-grafico'
                    
                ),
               dbc.Col(
                    dcc.Graph(id='grafico3_2', className='grafico'),
                    width=4,
                    class_name='col-grafico'
                    
                ),

                dbc.Col(
                    dcc.Graph(id='grafico3_3', className='grafico'),
                    width=4,
                    class_name='col-grafico'
                    
                ),

             
             ])


], className="layout-container")






def create_revenue_graph(df):
    # Agrupar por mês e somar a Receita Total
    monthly_revenue = df.groupby(['Nome do Mês', 'Numero_Mes'])['Receita_Total'].sum().reset_index()

    # Ordenar o DataFrame pela coluna 'Numero_Mes' para garantir a ordem correta dos meses
    monthly_revenue = monthly_revenue.sort_values('Numero_Mes')



    # Criar o gráfico de linha
    fig = px.line(monthly_revenue, x='Nome do Mês', y='Receita_Total', 
                  title='Receita Total por Mês (em milhar)',
                  labels={'Nome do Mês': 'Nome do Mês', 'Receita_Total': 'Receita Total (R$ mil)'}, 
                  markers=True)

    # Personalizar o layout do gráfico
    fig.update_layout(
        yaxis_title='Receita Total (R$ mil)',
        xaxis_title='Nome do Mês',
        xaxis_tickmode='array',
        xaxis_tickvals=monthly_revenue['Nome do Mês'],
        margin=dict(l=20, r=20, t=40, b=20),
    
    )
     #Ajustar a cor da linha
    fig.update_traces(line=dict(color='#00995d'), line_shape='spline')  # Substitua 'red' pela cor deseja
    
    return fig



def create_revenue_bar_chart(df):
    # Agrupar por País e somar a Receita Total
    revenue_by_country = df.groupby('País')['Receita_Total'].sum().reset_index()
    
    # Ordenar pela Receita Total em ordem decrescente
    revenue_by_country = revenue_by_country.sort_values(by='Receita_Total', ascending=False)

    # Formatar a coluna 'Receita_Total' para exibir duas casas decimais
    revenue_by_country['Receita_Total'] = revenue_by_country['Receita_Total'].apply(lambda x: f"{x:,.2f}")

    # Criar o gráfico de barras
    fig1 = px.bar(
        revenue_by_country,
        x='País',
        y='Receita_Total',
        title='Receita Total por País',
        text='Receita_Total',  # Mostrar os valores nas barras
    )

    # Definir a cor das barras
    fig1.update_traces(marker_color='#00995d')  # Altere 'blue' para a cor desejada

    # Ajustar a ordem dos países no eixo x
    fig1.update_xaxes(categoryorder='total descending')  # Ordenar pelo total da receita em ordem decrescente

    # Personalizar o layout do gráfico
    fig1.update_layout(
        yaxis_title='',  # Remove o rótulo do eixo Y
        xaxis_title='País',
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',  # Remove o fundo do gráfico
        paper_bgcolor='rgba(0,0,0,0)'  # Remove o fundo da área ao redor do gráfico
    )


    
    # Remover os números do eixo Y
    fig1.update_yaxes(showticklabels=False)  # Oculta os rótulos do eixo Y
    # Usar escala logarítmica no eixo Y
    fig1.update_yaxes(type='log')

    return fig1






##########FUNIL############

import plotly.express as px

def create_profit_funnel(df):
    # Calcular o Lucro
    df['Lucro'] = df['Receita_Total'] - df['Custo_Total']

    # Agrupar por Continente e somar o Lucro
    profit_by_continent = df.groupby('Continente')['Lucro'].sum().reset_index()


    # Classificar os continentes pelo Lucro em ordem decrescente
    profit_by_continent = profit_by_continent.sort_values(by='Lucro', ascending=False)

    # Criar o gráfico de funil
    fig2 = px.funnel(
        profit_by_continent,
        x='Lucro',
        y='Continente',
        title='Lucro por Continente',
        labels={'Lucro': 'Lucro (R$)', 'Continente': 'Continente'},
    )

     # Definir cores personalizadas (por exemplo, uma lista de cores)
    colors = ['#00995d',  '#bcbd22','#7f7f7f',  '#8c564b','#2ca02c', '#d62728', '#9467bd', '#e377c2',  '#17becf']

    # Atualizar as cores do gráfico
    fig2.update_traces(marker=dict(color=colors))

    # Personalizar o layout do gráfico
    fig2.update_layout(
        yaxis_title='Continente',
        xaxis_title='Lucro (R$)',
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',  # Remove o fundo do gráfico
        paper_bgcolor='rgba(0,0,0,0)'  # Remove o fundo da área ao redor do gráfico
    )

    return fig2




def create_revenue_pie_chart(df):
    # Agrupar por Marca e somar a Receita Total
    revenue_by_brand = df.groupby('Marca')['Receita_Total'].sum().reset_index()
    
    # Criar o gráfico de pizza
    fig_pizza = px.pie(
        revenue_by_brand,
        names='Marca',
        values='Receita_Total',
        title='Receita Total por Marca',
        color='Marca',  # Colorir as fatias por Marca
        hole=0.3  # Criar um gráfico de pizza com um buraco no meio (gráfico de rosquinha)
    )

    # Personalizar o layout do gráfico
    fig_pizza.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',  # Remove o fundo do gráfico
        paper_bgcolor='rgba(0,0,0,0)'  # Remove o fundo da área ao redor do gráfico
    )

    return fig_pizza





import plotly.express as px

def create_horizontal_bar_chart(df):
    # Agrupar por Tipo do Produto e somar a Receita Total
    revenue_by_product_type = df.groupby('Tipo do Produto')['Receita_Total'].sum().reset_index()


    # Classificar por Receita Total em ordem decrescente
    revenue_by_product_type = revenue_by_product_type.sort_values(by='Receita_Total', ascending=True)
    
    # Criar o gráfico de barras horizontal
    fig_barh = px.bar(
        revenue_by_product_type,
        x='Receita_Total',  # Eixo X como Receita Total
        y='Tipo do Produto',  # Eixo Y como Tipo do Produto
        title='Receita Total por Tipo do Produto',
        text='Receita_Total',  # Mostrar os valores nas barras
        orientation='h',  # Define o gráfico como horizontal
        color='Receita_Total',  # Colorir as barras pela Receita Total
    )

    # Personalizar o layout do gráfico
    fig_barh.update_layout(
        yaxis_title='',  # Remove o rótulo do eixo Y
        xaxis_title='Receita Total',
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='rgba(0,0,0,0)',  # Remove o fundo do gráfico
        paper_bgcolor='rgba(0,0,0,0)'  # Remove o fundo da área ao redor do gráfico
    )

    # Remover os números do eixo Y
    fig_barh.update_yaxes(showticklabels=True)  # Exibe os rótulos do eixo Y

    return fig_barh



# Definir o callback
@app.callback(
    [Output('receita-output', 'children'),
     Output('custo-output', 'children'),
     Output('lucro-output', 'children'),
     Output('margem-output', 'children'),
     Output('grafico-receita','figure'),
     Output('grafico-receita-pais','figure'),
     Output('grafico3_1', 'figure'),
     Output('grafico3_2', 'figure'),
     Output('grafico3_3', 'figure')],
    [Input('drop-1', 'value'),
     Input('drop-2', 'value'),]
)

def update_cards(selected_country, selected_year):
    # Filtrar o DataFrame com base nas seleções
    filtered_df = df

    if selected_country:
        filtered_df = filtered_df[filtered_df['Continente'] == selected_country]
    
    if selected_year:
        filtered_df = filtered_df[filtered_df['Ano'] == selected_year]

    # Calcule as medidas receita_total e custo_total
    receita_total = filtered_df['Receita_Total'].sum()
    custo_total = filtered_df['Custo_Total'].sum()
    lucro_total = receita_total - custo_total
   # Calcular a margem de lucro
    margem_lucro = (receita_total - custo_total) / receita_total * 100

    #grafico 1
    fig = create_revenue_graph(filtered_df)
    fig1 = create_revenue_bar_chart(filtered_df)
    fig2 = create_profit_funnel(filtered_df)
    fig_pizza = create_revenue_pie_chart(filtered_df)
    fig_barh = create_horizontal_bar_chart(filtered_df)

   

    # Formatar os valores para o formato brasileiro
    receita_total_str = locale.currency(receita_total, symbol=True, grouping=True)
    custo_total_str = locale.currency(custo_total, symbol=True, grouping=True)
    lucro_total_str = locale.currency(lucro_total, symbol=True, grouping=True)
    # Formatar a margem de lucro como uma string percentual
    margem_lucro_str = f"{margem_lucro:.2f}%"  # Com duas casas decimais
   

    return receita_total_str, custo_total_str, lucro_total_str,  margem_lucro_str, fig, fig1, fig2, fig_pizza, fig_barh




from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
import dash_table

# Carregar os dados do Excel
df = pd.read_excel(r"C:\Users\marciobarros\OneDrive - Unimed Vitória\MARCIO\dash\dataset\Tabela_Vendas.xlsx")

# Definir o layout
layout = html.Div([
    html.Div([
        html.Div([
            html.P([
                html.H3('Tabela de Dados', style={"color": "#0084d6"}),
                dcc.Markdown('''
                   Abaixo os dados que foram utilizados nesse **dashboard**.
                ''',className="title-v1"),
                html.Hr(),
                dbc.Spinner(html.Div(id='data_table', className="table-responsive text-nowrap overflow-auto",
                                     style={'height': '500px'}), color='info')
            ])
        ], className='table_bg twelve columns')
    ], className='table_row row')
])


# Callback para atualizar o conteúdo da tabela
@app.callback(
    Output('data_table', 'children'),
    Input('url', 'pathname')  # Aqui estou usando um Input genérico, ajuste conforme necessário
)
def update_table(pathname):
    # Converter o DataFrame em uma tabela Dash
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        
        page_size=20  # Define o número de linhas por página
    )
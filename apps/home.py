from dash import html
from dash import dcc


layout = html.Div([
    html.Div([
        html.Div([
            html.P(
                "Painel de vendas de KPI", style={"color": "#0084d6",
                                              "font-size": "20px",
                                              'margin-left': '15px',
                                              'margin-top': '15px'}
            ),
            html.P([html.P(dcc.Markdown('''Bem-vindo ao **Painel de vendas de KPI**!''',
                                        style={"color": "#ffffff",
                                               "font-size": "15px",
                                               'margin-left': '15px',
                                               'margin-top': '15px'})),
                    html.P(dcc.Markdown(
                        '''
                        Sou Coordenador de Ciência de Dados, liderando uma equipe de 10 profissionais, composta por cientistas e analistas de dados. 
                        Minha jornada na área de dados começou há quatro anos, após uma longa e bem-sucedida carreira de 16 anos na área comercial. 
                        Durante minha trajetória comercial, sempre utilizei dados para apoiar a tomada de decisões estratégicas, o que despertou meu 
                        interesse em explorar mais profundamente o poder dos dados.
                        Essa transição para a ciência de dados me permitiu combinar minha experiência prática na área de negócios com habilidades técnicas 
                        adquiridas com muito estudo e determinação, focando em resolver problemas complexos e transformar dados brutos em informações valiosas. 
                        Acredito que essa dualidade — uma compreensão profunda das necessidades comerciais e a capacidade de extrair insights de dados — me torna
                        um líder eficaz e orientado a resultados no campo da ciência de dados.

                        Sou formado em gestão Financeira com duas pós graduações (Gestão empresarial e Big Data), atualmente estou cursando minha segunda graduação em 
                        ciência da computação.
                        ''',
                        style={"color": "#ffffff",
                               "font-size": "15px",
                               'margin-left': '15px',
                               'margin-right': '15px',
                               'margin-bottom': '15px',
                               'line-height': '1.5',
                               'text-align': 'justify'}
                    )),
                    html.P([
                        'Para desenvolvimento desse painel, foi usado a biblioteca ',
                        html.A('Plotly', href="https://plotly.com/", target="_blank", style={"color": "#0084d6"
                                                                                             ,'text-decoration': 'none'}),
                        
                    ], style={"color": "#ffffff",
                              "font-size": "15px",
                              'margin-left': '15px',
                              'margin-right': '15px',
                              'margin-bottom': '15px',
                              'line-height': '1.2',
                              'text-align': 'justify',
                              'margin-top': '-15px'}),
                    html.P([dcc.Markdown(
                        '''
                        Se você tiver alguma dúvida ou precisar de ajuda, não hesite em entrar em contato.
                        ''',
                        style={"color": "#ffffff",
                               "font-size": "15px",
                               'margin-left': '15px',
                               'margin-right': '15px',
                               'margin-bottom': '15px',
                               'line-height': '1.2',
                               'text-align': 'justify'},
                    ),
                        html.P(
                            html.A('Marcio Magveski', href='https://www.linkedin.com/in/marcio-jos%C3%A9-magveski-barros-27994374/',
                                   target="_blank", style={"color": "#0084d6", 'text-decoration': 'none'}),
                            style={"color": "#ffffff",
                                   "font-size": "15px",
                                   'margin-left': '15px',
                                   'margin-right': '15px',
                                   'margin-bottom': '30px',
                                   'line-height': '1.2',
                                   'text-align': 'justify',
                                   'margin-top': '-15px'}),
                    ])
                    ])
        ], className='home_bg eight columns')
    ], className='home_row row')
])

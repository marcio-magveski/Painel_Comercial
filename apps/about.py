from dash import html


layout = html.Div([

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Marcio Magveski', style={"color": "#0084d6",
                                                 'margin-left': '15px',
                                                 'margin-top': '15px'}),
                    html.P('Coordenador de Ciência de Dados | Especialista em Big Data, Business Intelligence e Estratégias de Dados, '
                           'apaixonado por extrapolar as expectativas dos clientes'
                           ,
                           style={"color": "#ffffff",
                                  "font-size": "15px",
                                  'margin-left': '15px',
                                  'margin-right': '15px',
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'justify'
                                  }
                           ),
                    html.Div([
                       
                       
                        html.A(href='https://www.linkedin.com/in/marcio-jos%C3%A9-magveski-barros-27994374/', target='_blank',
                               children=[html.Img(src='/assets/linkedin.png', height="30px",
                                                  style={"margin-top": '20px',
                                                         'margin-left': '15px',
                                                         'margin-bottom': '15px',
                                                         "background-color": "#35384b"})]),
                    ])
                ], className='first_text_column'),
                html.Div([
                    html.Img(src='/assets/programmer.gif', className='gif_image')
                ], className='gif_column')
            ], className='gif_row')
        ], className='about_bg eight columns')
    ], className='about_row row')

])

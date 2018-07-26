# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import plotly.figure_factory as ff
import dash_html_components as html
import plotly.graph_objs as go

import plotly.dashboard_objs as dshb

import pandas as pd


app = dash.Dash()


#dog_1 csv========

dfc=pd.read_csv('dog_1.csv')

fig1c = ff.create_gantt(dfc, 
                        #colors=['#333F44', '#93e4c1'],
                        #colors=['#063063', '#93e4c1'], 
                        colors=['#aa1100', '#00cc11'],
                        index_col='Complete',
                        group_tasks=True,  
                        show_colorbar=True,
                        bar_width=0.4, 
                        height=800,
                        width = 1200,
                        #showgrid_x=True, 
                        #showgrid_y=True
                       )

dfcr=pd.read_csv('dog_1r.csv')

fig1cr = ff.create_gantt(dfcr, 
                        #colors=['#333F44', '#93e4c1'],
                        #colors=['#063063', '#93e4c1'], 
                        #colors=['#aa1100', '#00cc11'],
                        colors='Blues',
                        index_col='Complete',
                        group_tasks=True,  
                        show_colorbar=True,
                        bar_width=0.2, 
                        height=360,
                        width = 1200,
                        #showgrid_x=True, 
                        #showgrid_y=True
                       )
#end dog_2 csv=====

#dog_2 csv========

dfd=pd.read_csv('dog_2.csv')

fig2c = ff.create_gantt(dfd, 
                        #colors=['#333F44', '#93e4c1'],
                        colors=['#063063', '#aaccff'], 
                        #colors=['#aa1100', '#00cc11'],
                        index_col='Complete',
                        group_tasks=True,  
                        show_colorbar=True,
                        bar_width=0.4, 
                        height=800,
                        width = 1200,
                        showgrid_x=True, 
                        showgrid_y=True)

#end dog_2 csv=====

# ============  Bar   

trace0 = go.Bar(
    x=dfc['Finish'],
    y=dfc['Complete'],
    #width = [0.8, 0.8, 0.8, 3.5, 4]
)
trace1 = go.Bar(
    x=dfc['Start'],
    y=dfc['Complete'],
    #width = [0.8, 0.8, 0.8, 3.5, 4]
)

trace2 = go.Bar(
    x=dfd['Finish'],
    y=dfd['Complete'],
    #width = [0.8, 0.8, 0.8, 3.5, 4]
)
trace3 = go.Bar(
    x=dfd['Start'],
    y=dfd['Complete'],
    #width = [0.8, 0.8, 0.8, 3.5, 4]
)
data1 = [trace0,trace1]
figb1 = go.Figure(data=data1)

data2 = [trace2,trace3]
figb2 = go.Figure(data=data2)

trace5 = go.Bar(
    x=dfd['Start'],
    y=dfd['Complete']
)
trace6 = go.Scatter(
    x=dfd['Start'],
    y=dfd['Complete'],
    mode='markers',
    opacity = 0.7
)

data5 = [trace5,trace6]
fig5 = go.Figure(data=data5)

data6 = [trace0, trace1, trace2, trace3]
fig6 = go.Figure(data=data6)

# end ======  Bar


app.layout = html.Div(children=[
    html.H1(children='   Мониторинг исполнения договоров по НПП "Атамекен"'),
    html.Div(children='''
        Договоры.
    '''),
    
    html.Label('По договору №1'),
    dcc.Slider(
        min=0, max=9,
        marks={i: 'Отчеты {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=3,
    ),
    
    html.Label('По договору №2'),
    dcc.Slider(
        min=0, max=12,
        marks={i: 'Акты {}'.format(i) if i == 1 else str(i) for i in range(1, 12)},
        value=9,
    ),
    
    html.Div(children='''    '''),
    
    #dcc.Graph(figure=fig, id='gantt'),
    #dcc.Graph(figure=fig1, id='gantt1'),
    #html.Div(children='''
    #    =====================================================.
    #'''),
    
    html.H1(children='         Мониторинг исполнения договорa N1'),
    dcc.Graph(figure=fig1cr, id='gantt1cr'),
    dcc.Graph(figure=fig1c, id='gantt1c'),
    #dcc.Graph(figure=figd, id='dbar'),

    html.H1(children='% выполнения по срокам договорa N1'),
    dcc.Graph(figure=figb1, id='bar1'),    
    
    html.H1(children='         Мониторинг исполнения договорa N2'),
    dcc.Graph(figure=fig2c, id='gantt2c'),
    
    html.H1(children='% выполнения по срокам договорa N2'),
    dcc.Graph(figure=figb2, id='bar2'),  
    dcc.Graph(figure=fig5, id='fig55'),
    dcc.Graph(figure=fig6, id='fig66'),
])


if __name__ == '__main__':
    app.run_server(debug=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:20:55 2017

@author: CharlesPowell
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

style_colors = {
    'page_bg': '#0F1114',
    'content_bg': '#171B25',
    'baseline': '#2B313F',
    'icons': '#58677A',
    'text': '#8395AC',
    'main': '#FFFFFF',
    'small_kpi_good': '#39BF65',
    'large_kpi_good': '#4AF381',
    'small_kpi_bad' : '#E84569',
    'large_kpi_bad' : '#FC406A',
    'contrast': '#2EE4F4'
}

data_colors = {
    'turq_base': '#2EE4F4',
    'turq_dark': '#2291A0',
    'turq_lite': '#ABF4FA',
    'red_base': '#E76670',
    'red_dark': '#914652',
    'red_lite': '#EE949B',
    'gold_base': '#EFCE65',
    'gold_dark': '#BFA450',
    'gold_lite': '#F3DC93',
    'oran_base': '#FF9A53',
    'oran_dark': '#995C31',
    'oran_lite': '#FFB886',
    'grey_lite': 'A9B6B7'
    
}

data_colors1 = [
    '#2EE4F4',
    '#2291A0',
    '#ABF4FA',
    '#E76670',
    '#914652',
    '#EE949B',
    '#EFCE65',
    '#BFA450',
    '#F3DC93',
    '#FF9A53',
    '#995C31',
    '#FFB886'
    
]

# Define text style
style1 = dict(textAlign="center", fontFamily="arial", fontWeight="normal", color = style_colors['text'])
style2 = dict(textAlign="left", fontFamily="arial", fontWeight="normal", color = style_colors['text'])

##### DASH APP #############################

filepath = 'data/'

ops_data_hq = pd.read_csv(filepath + 'ops_data_high_quality_clean.csv', encoding = 'latin1')
width = 1200 # 2400

app = dash.Dash()

app.scripts.config.serve_locally = True
app.config.supress_callback_exceptions = True


app.layout = html.Div(style={'backgroundColor': style_colors['page_bg']}, children = [
    
    html.Br(),    

        
        
       
            html.Div(
            dcc.RangeSlider(id = 'time-slider', 
                            updatemode = 'mouseup',
                        min = 0,
                        max = 7200,
                        value = [0, 7200],
                        marks={
                                0:    {'label': '16:10:00', 'style': style1},
                                1200: {'label': '16:15:00', 'style': style1},
                                2400: {'label': '16:20:00', 'style': style1},
                                3600: {'label': '16:25:00', 'style': style1},
                                4800: {'label': '16:30:00', 'style': style1},
                                6000: {'label': '16:35:00', 'style': style1},
                                7200: {'label': '16:40:00', 'style': style1},
                                },
                        pushable = 1,
                        allowCross = False), style = {'marginLeft': 62, 'marginRight': 282,
                                               'marginBottom': 30, 'marginTop': 30 }),
                
            
            html.Div([html.H3("Overview", style = dict(textAlign="left", 
                                                       fontFamily="arial", 
                                                       fontWeight="normal", 
                                                       color = style_colors['text'],
                                                       marginLeft = 10)),
                    dcc.Graph(id = 'graph1')
                        ]),
            
            html.Div([html.H3("Engine Cylinder Temperatures", style = dict(textAlign="left", 
                                                                           fontFamily="arial", 
                                                                           fontWeight="normal", 
                                                                           color = style_colors['text'],
                                                                           marginLeft = 10)),
                    dcc.Graph(id = 'graph2')
                        ]),
            
            html.Div([html.H3("Cylinder Temperature Deviations", style = dict(textAlign="left", 
                                                                           fontFamily="arial", 
                                                                           fontWeight="normal", 
                                                                           color = style_colors['text'],
                                                                           marginLeft = 10)),
                    dcc.Graph(id = 'graph2b')
                        ]),

            html.Div([html.H3("Engine Cylinder Pressures", style = dict(textAlign="left", 
                                                                        fontFamily="arial", 
                                                                        fontWeight="normal", 
                                                                        color = style_colors['text'],
                                                                        marginLeft = 10)),
                    dcc.Graph(id = 'graph3')
                        ]),

            html.Div([html.H3("Fuel Flow", style = dict(textAlign="left", 
                                                        fontFamily="arial", 
                                                        fontWeight="normal", 
                                                        color = style_colors['text'],
                                                        marginLeft = 10)),
                    dcc.Graph(id = 'graph4')
                        ]),

            html.Div([html.H3("Propulsion", style = dict(textAlign="left", 
                                                         fontFamily="arial", 
                                                         fontWeight="normal", 
                                                         color = style_colors['text'],
                                                         marginLeft = 10)),
                    dcc.Graph(id = 'graph5')
                        ]),

            html.Div([html.H3("Main Engine Load Distribution", style = dict(textAlign="left", 
                                                         fontFamily="arial", 
                                                         fontWeight="normal", 
                                                         color = style_colors['text'],
                                                         marginLeft = 10)),
                    dcc.Graph(id = 'graph6')
                        ]),

            html.Div([html.H3("Propulsion Mode over Time", style = dict(textAlign="left", 
                                                         fontFamily="arial", 
                                                         fontWeight="normal", 
                                                         color = style_colors['text'],
                                                         marginLeft = 10)),
                        dcc.Graph(
                                id='graph7',
                                figure={
                                    'data': [
                                        {'x': ops_data_hq['Timestamp'], 
                                         'y': ops_data_hq['Propulsion_Mode'], 
                                         'text': 'Combinator',
                                         'hoverinfo': 'text',
                                         'type': 'bar', 
                                         'name': 'Combinator',
                                         'marker': {'color': data_colors['gold_dark']},
                                         }
                                    ],
                                    'layout': {
                                        'xaxis': {'linecolor': 'black','linewidth': 2,
                                               'ticks': False, 'titlefont': {'color': style_colors['text']}},
                                        'yaxis': {'linecolor': 'black', 'linewidth': 2,'ticks':False, 
                                               'zeroline': False, 'showticklabels': False, 
                                               'titlefont': {'color': style_colors['text']},
                                               'range': [0, 2]},
                                        'margin': {'l': 60, 'b': 10, 't': 10, 'r': 10},
                                        'hovermode': 'closest',
                                        'height': '100',
                                        'width': width - 220,
                                        'plot_bgcolor': style_colors['page_bg'],
                                        'paper_bgcolor': style_colors['page_bg'],
                                        'showlegend': True,
                                        'legend': {'x': 0, 'y': 1.2,
                                                   'font': {'color': style_colors['text']}}
                                    }
                                }
                            )
                        ]),

            html.Div([html.H3("Power Mode over Time", style = dict(textAlign="left", 
                                                         fontFamily="arial", 
                                                         fontWeight="normal", 
                                                         color = style_colors['text'],
                                                         marginLeft = 10)),
                        dcc.Graph(
                                id='graph8',
                                figure={
                                    'data': [
                                        {'x': ops_data_hq['Timestamp'], 
                                         'y': ops_data_hq['Propulsion_Mode'], 
                                         'text': 'Mechanical',
                                         'hoverinfo': 'text',
                                         'type': 'bar', 
                                         'name': 'Mechanical',
                                         'marker': {'color': data_colors['red_dark']},
                                         }
                                    ],
                                    'layout': {
                                        'xaxis': {'linecolor': 'black','linewidth': 2,
                                               'ticks': False, 'titlefont': {'color': style_colors['text']}},
                                        'yaxis': {'linecolor': 'black', 'linewidth': 2,'ticks':False, 
                                               'zeroline': False, 'showticklabels': False, 
                                               'titlefont': {'color': style_colors['text']},
                                               'range': [0, 2]},
                                        'margin': {'l': 60, 'b': 10, 't': 10, 'r': 10},
                                        'hovermode': 'closest',
                                        'height': '100',
                                        'width': width - 220,
                                        'plot_bgcolor': style_colors['page_bg'],
                                        'paper_bgcolor': style_colors['page_bg'],
                                        'showlegend': True,
                                        'legend': {'x': 0, 'y': 1.2,
                                                   'font': {'color': style_colors['text']}}
                                    }
                                }
                            )
                        ])
        
        ])


@app.callback(Output('graph1', 'figure'),
    [Input('time-slider', 'value')])
def update_figure1(slider_value):
    lines = []
    for i, col in enumerate(['Propeller RPM %', 'Propeller Pitch %', 
                             'BMEP Load Calc %', 'Fuel Flow %', 
                             'Cylinder Temp Deviation from Average']):
        lines.append({'type': 'scatter',
                     'mode': 'lines',
                     'x': ops_data_hq.index,
                     'y': ops_data_hq[col],
                     'text' : ops_data_hq['{}_text'.format(col)],
                     'hoverinfo': 'text',
                     'marker': {'size': 8,
                                'color': [data_colors['red_base'], 
                                          data_colors['oran_base'], 
                                          data_colors['gold_base'], 
                                          data_colors['turq_base'],
                                          data_colors['grey_lite']][i],
                                'line': {'width' : 1}},
                     'name': ['Propeller RPM', 'Propeller Pitch', 
                             'BMEP Load Calc', 'Fuel Flow', 
                             'Temp Comparison'][i]})

    return {
        'data': lines,
        'layout': go.Layout(
            xaxis={'showgrid': True, 'linecolor': 'black','linewidth': 2,
                   'mirror': 'ticks', 'ticks': 'inside',
                   'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': 'Percentage (%)', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 'mirror': 'ticks', 
                   'ticks':'inside', 'zeroline': False},
            shapes=[{'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 700, 'y0': 0, 'x1': 1840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2},
                    {'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 4800, 'y0': 0, 'x1': 6840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2}],
            margin={'l': 60, 'b': 10, 't': 10},
            hovermode='closest',
            height = '300',
            width = width,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }
        
@app.callback(Output('graph2', 'figure'),
    [Input('time-slider', 'value')])
def update_figure2(slider_value):
    lines = []
    for i, col in enumerate(['Cylinder 1 Temp', 'Cylinder 2 Temp', 'Cylinder 3 Temp', 'Cylinder 4 Temp', 'Cylinder 5 Temp', 'Cylinder 6 Temp',
                             'Cylinder 7 Temp', 'Cylinder 8 Temp', 'Cylinder 9 Temp', 'Average Cylinder Temp']):
        lines.append({'type': 'scatter',
                     'mode': 'lines',
                     'x': ops_data_hq.index,
                     'y': ops_data_hq[col],
                     'text' : ops_data_hq['{}_text'.format(col)],
                     'hoverinfo': 'text',
                     'marker': {'size': 8,
                                'color': [data_colors['red_lite'],
                                          data_colors['oran_lite'],
                                          data_colors['gold_lite'],
                                          data_colors['gold_dark'],
                                          data_colors['turq_dark'],
                                          data_colors['red_lite'],
                                          data_colors['turq_lite'],
                                          data_colors['oran_dark'],
                                          data_colors['grey_lite'],
                                          data_colors['turq_base']][i],
                                'line': {'width' : 1}},
                     'name': ['Cylinder 1', 'Cylinder 2', 'Cylinder 3',
       'Cylinder 4', 'Cylinder 5', 'Cylinder 6', 'Cylinder 7', 'Cylinder 8',
       'Cylinder 9', 'Average Temp     '][i]})

    return {
        'data': lines,
        'layout': go.Layout(
            xaxis={'showgrid': True, 'linecolor': 'black','linewidth': 2,
                   'mirror': 'ticks', 'ticks': 'inside',
                   'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': 'Temperature (°C)', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 'mirror': 'ticks', 
                   'ticks':'inside', 'zeroline': False},
            shapes=[{'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 700, 'y0': 0, 'x1': 1840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2},
                    {'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 4800, 'y0': 0, 'x1': 6840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2}],
            margin={'l': 60, 'b': 10, 't': 10, 'r': 10},
            hovermode='closest',
            height = '300',
            width = width,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }        
        
@app.callback(Output('graph2b', 'figure'),
    [Input('time-slider', 'value')])
def update_figure2b(slider_value):
    lines = []
    for i, col in enumerate(['Cylinder 1 % Deviation',
       'Cylinder 2 % Deviation', 'Cylinder 3 % Deviation', 'Cylinder 4 % Deviation',
       'Cylinder 5 % Deviation', 'Cylinder 6 % Deviation', 'Cylinder 7 % Deviation',
       'Cylinder 8 % Deviation', 'Cylinder 9 % Deviation']):
        lines.append({'type': 'scatter',
                     'mode': 'lines',
                     'x': ops_data_hq.index,
                     'y': ops_data_hq[col],
                     'text' : ops_data_hq['{}_text'.format(col)],
                     'hoverinfo': 'text',
                     'marker': {'size': 8,
                                'color': [data_colors['red_lite'],
                                          data_colors['oran_lite'],
                                          data_colors['gold_lite'],
                                          data_colors['gold_dark'],
                                          data_colors['turq_dark'],
                                          data_colors['red_lite'],
                                          data_colors['turq_lite'],
                                          data_colors['oran_dark'],
                                          data_colors['grey_lite']][i],
                                'line': {'width' : 1}},
                     'name': ['Cylinder 1', 'Cylinder 2', 'Cylinder 3',
       'Cylinder 4', 'Cylinder 5', 'Cylinder 6', 'Cylinder 7', 'Cylinder 8',
       'Cylinder 9'][i]})

    lines.append({'type': 'scatter',
                 'mode': 'lines',
                 'x': ops_data_hq.index,
                 'y': ops_data_hq['Average Cylinder Temp'],
                 'text' : ops_data_hq['Average Cylinder Temp_text'],
                 'hoverinfo': 'text',
                 'yaxis': 'y2',
                 'marker': {'size': 2,
                            'color': data_colors['turq_base'],
                            'line': {'width' : 1}},
                            'name': 'Average Temp     '})
    
    return {
        'data': lines,
        'layout': go.Layout(
            xaxis={'showgrid': True, 'linecolor': 'black','linewidth': 2,
                   'mirror': 'ticks', 'ticks': 'inside',
                   'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': '% Deviation from Average', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 'ticks':'inside'},
            yaxis2={'title': 'Temperature (°C)', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 
                   'ticks':'inside', 'overlaying': 'y', 'side': 'right',
                   'range': [350, 650]},       
            shapes=[{'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 700, 'y0': 0, 'x1': 1840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2},
                    {'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 4800, 'y0': 0, 'x1': 6840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2}],
            margin={'l': 60, 'b': 10, 't': 10, 'r': 10},
            hovermode='closest',
            height = '300',
            width = width,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }                

@app.callback(Output('graph3', 'figure'),
    [Input('time-slider', 'value')])
def update_figure3(slider_value):
    lines = []
    for i, col in enumerate(['Cylinder 1 Pressure', 'Cylinder 2 Pressure', 'Cylinder 3 Pressure',
       'Cylinder 4 Pressure', 'Cylinder 5 Pressure', 'Cylinder 6 Pressure', 'Cylinder 7 Pressure', 'Cylinder 8 Pressure',
       'Cylinder 9 Pressure', 'Average Cylinder Pressure']):
        lines.append({'type': 'scatter',
                 'mode': 'lines',
                 'x': ops_data_hq.index,
                 'y': ops_data_hq[col],
                 'text' : ops_data_hq['{}_text'.format(col)],
                 'hoverinfo': 'text',
                 'marker': {'size': 8,
                            'color': [data_colors['red_lite'],
                                      data_colors['oran_lite'],
                                      data_colors['gold_lite'],
                                      data_colors['gold_dark'],
                                      data_colors['turq_dark'],
                                      data_colors['red_lite'],
                                      data_colors['turq_lite'],
                                      data_colors['oran_dark'],
                                      data_colors['grey_lite'],
                                      data_colors['turq_base']][i],
                                'line': {'width' : 1}},
                            'name': ['Cylinder 1', 'Cylinder 2', 'Cylinder 3',
       'Cylinder 4', 'Cylinder 5', 'Cylinder 6', 'Cylinder 7', 'Cylinder 8',
       'Cylinder 9', 'Average Pressure '][i]})
    
    return {
        'data': lines,

        'layout': go.Layout(
            xaxis={'showgrid': True, 'linecolor': 'black','linewidth': 2,
                   'mirror': 'ticks', 'ticks': 'inside',
                   'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': 'Pressure', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 'mirror': 'ticks', 
                   'ticks':'inside', 'zeroline': False},
            shapes=[{'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 700, 'y0': 0, 'x1': 1840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2},
                    {'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 4800, 'y0': 0, 'x1': 6840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2}],
            margin={'l': 60, 'b': 10, 't': 10, 'r': 10},
            hovermode='closest',
            height = '300',
            width = width,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }
        
@app.callback(Output('graph4', 'figure'),
    [Input('time-slider', 'value')])
def update_figure4(slider_value):
    lines = []
    for i, col in enumerate(['Fuel Flow %']):
        lines.append({'type': 'scatter',
                 'mode': 'lines',
                 'x': ops_data_hq.index,
                 'y': ops_data_hq[col],
                 'text' : ops_data_hq['{}_text'.format(col)],
                 'hoverinfo': 'text',
                 'marker': {'size': 2,
                            'color': data_colors['turq_base'],
                            'line': {'width' : 1}},
                            'name': col})
    
    return {
        'data': lines,

        'layout': go.Layout(
            xaxis={'showgrid': True, 'linecolor': 'black','linewidth': 2,
                   'mirror': 'ticks', 'ticks': 'inside',
                   'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': 'Fuel Flow', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 'mirror': 'ticks', 
                   'ticks':'inside', 'zeroline': False},
            shapes=[{'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 700, 'y0': 0, 'x1': 1840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2},
                    {'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 4800, 'y0': 0, 'x1': 6840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2}],
            margin={'l': 60, 'b': 10, 't': 10, 'r': 10},
            hovermode='closest',
            height = '300',
            width = width - 220,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }     
        
@app.callback(Output('graph5', 'figure'),
    [Input('time-slider', 'value')])
def update_figure5(slider_value):
    lines = []        
    lines.append({'type': 'scatter',
                 'mode': 'lines',
                 'x': ops_data_hq.index,
                 'y': ops_data_hq['Vessel Speed'],
                 'text' : ops_data_hq['Vessel Speed_text'],
                 'hoverinfo': 'text',
                 'yaxis': 'y2',
                 'marker': {'size': 2,
                            'color': data_colors['turq_dark'],
                            'line': {'width' : 1}},
                            'name': 'Vessel Speed'})
            
    for i, col in enumerate(['Propeller RPM %', 'Propeller Pitch %']):
        lines.append({'type': 'scatter',
                 'mode': 'lines',
                 'x': ops_data_hq.index,
                 'y': ops_data_hq[col],
                 'text' : ops_data_hq['{}_text'.format(col)],
                 'hoverinfo': 'text',
                 'marker': {'size': 2,
                            'color': [data_colors['red_base'],
                                      data_colors['oran_base']][i],
                            'line': {'width' : 1}},
                 'name': ['Propeller RPM', 'Propeller Pitch     '][i]})
    
    return {
        'data': lines,

        'layout': go.Layout(
            xaxis={'showgrid': True, 'linecolor': 'black','linewidth': 2,
                   'mirror': 'ticks', 'ticks': 'inside',
                   'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': 'Percentage (%)', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 
                   'ticks':'inside', 'zeroline': False},
            yaxis2={'title': 'Vessel Speed (knots)', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 
                   'ticks':'inside', 'overlaying': 'y', 'side': 'right'},
            margin={'l': 60, 'b': 10, 't': 10, 'r': 10},
            shapes=[{'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 700, 'y0': 0, 'x1': 1840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2},
                    {'type': 'rect', 'xref': 'x', 'yref': 'paper',
                    'x0': 4800, 'y0': 0, 'x1': 6840, 'y1': 1,
                    'line': {'width': 0}, 'fillcolor': '#d3d3d3', 
                    'opacity': 0.2}],
            hovermode='closest',
            height = '300',
            width = width,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }       

@app.callback(Output('graph6', 'figure'),
    [Input('time-slider', 'value')])
def update_figure6(slider_value):
    lines = []
    for i, col in enumerate(['Auxiliary Engine Load','Main Engine Load (kW)']):
        lines.append({'type': 'scatter',
                 'mode': 'lines',
                 'fill': 'tonexty',
                 'x': ops_data_hq.index,
                 'y': ops_data_hq[col],
                 'text' : ops_data_hq['{}_text'.format(col)],
                 'hoverinfo': 'text',
                 'marker': {'size': 2,
                            'color': [data_colors['turq_dark'],
                                      data_colors['oran_lite']][i],
                            'line': {'width' : 1}},
                 'name': ['Auxiliary Engine  ', 'Main Engine'][i]})
    
    return {
        'data': lines,

        'layout': go.Layout(
            xaxis={'linecolor': 'black','linewidth': 2,
                   'ticks': False, 'showticklabels': False, 'range': [slider_value[0], slider_value[1]]},
            yaxis={'title': 'Percentage (%)', 'showgrid': True, 
                   'linecolor': 'black', 'linewidth': 2, 'mirror': 'ticks', 
                   'ticks':'inside', 'zeroline': False},
            margin={'l': 60, 'b': 10, 't': 10, 'r': 10},
            hovermode='closest',
            height = '300',
            width = width,
            plot_bgcolor = style_colors['content_bg'],
            paper_bgcolor = style_colors['page_bg'],
            legend = {'x': 1.07, 'y': 1, 'font': {'color': style_colors['text']}}
        )
    }               
        

if __name__ == '__main__':
    app.run_server(debug=True)
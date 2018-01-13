# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: test.py

@time: 2018/1/10 14:18

@desc:

'''

from IPython.display import display, HTML

# The public plotly graphs to include in the report. These can also be generated with `py.plot(figure, filename)`
graphs = [
    'https://plot.ly/~christopherp/308',
    'https://plot.ly/~christopherp/306',
    'https://plot.ly/~christopherp/300',
    'https://plot.ly/~christopherp/296'
]

def report_block_template(report_type, graph_url, caption=''):
    if report_type == 'interactive':
        graph_block = '<iframe style="border: none;" src="{graph_url}.embed" width="100%" height="600px"></iframe>'
    elif report_type == 'static':
        graph_block = (''
            '<a href="{graph_url}" target="_blank">' # Open the interactive graph when you click on the image
                '<img style="height: 400px;" src="{graph_url}.png">'
            '</a>')

    report_block = ('' +
        graph_block +
        '{caption}' + # Optional caption to include below the graph
        '<br>'      + # Line break
        '<a href="{graph_url}" style="color: rgb(190,190,190); text-decoration: none; font-weight: 200;" target="_blank">'+
            'Click to comment and see the interactive graph' + # Direct readers to Plotly for commenting, interactive graph
        '</a>' +
        '<br>' +
        '<hr>') # horizontal line

    return report_block.format(graph_url=graph_url, caption=caption)


interactive_report = ''
static_report = ''

for graph_url in graphs:
    _static_block = report_block_template('static', graph_url, caption='')
    _interactive_block = report_block_template('interactive', graph_url, caption='')

    static_report += _static_block
    interactive_report += _interactive_block

display(HTML(interactive_report))
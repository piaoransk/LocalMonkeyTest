# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: test1.py

@time: 2018/1/10 14:26

@desc:

'''
# Get this figure: fig = py.get_figure("https://plot.ly/~christopherp/308/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~christopherp/308/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="11", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~christopherp/308/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('xyh421', '31TnQJ9g35ifF8ALFxWj')
trace1 = {
  "x": ["1990-01-01 00:00:00", "1991-01-01 00:00:00", "1992-01-01 00:00:00", "1993-01-01 00:00:00", "1994-01-01 00:00:00", "1995-01-01 00:00:00", "1996-01-01 00:00:00", "1997-01-01 00:00:00", "1998-01-01 00:00:00", "1999-01-01 00:00:00", "2000-01-01 00:00:00", "2001-01-01 00:00:00", "2002-01-01 00:00:00", "2003-01-01 00:00:00", "2004-01-01 00:00:00", "2005-01-01 00:00:00", "2006-01-01 00:00:00", "2007-01-01 00:00:00", "2008-01-01 00:00:00", "2009-01-01 00:00:00", "2010-01-01 00:00:00", "2011-01-01 00:00:00", "2012-01-01 00:00:00", "2013-01-01 00:00:00"],
  "y": [11.5, 10.6, 10.7, 11.1, 12.5, 13.7, 15, 16.8, 17.9, 18.7, 19.6, 16.6, 15.9, 15.8, 16.6, 17.3, 17, 14.2, 10.1, 6.1, 5.6, 5, 4.6, 4.1],
  "marker": {"color": "rgb(94, 118, 170)"},
  "name": "Desktop",
  "type": "bar",
  "uid": "9f75f5",
  "xsrc": "christopherp:309:6b2dc1",
  "ysrc": "christopherp:309:159aab"
}
trace2 = {
  "x": ["1990-01-01 00:00:00", "1991-01-01 00:00:00", "1992-01-01 00:00:00", "1993-01-01 00:00:00", "1994-01-01 00:00:00", "1995-01-01 00:00:00", "1996-01-01 00:00:00", "1997-01-01 00:00:00", "1998-01-01 00:00:00", "1999-01-01 00:00:00", "2000-01-01 00:00:00", "2001-01-01 00:00:00", "2002-01-01 00:00:00", "2003-01-01 00:00:00", "2004-01-01 00:00:00", "2005-01-01 00:00:00", "2006-01-01 00:00:00", "2007-01-01 00:00:00", "2008-01-01 00:00:00", "2009-01-01 00:00:00", "2010-01-01 00:00:00", "2011-01-01 00:00:00", "2012-01-01 00:00:00", "2013-01-01 00:00:00"],
  "y": [20.8, 19.8, 19.9, 20.7, 21.6, 22.3, 23, 24.6, 26, 27.6, 29.1, 27.7, 28.2, 29.2, 30.1, 30, 29.6, 28, 24.7, 18.6, 17.2, 15.7, 14.3, 13.1],
  "marker": {"color": "rgb(217, 217, 217)"},
  "name": "Tablet",
  "type": "bar",
  "uid": "5adc98",
  "xsrc": "christopherp:309:6b2dc1",
  "ysrc": "christopherp:309:ab0975"
}
trace3 = {
  "x": ["2003-01-01 00:00:00", "2004-01-01 00:00:00", "2005-01-01 00:00:00", "2006-01-01 00:00:00", "2007-01-01 00:00:00", "2008-01-01 00:00:00", "2009-01-01 00:00:00", "2010-01-01 00:00:00", "2011-01-01 00:00:00", "2012-01-01 00:00:00", "2013-01-01 00:00:00"],
  "y": [1.2, 1.6, 2, 2.7, 3.1, 3.1, 2.7, 3, 3.2, 3.4, 3.4],
  "marker": {"color": "rgb(174, 186, 213)"},
  "name": "Mobile",
  "type": "bar",
  "uid": "5f63cf",
  "xsrc": "christopherp:309:9accfc",
  "ysrc": "christopherp:309:740d1e"
}
data = Data([trace1, trace2, trace3])
layout = {
  "autosize": True,
  "height": 677,
  "showlegend": True,
  "title": "Site Traffic",
  "width": 787,
  "xaxis": {
    "autorange": True,
    "range": [615402000000, 1372784400000],
    "type": "date"
  },
  "yaxis": {
    "autorange": True,
    "range": [0, 31.6842105263],
    "title": "Visits (Millions)",
    "type": "linear"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
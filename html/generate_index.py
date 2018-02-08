# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: index.py

@time: 2018/2/8 10:05

@desc:

'''
progress_html = """
<table width="200" border="1">
  <tr>
    <th scope="row">安装</th>
    <td><div align="center">成功</div></td>
    <td><div align="center">10s</div></td>
  </tr>
  <tr>
    <th scope="row">启动</th>
    <td><div align="center">成功</div></td>
    <td><div align="center">10s</div></td>
  </tr>
  <tr>
    <th scope="row">测试</th>
    <td><div align="center">成功</div></td>
    <td><div align="center">10s</div></td>
  </tr>
  <tr>
    <th scope="row">卸载</th>
    <td><div align="center">成功</div></td>
    <td><div align="center">10s</div></td>
  </tr>
</table>
"""
screenshot_html = ""
performance_html = ""
overview_html = ""
exception_html = ""
index_filename = "indexTest.html"
index_html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>本地兼容性测试</title>
    <script src="https://img.hcharts.cn/jquery/jquery-1.8.3.min.js"></script>
    <script src="https://img.hcharts.cn/highcharts/highcharts.js"></script>
    <script src="https://img.hcharts.cn/highcharts/highcharts-more.js"></script>
    <script src="https://img.hcharts.cn/highcharts-plugins/highcharts-zh_CN.js"></script>
</head>
<body>
<div id="overview">
    测试结果
    %s
</div>
<div id="image_view">
    查看截图
    %s
</div>
<div id="monkey_view">
    异常汇总
    %s
   
</div>
<div id="progress_view">
    进程详情
    %s
</div>
<div id="performance_line_chart">
    性能曲线
    %s
</div>

</body>
</html>
"""

def get_progress():
    pass
def get_overview():
    pass
def get_index():
    pass
def get_performance():
    pass
def get_image():
    pass

with open("index_filename", w) as f:
    f.write(index_html)

# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: writeJson.py

@time: 2018/2/8 10:54

@desc:

'''
import json


json_str = """
{
  "xData": %s,
  "datasets": [{
    "name": "CPU",
    "data": %s,
    "unit": "%%",
    "type": "line",
    "valueDecimals": 1
  }, {
    "name": "内存",
    "data": %s,
    "unit": "kb",
    "type": "line",
    "valueDecimals": 0
  }, {
    "name": "上传网络",
    "data": %s,
    "unit": "kb",
    "type": "line",
    "valueDecimals": 0
  }, 
  {
    "name": "下传网络",
    "data": %s,
    "unit": "kb",
    "type": "line",
    "valueDecimals": 0
  }
  
  
  , {
    "name": "FPS",
    "data": %s,
    "unit": "",
    "type": "line",
    "valueDecimals": 0
  }
    , {
    "name": "电池",
    "data": %s,
    "unit": "",
    "type": "line",
    "valueDecimals": 0
  }
  ]
}
"""


def write_json(filepath, filedata):
    with open(filepath, "w") as f:
        f.write(filedata)


def generate_main_json_str( timestr, cpu, memory,  upflow,downflow, fps, battery):
    """
    timestr, cpu, memory,  upflow,downflow, fps, battery
    把所有list 加到json文件中
    :param temp_json:
    :param cpu:
    :param memory:
    :param upflow:
    :param downflow:
    :param fps:
    :param battery:
    :return:
    """
    # return json_str%(memory,cpu, battery , upflow,downflow, fps, time)
    return json_str % (timestr, cpu, memory,  upflow,downflow, fps, battery)


def generate_progress():
    pass













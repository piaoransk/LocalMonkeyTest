# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: test.py

@time: 2018/1/31 15:02

@desc:

'''

cpu_info = ['203,046K:', '234,233K:']
men_info = ['60%', '54%']
battery_info = ['100', '100']
upflow_info = ['552863\r\n', '614020\r\n']
downflow_info = ['7079519\r\n', '7995729\r\n']

print  cpu_info[0].replace(",","")[:-2]
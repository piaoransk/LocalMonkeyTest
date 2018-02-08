# -*- coding: UTF-8 -*-

'''

@author: yuhuixu

@file: util.py

@time: 2017/11/22 15:15

@desc: 工具类,存放一些工具的方法,监控什么的就放这里吧
收集数据
通过率: 96.67%
通过终端数: 29 可能影响 1403 万用户
未通过终端数: 1 可能影响 200 万用户
总终端数: 30


失败概况

运行失败100%
运行失败100.0%
错误类型	终端数	影响用户数（万）
安装失败	0	0
启动失败	0	0
运行失败	1	200
合计	1	200

测试概况




终端详情
错误日志
性能报告
    指标	测试结果	行业对比	行业平均指标	综合排名前20%终端数	综合排名后80%终端数
    启动耗时	361.00 ms	优于 77.76% 的APP	2798.83 ms	1	7
    CPU占用	1.40%	优于 86.80% 的APP	9.50%	0	8
    内存占用	139.74 MB	优于 87.01% 的APP	87.15 MB	0	8
    流量耗用	623.24 KB/min	优于 89.26% 的APP	4.81 MB/min	0	8
    电量耗用	2.90 mAh/min	优于 63.81% 的APP	3.49 mAh/min	2	6
    FPS	12.78	优于 13.70% 的APP	39	7	1
全部截图








'''

import re


class Report(object):

    def __init__(self):
        self.start_print()
        self._crashMonkey = []
        self._analyzeLogcat = []

    def __del__(self):
        self.end_print()

    def get_monkey_crash_msg(self, log):
        """
        分析menkey日志
        :param log:monkey日志全路径
        :return: 返回[错误分类,错误信息,行数]
        """
        with open(log) as monkey_log:
            lines = monkey_log.readlines()
            i = 1
            for line in lines:
                if re.findall(r"^ANR", line):
                    print("存在anr错误:" + line)
                    self._crashMonkey.append(["ANR", line, i])
                if re.findall(r"^Crash", line):
                    print("存在crash错误:" + line)
                    self._crashMonkey.append(["Crash", line, i])
                if re.findall(r"^EXCEPTION", line):
                    print("exception" + line)
                    self._crashMonkey.append(["EXCEPTION", line, i])
                i += 1
            return self._crashMonkey

    def analyze_logcat(self, log):
        """
        分析logcat日志
        :param log:logcat日志全路径
        :return: 返回错误信息和行数
        """
        with open(log) as monkey_log:
            lines = monkey_log.readlines()
            i = 1
            anr_num = 0
            crash_num = 0
            exception = 0
            for line in lines:
                if re.findall(r"^ANR", line):
                    print("存在anr错误:" + line)
                    self._analyzeLogcat.append(["ANR", line, i])

                if re.findall(r"^Crash", line):
                    print("存在crash错误:" + line)
                    self._analyzeLogcat.append(["Crash", line, i])
                if re.findall(r"^EXCEPTION", line):
                    print("exception" + line)
                    self._analyzeLogcat.append(["EXCEPTION", line, i])
                i += 1
            return self._crashM

    def start_print(self):
        # print " ____                        __  ____"
        # print "/\  _`\               __    /\ \/\  _`\\"
        # print "\ \ \/\ \  _ __  ___ /\_\   \_\ \ \ \L\ \   ___   __  _"
        # print " \ \ \ \ \/\`'__\ __`\/\ \  /'_` \ \  _ <' / __`\/\ \/'\\"
        # print "  \ \ \_\ \ \ \/\ \L\ \ \ \/\ \L\ \ \ \L\ \\ \L\ \/>  </"
        # print "   \ \____/\ \_\ \____/\ \_\ \___,_\ \____/ \____//\_/\_\\"
        # print "    \/___/  \/_/\/___/  \/_/\/__,_ /\/___/ \/___/ \//\/_/"
        print """
    ((         /|_/|
       \\.._.'   , ,\  
       /\ | '.__ v /    
        (_ .    /    "         
     ) _) ._   _ /     
      '.\ \| ( / (       
        '' ''\\ \\ 
        go go go ...    
    """

    def end_print(self):
        print """
    ((         /|_/|
       \\.._.'   , ,\  
       /\ | '.__ v /    
        (_ .    /    "         
     ) _) ._   _ /     
      '.\ \| ( / (       
        '' ''\\ \\ 
        Done ...    
    """

if __name__ == '__main__':
    obj = Report()


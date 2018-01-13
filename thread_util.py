# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: thread_util.py

@time: 2017/11/29 16:12

@desc:

'''

import cPickle as Pickle
import threading,time, re

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 1000:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        # time.sleep(1)
        print time.ctime()
    print('thread %s ended.' % threading.current_thread().name)


# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
import subprocess
def getcpuinfo():
    """
       cpu  pid  NAME
      0.1% 2687/com.zzl.falcon.internal: 0% user + 0.1% kernel / faults: 163 minor
        0% 2796/com.zzl.falcon.internal:channel: 0% user + 0% kernel / faults: 293 minor
        分割的顺序
        ['3%', '2687/com.zzl.falcon.internal:', '1%', 'user', '+', '2%', 'kernel', '/', 'faults:', '2421', 'minor']
    :return:
    """
    cmd="adb shell dumpsys cpuinfo | grep com.zzl.falcon.internal"
    output=subprocess.check_output(cmd).split()
    # print output
    s_men = ".".join([x.decode() for x in output])  # 转换为string
    print s_men
    len_output=len(output)
    n = 11  # 每行log的数量
    num=len_output/n
    cpu_dic={}
    for i in range(num):
        cpu_dic[output[i*n+1]] = output[i*n]
    print cpu_dic
    return cpu_dic

def getmeminfo():
    """
C:\Users\yuhui>adb shell "dumpsys meminfo | grep com.zzl.falcon"
    55321 kB: com.zzl.falcon.internal (pid 2687 / activities)
    20059 kB: com.zzl.falcon.internal:channel (pid 2796)
               55321 kB: com.zzl.falcon.internal (pid 2687 / activities)
               20059 kB: com.zzl.falcon.internal:channel (pid 2796)

        分割的顺序

    :return:
    """
    cmd="adb shell dumpsys meminfo | grep com.zzl.falcon"
    output1=subprocess.check_output(cmd)            #以空格分割日志
    print output1
    output=output1.split()
    print output
    len_output=len(output)
    print len_output
    n=6                                                     #每行log的数量
    num=output.count('kB:')
    print num
    mem_dic={}
    for i in range(len_output/2):
        if output[i]=='kB:':
            mem_dic[output[i+1]] = output[i -1]
    print mem_dic
    return mem_dic

def getdeviceinfo():
    """
    [ro.build.version.release]: [5.1]
    [ro.product.model]: [Google Nexus 4 - 5.1.0 - API 22 - 768x1280]
    [ro.product.brand]: [generic]
    :return:
    """
    cmd="adb shell getprop"
    print(cmd)
    # output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    output = subprocess.check_output(cmd).decode()
    # print output
    result={}

    result["release"] = getvaluefromgetprop(re.findall("release].*?]", output, re.S)[0])     # 系统版本
    result["brand_name"] = getvaluefromgetprop(re.findall("ro.product.brand].*?]", output, re.S)[0])         # 手机名
    result["phone_model"] = getvaluefromgetprop(re.findall("ro.product.model].*?]", output, re.S)[0])         # 品牌名

    print result
    return result
def getvaluefromgetprop(var):
    """
     [ro.build.version.release]: [5.1] 获取5.1
     ro.product.model]: [Google Nexus 4 - 5.1.0 - API 22 - 768x1280]
    :return:
    """

    res=var.split()
    print res
    str = "".join([x.decode() for x in res])
    # print str
    str1=str.split(':')[1][1:-1]
    # print str1
    return str1

def get_battery():
    try:
        cmd = "adb  shell dumpsys battery"
        print(cmd)
        output = subprocess.check_output(cmd).split()
        # _batter = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
        #                            stderr=subprocess.PIPE).stdout.readlines()
        st = ".".join([x.decode() for x in output])  # 转换为string
        print(st)
        battery2 = int(re.findall("level:.(\d+)*", st, re.S)[0])
        print battery2
    except:
        battery2 = 90
    # writeInfo(battery2, PATH("../info/" + devices + "_battery.pickle"))

    return battery2
# get_battery()
# getdeviceinfo()
# getcpuinfo()
# getmeminfo()
import pickle
# path="pickle.pkl"
path=r'C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101_5555_battery.pickle'
# s=getcpuinfo()
# f=open(path, 'a+')
# data1= Pickle.dump(s, f)
# print data1
# with open(path, 'a+') as f:
#     data2= pickle.load(f)
# print data2.items()
# print data2.keys()
import os
def readInfo(path):
    data = []
    print os.path.exists(path)
    with open(path, 'a+') as f:
        try:
            data = pickle.load(f)
            print data
            # print(data)
        except EOFError:
            data = []
            print("读取文件错误")
            print path
    print("------read-------")
    print(path)
    print(data)
    return data
path=r'C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101_5555_battery.pickle'
readInfo(path)
# devices=['192.168.179.101:5555', '1234567']
# _app = {}
# devices_Pool=[]
# for item in range(0, len(devices)):
#     if ':' in devices[item]:
#         print '替换 :'
#         de=devices[item].replace(':', ' ')  # device 包含':' ,无法写入文件名,因为文件名不能有特殊符号
#         print 'de:',de
#         _app["devices"+str(item)] = de
#     else:
#         _app["devices"+str(item)] = devices[item]
#     _app["num"] = len(devices)
#     devices_Pool.append(_app)
# print devices_Pool

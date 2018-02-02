# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: test.py

@time: 2018/1/13 14:50

@desc:

'''
import pickle,os,math
path='C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'
def verify_colon(path):
    """
    验证path是否有冒号,如果有就替换成空格
    :param path:
    :return:
    """
    # print "之前:",path
    # path_wait_exist(path)
    basename = os.path.basename(path)
    if ':' in basename:
        # print "替换一下:",path
        basename = basename.replace(':', '_')
        dirname = os.path.dirname(path)
        path = os.path.join(dirname, basename)
    # print "之后:", path
    return path

def readInfo(path):
    data = []
    path = verify_colon(path)
    with open(path, 'rb') as f:
        data = pickle.load(f)
        # try:
        #     data = pickle.load(f)
        #     print "data:",data
        #     # print(data)
        # except EOFError:
        #     data = []
        #     print("读取文件错误")
        #     print "错误路径:",path      #写文件失败
    print("------read-------")
    print(path)
    print(data)
    return data
path=r'C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101_5555_flow.pickle'
# readInfo(path)
def maxCpu(cpu):
    if len(cpu):
        print "111"
        result = "%.1f" % max(cpu)
        print "2222"
        return str(math.ceil(float(result)*10)) + "%"
    return "0%"
# cpu=['']
# print float(max(cpu))
# maxCpu(cpu)
# s="5.6%"
# s1=float(s.split('%')[0])/100
# print s1


flow= [[109185394], [1116722040]]

def maxFlow(flow):
    if flow[0]:
        maxFlowUp = str(max(flow[0])/1024) + "KB"  # 上行流量
    else:
        maxFlowUp = "0"
    if flow[1]:
        maxFlowDown = str(max(flow[1])/1024) + "KB"  # 下行流量
    else:
        maxFlowDown = "0"
    return maxFlowUp, maxFlowDown
# print maxFlow(flow)
#
# print "%.2f" % max([0.5])
import subprocess,re
def get_men(pkg_name, devices):
    try:
        cmd = "adb -s " +  devices +" shell  dumpsys  meminfo |grep %s" % (pkg_name)
        print(cmd)
        output = subprocess.check_output(cmd).split()
        # print(output)
        # s_men = ".".join([x.decode() for x in output]) # 转换为string
        men2=output[0]
        print"men2:", men2
        # men2 = int(re.findall("TOTAL.(\d+)*", s_men, re.S)[0])
    except:
        men2 = 0
    # if ':'in devices:
    #     devices=devices.replace(':',' ')
    # writeInfo(men2, PATH("../info/" + devices + "_men.pickle"))
    return men2
devices='192.168.179.101:5555'
# print get_men("com.zzl.falcon",devices)


def maxMen(men):
    if len(men):
        # print("men=" + str(men))
        return str(math.ceil((max(men) / 1024))) + "M"
    return "0M"


men=['101551']
print type(max(men))
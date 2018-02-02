# -*- coding: utf-8 -*-
__author__ = "shikun"
import pickle
import os
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def writeSum(init, data=None, path="data.pickle"):
    print "writeSum", __name__
    path = verify_colon(path)
    if init == 0:
        result = data
    else:
        _read = readInfo(path)
        result = _read - 1

    with open(path, 'wb') as f:
        print("------writeSum-------")
        print(result)
        pickle.dump(result, f)


def readSum(path):
    path = verify_colon(path)
    data = {}
    with open(path, 'a+') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
            print("读取文件错误")
    print("------read-------")
    print(path)
    print(data)
    return data

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

def path_wait_exist(path,timeout=16):
    """
    等待路径下文件生产,16秒
    :param path:
    :param timeout:
    :return:
    """
    bflag = False
    i=0
    while not os.path.exists(path):
        print ("等待1秒")
        sleep(1)
        if i==timeout:
            break
        i += 1

def readInfo(path):
    data = []
    path = verify_colon(path)
    with open(path, 'a+') as f:
        try:
            data = pickle.load(f)
            print "data:",data
            # print(data)
        except EOFError:
            data = []
            print("读取文件错误")
            print "错误路径:",path      #写文件失败
    print("------read-------")
    print(path)
    print(data)
    return data


def writeInfo(data, path="data.pickle"):
    print "writeInfo start ------"
    path = verify_colon(path)
    _read = readInfo(path)  #[]
    result = []
    if _read:
        _read.append(data)
        result = _read
    else:
        result.append(data)    #100
    with open(path, 'wb') as f:
        print("------writeInfo-------")
        print(result)
        pickle.dump(result, f)
    print  "writeInfo END------------"

def writeFlowInfo(upflow, downflow, path="data.pickle"):
    print "开始:",__name__
    path=verify_colon(path)
    print("---data-----")
    print("上行流量="+str(upflow))
    print("下行流量="+str(downflow))

    _read = readInfo(path)
    result = [[], []]
    if _read:
        _read[0].append(upflow)
        _read[1].append(downflow)
        result = _read
    else:
        result[0].append(upflow)
        result[1].append(downflow)
    with open(path, 'wb') as f:
        print("------writeFlowInfo-------")
        print(result)
        pickle.dump(result, f)
    print "结束:", __name__

# if __name__ == "__main__":
    # readInfo(PATH("../info/DU2TAN15AJ049163_battery.pickle"))
    # readInfo(PATH("../info/emulator-5554_fps.pickle"))
    # readInfo(PATH("../info/emulator-5554_battery.pickle"))
    # readInfo(PATH("../info/emulator-5554_men.pickle"))
    # readInfo(PATH("../info/DU2TAN15AJ049163_men.pickle"))
    # readInfo(PATH("../info/emulator-5554_flow.pickle"))
    # readInfo("E:\\app\\py\\monkey1\\info\\info.pickle")
    # readInfo(PATH("../info/DU2TAN15AJ049163_cpu.pickle"))
    # devices="192.168.179.101:5555"
    # writeInfo(100, PATH("../info/" + devices + "_battery.pickle"))
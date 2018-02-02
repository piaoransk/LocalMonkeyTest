# -*- coding: utf-8 -*-
import math


# total 是rom容量
def avgMen(men, total):
    if len(men):
        _men = [math.ceil(((men[i]) / total) * 1024) for i in range(len(men))]
        print(_men)
        return str(math.ceil(sum(_men) / len(_men))) + "M"
    return "0"


def avgCpu(cpu):
    if len(cpu):
        resutl = "%.3f" % (sum(cpu) / len(cpu))
        return str(math.ceil(float(resutl)*100)) + "%"
    return "0%"


def avgFps(fps):
    if len(fps):
        return '%.2f' % float(str(math.ceil(sum(fps) / len(fps))))
    return 0.00


def maxMen(men):
    if len(men):
        print("men=" + str(men))
        return str(math.ceil((max(men)) / 1024)) + "M"
    return "0M"


def maxCpu(cpu):
    if len(cpu):
        print "111"
        result = "%.3f" % max(cpu)
        return str(math.ceil(float(result)*100)) + "%"

    return "0%"


def maxFps(fps):
    return str(max(fps))


def maxFlow(flow):
    print("def:maxFlow")
    print(flow)
    _flowUp = []
    _flowDown = []
    # for i in range(len(flow[0])):
    #     if i + 1 == len(flow[0]):
    #         break
    #     _flowUp.append(math.ceil((flow[0][i + 1] - flow[0][i]) / 1024))
    #     print("---maxFlow2222---------")
    #     print(_flowUp)
    # for i in range(len(flow[1])):
    #     if i + 1 == len(flow[1]):
    #         break
    #     _flowDown.append(math.ceil((flow[1][i + 1] - flow[1][i]) / 1024))
    #     print("---maxFlow3333---------")
    #     print(_flowDown)
    if flow[0]:
        maxFlowUp = str(max(flow[0])/1024) + "KB"  # 上行流量
    else:
        maxFlowUp = "0"
    if flow[1]:
        maxFlowDown = str(max(flow[1])/1024) + "KB"  # 下行流量
    else:
        maxFlowDown = "0"
    return maxFlowUp, maxFlowDown

def avgFlow(flow):
    _flowUp = []
    _flowDown = []


    for i in range(len(flow[0])):
        if len(flow[0]) == 1:
            _flowUp.append((flow[0][0]) / 1024)
            break
        if i + 1 == len(flow[0]):
            break
        _flowUp.append((flow[0][i + 1] - flow[0][i])/1024)
    for i in range(len(flow[1])):
        if len(flow[1]) == 1:
            _flowDown.append((flow[1][0]) / 1024)  #如果为1,不用计算
            break
        if i + 1 == len(flow[1]):
            break
        _flowDown.append((flow[1][i + 1] - flow[1][i])/1024)
    # print "定位错误所在:eroDivisionError: integer division or modulo by zero"
    print "_flowUp:", _flowUp
    print "_flowDown:", _flowDown
    avgFlowUp = str(math.ceil(sum(_flowUp) / len(_flowUp))) + "KB"  #问题所在2017年12月9日13:48:23
    avgFlowDown = str(math.ceil(sum(_flowDown) / len(_flowDown))) + "KB"  #为什么flow 的地方出现fps计算,可能是名字定义错误
    return avgFlowUp, avgFlowDown

if __name__ == '__main__':
    flow = [[93919172, 94987124, 96309507], [14250800, 14285269, 14331153]]
    cpu  = [1.9164759725400458, 0.40045766590389015, 0.8493771234428086, 1.8407534246575343]
    men = [310171, 323267, 321179, 317913, 316569, 335277, 323853, 315837, 333765, 333829, 337433, 337473, 339877, 328953, 328881, 328909, 334029, 329873, 334645, 338649, 332541, 329273, 333581]

    print(avgMen(men, 3014000))
    # print(maxFlow(flow))
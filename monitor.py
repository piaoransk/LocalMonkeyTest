# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: monitor.py

@time: 2018/2/5 11:10

@desc:

'''

import subprocess
import re
from wsgiref.validate import validator
import os

def getcpuinfo(devices,packagename):
    """
    安卓7.0
    安卓6.0
    安卓5.0
    安卓4.0
    :param devices:
    :param packagename:
    :return:
    """
    get_cpu_cmd = 'adb -s %s shell "dumpsys cpuinfo | grep %s"' % (devices, packagename)  # 返回百分比
    print "_____cpu_info_____"
    print get_cpu_cmd
    cpu_subprocess = subprocess.Popen(get_cpu_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    cpu_rate = cpu_subprocess.stdout.readline().split()
    print cpu_rate
    if not cpu_rate:
        cpu_rate = ["0%", ]
    print cpu_rate[0]
    return cpu_rate[0]


def getmeninfo(devices, packagename):
    """
    安卓7.0   1000,222KB:
    安卓6.0  ['106723', 'kB:', 'com.android.browser', '(pid', '1834', '/', 'activities)']
    安卓5.0
    安卓4.0

    获取指定包名的memery
    adb shell "dumpsys meminfo | grep packagename"
    :param devices:设备号
    :param packagename:包名
    :return: memery,单位kb
    """
    cmd = 'adb -s %s shell "dumpsys meminfo | grep %s"' % (devices, packagename)  # 返回单位kb
    print cmd
    print "____get meninfo________"
    mem_subprocess = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    men_rate = mem_subprocess.stdout.readline().split()
    print men_rate
    if not men_rate:
        men_rate = ["0", ]
    # memery = men_rate[0].replace(",", "")[:-2]#三星手机7.0
    memory = men_rate[0]
    val_list = ["K:", "k:", ",", "K", "k"]
    for i in val_list :
        memory = val_mem(i, memory)
    return memory


def val_mem(val, memory):
    """
    如果memory包含val,则去掉val
    :param val:
    :param memory:
    :return:memory
    """
    if val in memory:
        memory = memory.replace(val, "")
    return memory



def getbatinfo(devices):
    """
    不是所有android版本都能够查看到app的耗电量
    所以只能查看电池电量了
    get battery info
    adb shell dumpsys batterystats --enable full-wake-history
    adb shell dumpsys batterystats --reset
    adb shell dumpsys battery
    adb shell dumpsys batterystats  com.android.settings | more
    :param devices:
    :param package:
    :return:
    """
    get_battery_cmd = "adb -s " + devices + " shell dumpsys battery"
    bat_subprocess = subprocess.Popen(get_battery_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    bat = bat_subprocess.communicate()
    index=bat[0].index('level')
    battery = bat[0][index:(index+10)].split()[1]
    return battery


def getupflowinfo(devices, package):
    """
    get upload flow info
    :param devices:
    :param package:
    :return:
    """
    pass


def get_flow_new(devices,uid):
    """
    安卓7.0
        example:
        devices 三星手机
        pid 19039
        uid 10156
        adb shell cat /proc/uid_stat/10156/tcp_snd
        adb shell cat /proc/uid_stat/10156/tcp_rcv
    安卓6.0

    安卓5.0
    安卓4.0
    获取较新安卓版本的指定应用的流量信息

    :param uid: string
    :param devices: string
    :return: [rcv,snd](接收流量,发送流量),单位/kb
    """
    cmd_rcv = r"adb -s %s shell cat /proc/uid_stat/%s/tcp_rcv"%(devices,uid)
    cmd_snd = r"adb -s %s shell cat /proc/uid_stat/%s/tcp_snd" % (devices, uid)
    print("----get_flow_new-------")
    print(cmd_rcv)
    rcv = subprocess.Popen(cmd_rcv, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE).stdout.readline()
    snd = subprocess.Popen(cmd_snd, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE).stdout.readline()
    return [rcv.strip(), snd.strip()]


def get_flow(pid, type, devices):
    """
    devices  192.168.179.101:5555
    pid  1740
    uid  10018

    devices 三星手机
    pid 19039
    uid 10156
    单位字节
    adb shell cat /proc/uid_stat/10156/tcp_snd
    adb shell cat /proc/uid_stat/10156/tcp_rcv

    adb -s 192.168.179.101:5555 shell cat /proc/1740/net/dev
    adb shell " ps  | grep com.zzl.falcon.internal"
    adb shell cat /proc/1461/net/dev
    C:\Users\yuhui>adb shell "cat /proc/1462/net/dev"
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
  sit0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
    lo:    1378      24    0    0    0     0          0         0     1378      24    0    0    0     0       0          0
  ifb1:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
  ifb0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
  eth1:  109329     360    0    0    0     0          0         0    54633     365    0    0    0     0       0          0
  eth0: 4599487   48794    0    0    0     0          0         0 74940972   27986    0    0    0     0       0          0



    :param pid:
    :param type:
    :param devices:
    :return: up,down 单位字节
    """
    print "type:", type
    # pid = get_pid(pkg_name)
    upflow = downflow = 0
    if pid is not None:
        cmd = "adb -s " + devices + " shell cat /proc/" + pid + "/net/dev" #adb shell cat /proc/
        print(cmd)
        _flow = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE).stdout.readlines()
        for item in _flow:
            print "每行都数据:",item.split()[0].decode()
            if type == "wifi" and item.split()[0].decode() == "wlan0:":  # wifi
                # 0 上传流量，1 下载流量
                print item
                upflow = int(item.split()[1].decode())
                downflow = int(item.split()[9].decode())
                print("------flow---------")
                print(upflow)
                break
            if type == "gprs" and item.split()[0].decode() == "rmnet0:":  # gprs
                print("-----flow---------")
                upflow = int(item.split()[1].decode())
                downflow = int(item.split()[9].decode())
                print(upflow)
                break
            if type == "vm" and item.split()[0].decode() == "eth0:":  #  virtual_machine
                print("-----flow---------")
                upflow = int(item.split()[1].decode())
                downflow = int(item.split()[9].decode())
                print(upflow)
                break
    print "up:",upflow
    print "down",downflow
    return [upflow,downflow]
    # writeFlowInfo(upflow, downflow, PATH("../info/" + devices + "_flow.pickle"))


def get_fps(pkg_name, devices):
    _adb = "adb -s " + devices +" shell dumpsys gfxinfo %s" % pkg_name
    print(_adb)
    results = os.popen(_adb).read().strip()
    frames = [x for x in results.split('\n') if validator(x)]
    frame_count = len(frames)
    jank_count = 0
    vsync_overtime = 0
    render_time = 0
    for frame in frames:
        time_block = re.split(r'\s+', frame.strip())
        if len(time_block) == 3:
            try:
                render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2])
            except Exception as e:
                render_time = 0

        '''
        当渲染时间大于16.67，按照垂直同步机制，该帧就已经渲染超时
        那么，如果它正好是16.67的整数倍，比如66.68，则它花费了4个垂直同步脉冲，减去本身需要一个，则超时3个
        如果它不是16.67的整数倍，比如67，那么它花费的垂直同步脉冲应向上取整，即5个，减去本身需要一个，即超时4个，可直接算向下取整

        最后的计算方法思路：
        执行一次命令，总共收集到了m帧（理想情况下m=128），但是这m帧里面有些帧渲染超过了16.67毫秒，算一次jank，一旦jank，
        需要用掉额外的垂直同步脉冲。其他的就算没有超过16.67，也按一个脉冲时间来算（理想情况下，一个脉冲就可以渲染完一帧）

        所以FPS的算法可以变为：
        m / （m + 额外的垂直同步脉冲） * 60
        '''
        if render_time > 16.67:
            jank_count += 1
            if render_time % 16.67 == 0:
                vsync_overtime += int(render_time / 16.67) - 1
            else:
                vsync_overtime += int(render_time / 16.67)

    _fps = int(frame_count * 60 / (frame_count + vsync_overtime))
    # if ':'in devices:
    #     devices=devices.replace(':',' ')


    # return (frame_count, jank_count, fps)
    print("-----fps------")
    print(_fps)
    return _fps
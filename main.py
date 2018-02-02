# -*- coding: UTF-8 -*-
"""
cpu_info = ['203,046K:', '234,233K:']
men_info = ['60%', '54%']
battery_info = ['100', '100']
upflow_info = ['552863\r\n', '614020\r\n']
downflow_info = ['7079519\r\n', '7995729\r\n']
"""
import os
import time
import re
import  subprocess
import threading
# devices="192.168.179.101:5555"
# devices = "efc2bb49"
# package="com.android.settings"
package="com.android.browser"
samsung_pkg="com.sec.android.app.sbrowser"

event = threading.Event()  #False初始值
cpu_info = []
men_info = []
battery_info = []
upflow_info = []
downflow_info = []


def start_monkey(cmd):
    # Monkey测试结果日志:monkey_log
    print(cmd)
    event.set()
    subp = subprocess.Popen(cmd,shell=True)
    print "--------------"
    subp.wait()
    event.clear()
    # # Monkey时手机日志,logcat
    # logcatname = log + r"logcat.log"
    # cmd2 = "adb logcat -d >%s" % (logcatname)
    # os.popen(cmd2)
    #
    # # "导出traces文件"
    # tracesname = log + r"traces.log"
    # cmd3 = "adb shell cat /data/anr/traces.txt>%s" % tracesname
    # os.popen(cmd3)


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
    memery = men_rate[0].replace(",", "")  #6.0
    return memery


def getsysinfo(devices, pkg, uid):
    """
    获取设备的cpu,men,battery,upflow,downflow
    """
    # os.remove("cpu_rate.txt")
    # print ("cpu1:" + str(event.isSet()))
    event.wait()    #等待主进程,monkey
    # print ("cpu2:"+str(event.isSet()))
    while event.isSet():
        time.sleep(1)
        print "start:",time.ctime()
        # with open("cpu_rate.txt","a+") as f:
        #     f.write(time.ctime()+" "+cpu_rate[0] + " \n")
        # print (time.ctime()+" "+cpu_rate[0] + " \n")
        start=time.ctime()
        pid = get_pid(pkg, devices)
        print "pid:  ",pid
        cpu_info.append(getcpuinfo(devices, pkg))
        cpu_infoTime = time.ctime()
        # time_escape=cpu_infoTime-start
        # print "时间差:",time_escape
        print "cpu_info:",cpu_infoTime
        men_info.append(getmeninfo(devices, pkg))
        print "men_info:", time.ctime()
        battery_info.append(getbatinfo(devices))
        print "battery_info:", time.ctime()
        flow=get_flow_new(devices, uid)
        upflow_info.append(flow[1])
        print "upflow_info:", time.ctime()
        downflow_info.append(flow[0])
        print "downflow_info:", time.ctime()
    return cpu_info, men_info

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


def get_flow(pid,type, devices):
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
    :return:
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
            print item
            if type == "wifi" and item.split()[0].decode() == "wlan0:":  # wifi
                # 0 上传流量，1 下载流量
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
            if type == "virtual_machine" and item.split()[0].decode() == "eth0:":  # eth0
                print("-----flow---------")
                upflow = int(item.split()[1].decode())
                downflow = int(item.split()[9].decode())
                print(upflow)
                break
    print "up:",upflow_info.append(upflow)
    print "down",downflow_info.append(downflow)
    # writeFlowInfo(upflow, downflow, PATH("../info/" + devices + "_flow.pickle"))


def getdownflowinfo(devices, package):
    """
    get
    :param devices:
    :param package:
    :return:
    """
    pass

def get_pid(pkg_name, devices):
    """

    :param pkg_name:
    :param devices:
    :return:
    """
    cmd = "adb -s " + devices + " shell ps | findstr " + pkg_name
    print("----get_pid-------")
    print(cmd)
    pid = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE).stdout.readlines()
    for item in pid:
        if item.split()[8].decode() == pkg_name:
            return item.split()[1].decode()

def get_uid(pkg_name, devices):
    """
    get uid from adb cmd
    adb cmd script : adb shell dumpsys package com.android.browser  | findstr userId=
    :param pkg_name:
    :param devices:
    :return:uid
    """
    cmd = "adb -s %s shell dumpsys package %s | findstr userId=" % (devices, pkg_name)
    print("----get_uid-------")
    print(cmd)
    uid = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE).stdout.readline()
    uid_1 = uid.split()[0].split("=")[1]
    print "uid :",uid_1
    return uid_1

def kill_adb_port():
    pass

def star_adb_port():
    pass

def clear_logcat():
    pass

def check_devices():
    pass

def get_hw_info():
    #获取设备的硬件信息
    pass

def report():
    #收集csv 生成html报告
    pass


import AdbCommon


if __name__ == '__main__':
    print time.ctime()
    # kill_adb_port()
    # star_adb_port()
    # clear_logcat()
    # #1.查看设备是否正常
    # check_devices()
    # #2.收集设备信息
    # get_sys_info()#获取设备的硬件信息
    # #3.打开查看器:收集cpu,mem,battery,wifi信息;logcat
    # get_running_info("on")
    # #4.run:py脚本
    # run(start_monkey,monkey_cmd)    #monkey运行结束,get_running_info也要结束
    # #5.收集信息,出report--html
    # report()#收集csv 生成html报告
    # ____________________________________________________________________________
    pkg=package
    devices = AdbCommon.getdevices()[0]
    print "pkg: ,"+pkg
    print "devices , "+devices
    uid=get_uid(pkg, devices)
    monkey_cmd_str='adb -s %s shell monkey -p %s -v 500 > moonkey_log.log'%(devices,pkg)
    thread1 = threading.Thread(target=start_monkey, args=(monkey_cmd_str,))  #主函数
    thread2 = threading.Thread(target=getsysinfo, args=(devices,pkg, uid))    #次要的,主函数运行,就运行;主函数关闭,就关闭
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    print "Print system info after test is end!"
    print men_info
    print cpu_info
    print battery_info
    print upflow_info
    print downflow_info
    # ____________________________________________________________________________
    # devices1=AdbCommon.getdevices()
    # if devices1:
    #     devices=devices1[0]
    # pid=get_pid(samsung_pkg,devices)
    # # get_flow(pid,"wifi", devices)
    # uid=get_uid(samsung_pkg,devices)
    # print get_flow_new(uid,devices)
    print time.ctime()
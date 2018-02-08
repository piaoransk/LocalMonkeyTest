# -*- coding: UTF-8 -*-
"""
cpu,内存,电池,上行流量,下行流量
fps
魅蓝
['40438', '43201', '42345', '42539', '46071', '50881']
['0%', '1.9%', '20%', '24%', '34%', '48%']
['84', '84', '84', '84', '84', '84']
[4911373, 4918556, 4921684, 4925113, 4928966, 4929616]
[140419039, 140437296, 140440648, 140445389, 140452925, 140454306]
[60, 60, 60, 60, 60, 60]
"""
import AdbCommon
import monitor
import os
from wsgiref.validate import validator
import time
import re
import  subprocess
import threading
from data import writeJson
from report import Report

# devices="192.168.179.101:5555"
devices = "efc2bb49"
# package="com.android.settings"
package="com.android.browser"
samsung_pkg="com.sec.android.app.sbrowser"

event = threading.Event()  #False初始值
cpu_info = []
men_info = []
battery_info = []
upflow_info = []
downflow_info = []
fps_info = []
time_list = []


def install_apk():
    pass


def uninstall_apk():
    pass


def login():
    pass


def stop_monkey(device):
    pid=AdbCommon.get_pid( "monkey", device)
    return AdbCommon.kill_pid(device, pid)


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


def getsysinfo(device, pkg, uid, type_flow ):
    """
    获取设备的cpu,men,battery,upflow,downflow
    :param device:
    :param pkg:
    :param uid:
    :param type:
    :return:
    """
    event.wait()    #等待主进程,monkey
    # print ("cpu2:"+str(event.isSet()))
    while event.isSet():
        time.sleep(1)
        time_stamp = time.strftime('%H:%M:%S', time.localtime(time.time()))
        print "start:",time_stamp
        time_list.append(time_stamp)
        # with open("cpu_rate.txt","a+") as f:
        #     f.write(time.ctime()+" "+cpu_rate[0] + " \n")
        # print (time.ctime()+" "+cpu_rate[0] + " \n")
        start=time.ctime()
        pid = AdbCommon.get_pid(pkg, device)
        print "pid:  ", pid
        cpu_info.append(monitor.getcpuinfo(device, pkg))
        cpu_infoTime = time.ctime()
        # time_escape=cpu_infoTime-start
        # print "时间差:",time_escape
        print "cpu_info:",cpu_infoTime
        men_info.append(monitor.getmeninfo(device, pkg))
        print "men_info:", time.ctime()
        battery_info.append(monitor.getbatinfo(device))
        print "battery_info:", time.ctime()
        # flow=get_flow_new(devices, uid)
        flow = monitor.get_flow(pid, type_flow, device)#"wifi"
        upflow_info.append(flow[1])
        print "upflow_info:", time.ctime()
        downflow_info.append(flow[0])
        print "downflow_info:", time.ctime()
        fps_info.append(monitor.get_fps(pkg, device))
        print "fps_info:", time.ctime()
    return cpu_info, men_info


def getdownflowinfo(devices, package):
    """
    get
    :param devices:
    :param package:
    :return:
    """
    pass


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


def run(pkg, times, type_flow):
    """

    :param pkg:
    :param times:
    :param type_flow: wifi,vm
    :return:
    """
    device = AdbCommon.getdevices()[0]
    print "pkg: ," + pkg
    print "devices , " + device
    uid = AdbCommon.get_uid(pkg, device)
    monkey_cmd_str = 'adb -s %s shell monkey -p %s -v %s > moonkey_log.log' % (device, pkg,times)
    thread1 = threading.Thread(target=start_monkey, args=(monkey_cmd_str,))  # 主函数
    # 次要的,主函数运行,就运行;主函数关闭,就关闭
    thread2 = threading.Thread(target=getsysinfo, args=(device, pkg, uid, type_flow))
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()
    print "Print system info after test is end!"
    # print men_info
    # print cpu_info
    # print battery_info
    # print upflow_info
    # print downflow_info
    # print fps_info
    # print time_list
    #timestr, cpu, memory,  upflow,downflow, fps, battery
    res_list= [time_list, cpu_info, men_info, upflow_info, downflow_info, fps_info, battery_info ]
    print res_list
    return res_list


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
    # pkg=package
    result = run("com.zzl.falcon.internal", "500", "vm")
    #[men_info, cpu_info, battery_info, upflow_info, downflow_info, fps_info, time_list]
    jsondata = writeJson.generate_main_json_str(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
    writeJson.write_json("./data/datatest.json", jsondata)
    # report = Report()
    # print report.get_monkey_crash_msg("moonkey_log_backup.log")
    # ____________________________________________________________________________
    # devices1=AdbCommon.getdevices()
    # if devices1:
    #     devices=devices1[0]
    # pid=get_pid(samsung_pkg,devices)
    # # get_flow(pid,"wifi", devices)
    # uid=get_uid(samsung_pkg,devices)
    # print get_flow_new(uid,devices)
    # print get_fps(samsung_pkg,devices)
    print time.ctime()
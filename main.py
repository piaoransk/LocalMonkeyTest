# -*- coding: UTF-8 -*-
import os,monkey_cmd
import re
devices="192.168.179.101:5555"
def run():
    #start logcat
    #
    result = os.system(monkey_cmd.monkey_log_cmd)
    print result

def getsysinfo():
    # output = os.popen(monkey_cmd.getprop_cmd).read()
    # # print '900000'
    # # print output
    # # print '1111'
    # # print type(output)
    # # version = re.findall(r"[ro.build.version.release]: [5.1]", output)
    # index=output.find('[ro.build.version.release]')
    # version= output[(index+27):(index+34)]
    # print version
    cmd='adb shell getprop'
    pass

def getcpuinfo(devices):
    """
    C:\Users\yuhui>adb shell "dumpsys cpuinfo | grep com.zzl.falcon"
    0.1% 2687/com.zzl.falcon.internal: 0% user + 0.1% kernel / faults: 98 minor
    :return:
    """
    get_cpu_cmd = 'adb -s %s shell "dumpsys cpuinfo | grep com.zzl.falcon"' % devices
    cpu_rate=os.popen(get_cpu_cmd).read().split()
    # print type(cpu_rate[0])
    return cpu_rate[0]

def getmeninfo():
    """
    adb shell "dumpsys meminfo | grep com.zzl.falcon"
    :return:
    """
    pass

def getflow():
    """
    adb shell "cat /proc/uid_stat/10068/tcp_snd"
    :return:
    """
    pass


if __name__ == '__main__':
    #kill adb port
    #star adb port
    #clear logcat
    #1.查看设备是否正常
    #2.收集设备信息
    #3.打开查看器:收集cpu,mem,battery,wifi信息;logcat
    #4.run:py脚本
    #5.收集信息,出report--html
    #jiajia2 ,flask
    # getsysinfo()
    print getcpuinfo(devices)

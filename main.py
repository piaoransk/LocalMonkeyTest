# -*- coding: UTF-8 -*-
import os,monkey_cmd
import re

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

def getcpuinfo():
    """
    C:\Users\yuhui>adb shell "dumpsys cpuinfo | grep com.zzl.falcon"
    0.1% 2687/com.zzl.falcon.internal: 0% user + 0.1% kernel / faults: 98 minor
    :return:
    """
    cpuinfo_cmd='adb shell "dumpsys cpuinfo | grep com.zzl.falcon"'
    os.popen(cpuinfo_cmd).read()
def getmeninfo():
    pass


if __name__ == '__main__':
    #kill adb port
    #star adb port
    #clear logcat

    # run()
    getsysinfo()


# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: thread_util.py

@time: 2017/11/29 16:12

@desc:

'''

import threading,time

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
    cmd="adb shell dumpsys cpuinfo  grep com.zzl.falcon"
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

# getcpuinfo()
# getmeminfo()
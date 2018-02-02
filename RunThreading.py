# -*- coding: UTF-8 -*-
'''

@author: yuhuixu

@file: RunThreading.py

@time: 2018/1/22 17:15

@desc:简单实现多线程读写两个文件

'''


# from docutils.nodes import target
import threading
import time
import os

event_flag = threading.Event()


def Loop1():
    i=0
    event_flag.wait()
    while event_flag.isSet():
        print "L1 : ", i
        i+=1
        time.sleep(1)
        name = threading.current_thread().name
        with open("Loop1.txt", "a+") as f:
            f.write(time.ctime() + "-Loop1-" + "-i-" + str(i) + ":" + name + "\n")


def Loop2():
    i = 0
    for i in range(10):
        event_flag.set()
        print "L2 : " ,i
        i += 1
        time.sleep(1)
        name = threading.current_thread().name
        with open("Loop2.txt", "a+") as f:
            f.write(time.ctime() + "-Loop2-" + "-i-" + str(i) + ":" + name + "\n")
    event_flag.clear()

# os.remove("Loop2.txt")
# os.remove("Loop1.txt")
thread2=threading.Thread(target=Loop2, name="Loop2Name")
thread1=threading.Thread(target=Loop1, name="Loop1Name")
thread1.start()
thread2.start()


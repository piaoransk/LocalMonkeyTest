# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: adbcommon.py

@time: 2018/1/29 15:16

@desc:

'''

import os


def getdevices():
    """
    get a list of devices
    :return:  list: ['efc2bb49', '192.168.179.101:5555']
    """
    cmd = "adb devices"
    filter_str = "\tdevice\n"
    cmd_result = os.popen(cmd).readlines()
    print cmd_result
    devices=[]
    for i in cmd_result:
        if filter_str in i:
            devices.append(i.split(filter_str)[0])
    print "getdevices(): ", devices
    return devices


class AdbCommon(object):
    """
    adb common functions
    usage:
    adb=AdbCommon(devices)

    """
    def __init__(self, devices):
        self.devices = devices

    def call_adb(self, command):
        command_result = ''
        command_text = 'adb -s %s %s' % (self.devices, command)
        print(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep " + pkg_name)
        # print(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # print(result[4])
        return result[4]

# print getdevices()
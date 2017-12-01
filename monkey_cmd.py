# -*- coding: UTF-8 -*-
#!/usr/bin/env python
'''

@author: yuhuixu

@file: monkey_cmd.py

@time: 2017/11/22 15:23

@desc: 存放monkey 命令

'''

monkey_cmd='adb shell monkey -p com.android.settings  -v 500'
monkey_log_cmd='adb shell monkey -p com.android.settings  -v 500 > moonkey_log.log'
logcat_cmd='adb shell logcat -d -v time >logcat.log'
getprop_cmd='adb shell getprop'
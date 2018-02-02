2017年12月9日13:20:12
需要handle flow type, wifi 和genymotion 的区别
net== wifi     #wlan0
vm = virtual machine    #eth0

2017年12月2日17:09:52
C:\Python27\python.exe "C:\Program Files\JetBrains\PyCharm 2017.2\helpers\pydev\pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 12326 --file C:/Users/yuhui/Documents/GitHub/monkeyTest/monkeyTest.py
pydev debugger: process 15964 is connecting

Connected to pydev debugger (build 172.3317.103)
======================
*** liyu 2015-01-15***
***     v1.0.0     ***
======================
---------------------------
Checking adb port...
???: ????? PID ? 8184 ??????
????: ?????????? "8184"??
????: ?????????? "8184"??
????: ?????????? "12904"??
????: ?????????? "8588"??
---------------------------
adb port has been released!
---------------------------
adb devices
['192.168.179.101:5555']
[{'num': 1, 'devices': '192.168.179.101:5555'}]
devices: 192.168.179.101:5555
adb -s 192.168.179.101:5555 shell wm size
adb -s 192.168.179.101:5555 shell cat /proc/meminfo
adb -s 192.168.179.101:5555 shell 'getprop'
adb -s 192.168.179.101:5555 shell cat /proc/cpuinfo
创建文件成功
创建文件成功
文件已经存在
创建文件成功
创建文件成功
创建文件成功
创建文件成功
------writeSum-------
1
adb -s 192.168.179.101:5555 shell monkey -p com.zzl.falcon.internal -v 500>C:\Users\yuhui\Documents\GitHub\monkeyTest\log\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log
----get_pid-------
adb -s 192.168.179.101:5555 shell ps | findstr com.zzl.falcon.internal
adb -s 192.168.179.101:5555 shell cat /proc/cpuinfo
adb -s 192.168.179.101:5555 shell dumpsys battery
Current.Battery.Service.state:.AC.powered:.true.USB.powered:.false.Wireless.powered:.false.status:.5.health:.1.present:.true.level:.100.scale:.100.voltage:.10000.temperature:.0.technology:.Unknown
修改前地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101:5555_battery.pickle
修改后地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_battery.pickle
[100, 100, 100, 100]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_battery.pickle
[100, 100, 100, 100]
------writeInfo-------
[100, 100, 100, 100, 100]
start------------123
star()----1
adb -s 192.168.179.101:5555 shell cat /proc/1574/stat
utime=1396
stime=1757
cutime=0
cstime=0
processCpuTime=3153
adb -s 192.168.179.101:5555 shell cat /proc/1574/stat
utime=1396
stime=1757
cutime=0
cstime=0
processCpuTime=3153
adb -s 192.168.179.101:5555 shell cat /proc/stat
user=7347
nice=116
system=23761
idle=4111723
iowait=760
irq=0
softirq=968
totalCpuTime4144675
adb -s 192.168.179.101:5555 shell cat /proc/stat
user=7348
nice=116
system=23764
idle=4112137
iowait=760
irq=0
softirq=968
totalCpuTime4145093
totalCpuTime3=1672
processCpuTime3=0
修改前地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101:5555_cpu.pickle
修改后地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_cpu.pickle
[0]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_cpu.pickle
[0]
------writeInfo-------
[0, 0]
--------cpu--------
0
adb -s 192.168.179.101:5555 shell  dumpsys  meminfo com.zzl.falcon.internal
Applications.Memory.Usage.(kB):.Uptime:.10465119.Realtime:.10465119.**.MEMINFO.in.pid.1574.[com.zzl.falcon.internal].**.Pss.Private.Private.Swapped.Heap.Heap.Heap.Total.Dirty.Clean.Dirty.Size.Alloc.Free.------.------.------.------.------.------.------.Native.Heap.19489.19412.0.0.45056.30030.15025.Dalvik.Heap.19374.19312.0.0.23864.16503.7361.Dalvik.Other.592.592.0.0.Stack.620.620.0.0.Ashmem.13844.13724.0.0.Other.dev.8.0.8.0..so.mmap.31108.292.25724.0..apk.mmap.935.0.220.0..ttf.mmap.3101.0.380.0..dex.mmap.11546.0.5712.0..oat.mmap.5735.0.900.0..art.mmap.1838.1372.40.0.Other.mmap.1260.4.1052.0.Unknown.13765.13764.0.0.TOTAL.123215.69092.34036.0.68920.46533.22386.Objects.Views:.788.ViewRootImpl:.2.AppContexts:.12.Activities:.9.Assets:.3.AssetManagers:.3.Local.Binders:.22.Proxy.Binders:.35.Parcel.memory:.10.Parcel.count:.42.Death.Recipients:.1.OpenSSL.Sockets:.0.SQL.MEMORY_USED:.309.PAGECACHE_OVERFLOW:.80.MALLOC_SIZE:.62.DATABASES.pgsz.dbsz.Lookaside(b).cache.Dbname.4.20.29.1/40/2./data/user/0/com.zzl.falcon.internal/databases/accs.db.4.56.14.0/39/1./data/user/0/com.zzl.falcon.internal/databases/MsgLogStore.db.4.36.25.48/41/3./data/user/0/com.zzl.falcon.internal/databases/MessageStore.db
修改前地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101:5555_men.pickle
修改后地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_men.pickle
[118259, 119240]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_men.pickle
[118259, 119240]
------writeInfo-------
[118259, 119240, 123215]
adb -s 192.168.179.101:5555 shell dumpsys gfxinfo com.zzl.falcon.internal
修改前地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101:5555_fps.pickle
修改后地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_fps.pickle
[60, 60]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_fps.pickle
[60, 60]
------writeInfo-------
[60, 60, 60]
-----fps------
60
adb -s 192.168.179.101:5555 shell cat /proc/1574/net/dev
---data-----
上行流量=0
下行流量=0
读取文件错误
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_flow.pickle
[]
------writeFlowInfo-------
[[0], [0]]
adb -s 192.168.179.101:5555 shell dumpsys battery
Current.Battery.Service.state:.AC.powered:.true.USB.powered:.false.Wireless.powered:.false.status:.5.health:.1.present:.true.level:.100.scale:.100.voltage:.10000.temperature:.0.technology:.Unknown
修改前地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101:5555_battery.pickle
修改后地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_battery.pickle
[100, 100, 100, 100, 100]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_battery.pickle
[100, 100, 100, 100, 100]
------writeInfo-------
[100, 100, 100, 100, 100, 100]
192.168.179.101:5555测试完成咯
0
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\sumInfo.pickle
0
------writeSum-------
-1
adb -s 192.168.179.101:5555 shell dumpsys battery
Current.Battery.Service.state:.AC.powered:.true.USB.powered:.false.Wireless.powered:.false.status:.5.health:.1.present:.true.level:.100.scale:.100.voltage:.10000.temperature:.0.technology:.Unknown
修改前地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101:5555_battery.pickle
修改后地址:C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_battery.pickle
[100, 100, 100, 100, 100, 100]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_battery.pickle
[100, 100, 100, 100, 100, 100]
------writeInfo-------
[100, 100, 100, 100, 100, 100, 100]
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\info.pickle
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
------writeInfo-------
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}, {'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'afterBattery': 100, 'beforeBattery': 100, 'pix': u'768x1280', 'time': '173\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
-1
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\sumInfo.pickle
-1
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'afterBattery': 100, 'beforeBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}, {'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '173\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\info.pickle
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'afterBattery': 100, 'beforeBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}, {'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '173\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'afterBattery': 100, 'beforeBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}, {'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '173\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'afterBattery': 100, 'beforeBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}, {'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '173\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\info.pickle
[{'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\728e78a8-e303-41f6-8d8c-ead05cc73468monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'afterBattery': 100, 'beforeBattery': 100, 'pix': u'768x1280', 'time': '5\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}, {'192.168.179.101:5555': {'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle', 'men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle', 'flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\63c54951-f0d7-4b4c-8451-28e4ee680116monkey.log', 'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 100, 'afterBattery': 100, 'pix': u'768x1280', 'time': '173\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}]
[0, 0]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_cpu.pickle
[0, 0]
[118259, 119240, 123215]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_men.pickle
[118259, 119240, 123215]
[60, 60, 60]
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_fps.pickle
[60, 60, 60]
读取文件错误
------read-------
C:\Users\yuhui\Documents\GitHub\monkeyTest\info\192.168.179.101 5555_flow.pickle
[]
----wrap-----
[]
maxCpu=[0, 0]
men=[118259, 119240, 123215]
[0.0, 0.0, 0.0]
---maxFlow111----------
[]
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm 2017.2\helpers\pydev\pydevd.py", line 1596, in <module>
    globals = debugger.run(setup['file'], None, None, is_module)
  File "C:\Program Files\JetBrains\PyCharm 2017.2\helpers\pydev\pydevd.py", line 1023, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "C:/Users/yuhui/Documents/GitHub/monkeyTest/monkeyTest.py", line 172, in <module>
    runnerPool()
  File "C:/Users/yuhui/Documents/GitHub/monkeyTest/monkeyTest.py", line 93, in runnerPool
    pool.map(start, devices_Pool)
  File "C:\Python27\lib\multiprocessing\pool.py", line 251, in map
    return self.map_async(func, iterable, chunksize).get()
  File "C:\Python27\lib\multiprocessing\pool.py", line 567, in get
    raise self._value
IndexError: list index out of range

Process finished with exit code 1

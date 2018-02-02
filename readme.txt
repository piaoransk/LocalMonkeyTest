前端
canvas 折线图



Android应用性能测试之CPU和内存占用
http://blog.csdn.net/yzl11/article/details/51952743
贝尔在线activity
com.zzl.falcon.internal/com.zzl.falcon.MainActivity
获取cpu,men
dumpsys meminfo | grep com.zzl.falcon

多线程
threading
multiprocessing



1）adb shell （进入linux的底层）
2）echo 3>/proc/sys/vm/drop_caches （清除一下系统cache）
3）top -d 1 | grep com.baidu.BaiduMap （以百度地图为例，每一秒打印一次资源利用情况）
top -d 1 | grep com.zzl.falcon.internal



 PID PR CPU% S  #THR     VSS     RSS PCY UID      Name
  278  0   1% S    23 122484K   8856K  fg root     /system/bin/local_opengl
  912  0   1% S    13  66172K   4900K  fg system   /system/bin/surfaceflinger
 2687  0   1% S    38 1061252K 122704K  fg u0_a99   com.zzl.falcon.internal
 2894  0   0% R     1  11984K   2000K  fg root     top
  882  0   0% S    78 1139744K 130624K  fg system   system_server
    7  1   0% S     1      0K      0K  fg root     rcu_preempt
    9  0   0% S     1      0K      0K  fg root     rcu_bh
   10  0   0% S     1      0K      0K unk root     migration/0
   11  1   0% S     1      0K      0K unk root     migration/1
   12  1   0% S     1      0K      0K  fg root     ksoftirqd/1



top  | grep app名称
ps  |  grep app名称
procrank | grep app名称
dumpsys meminfo app名称
前两个命令只能查到VSS RSS内存占用信息
而后面两个命令可以查出  PSS USS内存占用.
dumpsys meminfo 可以查出native和dalvik分别占用多少内存
dumpsys 用来给出手机中所有应用程序的信息，并且也会给出现在手机的状态。
dumpsys [Option]
               meminfo 显示内存信息
               cpuinfo 显示CPU信息
               account 显示accounts信息
               activity 显示所有的activities的信息
               window 显示键盘，窗口和它们的关系
               wifi 显示wifi信息



adb shell dumpsys cpuinfo | grep  com.zzl.falcon.internal

nokia root方案
https://www.ithome.com/html/android/328333.htm
https://forum.xda-developers.com/nokia-8/development/nokia-8-official-firmware-links-updated-t3678487
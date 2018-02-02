# -*- coding: utf-8 -*-
import os
import xlsxwriter
from Base import BaseReport


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def report(info):
    print "info:",info
    workbook = xlsxwriter.Workbook('report.xlsx')
    bo = BaseReport.OperateReport(workbook)
    bo.monitor(info)
    bo.crash()
    bo.analysis(info)
    bo.close()

def report1(info):
    #dic={'192.168.179.101:5555':{'battery': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_battery.pickle','men': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_men.pickle','flow': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_flow.pickle', 'header': {'monkey_log': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\log\\725748ae-127f-4386-b7eb-f95d851b5806monkey.log', 			'kel': '4\xe6\xa0\xb8', 'rom': 2051740, 'beforeBattery': 99, 'afterBattery': 99, 'pix': u'768x1280', 'time': '26\xe7\xa7\x92', 'net': u'wifi', 'phone_name': u'.geny-def]:_.geny-def]:_]:'}, 'fps': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_fps.pickle', 'cpu': 'C:\\Users\\yuhui\\Documents\\GitHub\\monkeyTest\\info\\192.168.179.101:5555_cpu.pickle'}}
    print "info:",info
    workbook = xlsxwriter.Workbook('report.xlsx')
    bo = BaseReport.OperateReport(workbook)
    bo.monitor(info)
    bo.crash()
    bo.analysis(info)
    bo.close()

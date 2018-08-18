# -*- coding: utf-8 -*-
# 时间：2018/5/17 21:15
# 作者：lhz
# 邮箱：lhzlovecplusplus@163.com
import psutil

ps_list = []
# 获取目前进程
count = 0
processInfo = {}
for pid in psutil.pids():
    try:
        ps = psutil.Process(pid)
        processInfo.update({pid: [{
            'name': ps.name(), 'exe_path': ps.exe(), 'usedPath': ps.cwd()
        }]})
        #print "{\n name:%s \n path:%s \n usedPath:%s \n}" % (ps.name(),ps.exe(),ps.cwd())
    except:
        continue

for psinfo in processInfo[1408]:
    print psinfo

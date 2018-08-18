# -*- coding: utf-8 -*-
# 时间：2018/5/17 10:45
# 作者：lhz
# 邮箱：lhzlovecplusplus@163.com

import psutil
import datetime
#放进程对象
ps_list = []
for pid in psutil.pids():
    ps_list.append(psutil.Process(pid))

# 用户列表
user_list = psutil.users()
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
print boot_time

#内存相关
mem = psutil.virtual_memory()
#
swap_mem = psutil.swap_memory()
print mem
print swap_mem
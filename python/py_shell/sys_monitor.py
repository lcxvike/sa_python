#!/usr/bin/python2.7

import psutil
class sys_analyze(self)
    def 
###cpu analyze
def cpu_analyze()
    per_5_cpu     = psutil.cpu_percent(interval=5)
    per_5_cpu_val = psutil.cpu_percent(interval=5,percpu=True)
    cpu_logi_cnt  = psutil.cpu_count(logical=True)

    print per_5_cpu
    print per_5_cpu_val
    print cpu_logi_cnt

##mem analyze
def mem_analyze()
    mem = psutil.virtual_memory()
    print mem.total,mem.used

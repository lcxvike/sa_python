#!/usr/bin/python2.7

import sys
import os
import time,datetime


dir1=/export/log

#delete logfile
logdir=/tmp
logfile=os.path.join(logdir,'delete.log')
time.strftime(r"%Y-%m-%d",time.localtime())

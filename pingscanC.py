#!/bin/env python
###################################################################################
#  Tom Angle
#
#  This script is to do a ping scan on a class C network.
#
#  Usage: pingscanC.py
#
###################################################################################

import os
import re
import time
import sys
from threading import Thread

ipstart = '10.0.0.1'
ipend = '10.0.0.254'

class runit(Thread):
    def __init__ (self,ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = -1
    def run(self):
        if sys.platform == 'win32':
            pcmd = os.popen("ping -n 2 -w 2 "+self.ip,"r")
        else:
            pcmd = os.popen("ping -q -c2 "+self.ip,"r")          
        while 1:
            line = pcmd.readline()
            if not line:
                break
            preturn = re.findall(runit.lifeline,line)
            if preturn:
                self.status = int(preturn[0])

if sys.platform == 'win32':
    runit.lifeline = re.compile(r"Received = (\d)")
else:
    runit.lifeline = re.compile(r"(\d) received")
    
report = ("No response","Partial Response","Alive")

print time.ctime()

pinglist = []

startoct = int(ipstart.split('.')[3])
endoct = int(ipend.split('.')[3]) + 1
octs = ipstart.split('.')[0] + '.' + ipstart.split('.')[1] + '.' + ipstart.split('.')[2]


for host in range(startoct,endoct):
    ip = octs + '.' + str(host)
    current = runit(ip)
    pinglist.append(current)
    current.start()

for pitems in pinglist:
    pitems.join()
    print "Status: ",pitems.ip,"is",report[pitems.status]

print time.ctime()

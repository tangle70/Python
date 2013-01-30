#!/bin/env python
###################################################################################
#
# A sctipt to list files in an FTP directory.
#
###################################################################################
import os
import sys
import string
import time
import random
import struct
import sys
import ftplib
from socket import gethostname

def listFiles(host, uname, upass):
    ftp = ftplib.FTP()
    ftp.connect(host, '21')
    ftp.login(uname, upass)
    ftp.cwd('~')
    lines = []
    ftp.retrlines('LIST', lines.append)
    ftp.quit()
    x = 0
    print host
    for item in lines:
        print item

#-------------------------------------------------------#

sname = ['gr450','gr452']#sys.argv[0]
uname = 'root'
upass = 'gbms4'
flist = []

# List file on server
for host in sname:
    listFiles(host, uname, upass)

#!/bin/env/python
###################################################################################
#  Tom Angle
#
#  A script to list files in a directory using via SSH using the paramiko 
#  module.
#
###################################################################################

import paramiko

def listFiles(srv, uname, passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(srv, username=uname, password=passwd)

        stdin, stdout, stderr = ssh.exec_command('ls')
        stdin.flush()
        data = stdout
        x = 0
        print '################################################'
        print srv
        for line in data:
            line = line.replace('\n','')
            print '    ', line
    except:
        print '################################################'
        print 'ERROR: conencting to', srv

srv = 'srv'
uname = 'uname'
passwd = 'passwd'
listFiles(srv,uname,passwd)
print '################################################'

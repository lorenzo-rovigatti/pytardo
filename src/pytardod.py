#!/usr/bin/env python
'''
Created on 18 mag 2018

@author: lorenzo
'''

import sys
from daemon.pidfile import TimeoutPIDLockFile
import daemon
from pytardo import p

if __name__ == '__main__':
    pidfile = TimeoutPIDLockFile("/var/run/pytardo.pid")
    daemon_context = daemon.DaemonContext(
        stdout=sys.stdout,
        pidfile=pidfile
    )
    
    with daemon_context:
        p.poll()
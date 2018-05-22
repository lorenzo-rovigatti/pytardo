#!/usr/bin/env python
'''
Created on 18 mag 2018

@author: lorenzo
'''

from daemon.pidfile import TimeoutPIDLockFile
import daemon
from pytardo import pytardo

if __name__ == '__main__':
    pidfile = TimeoutPIDLockFile("/var/run/pytardo.pid")
    output_file = open("/var/log/pytardo.log", "a+")
    daemon_context = daemon.DaemonContext(
        stdout=output_file,
        stderr=output_file,
        pidfile=pidfile
    )
    
    pytardo_poller = pytardo()
    with daemon_context:
        pytardo_poller.poll()
        
    output_file.close()
    
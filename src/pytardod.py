#!/usr/bin/env python
'''
Created on 18 mag 2018

@author: lorenzo
'''

import sys
from daemon.pidfile import TimeoutPIDLockFile
import daemon
import initialiser

if __name__ == '__main__':
    pidfile = TimeoutPIDLockFile("/var/run/pytardo.pid")
    daemon_context = daemon.DaemonContext(
        stdout=sys.stdout,
        pidfile=pidfile
    )
    p = initialiser.init_from_config_file(sys.argv[1])
    
    with daemon_context:
        p.poll()
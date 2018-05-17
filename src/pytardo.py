#!/usr/bin/env python
'''
Created on 17 mag 2018

@author: lorenzo
'''

import poller
import daemon
import sys

if __name__ == '__main__':
    with daemon.DaemonContext(stdout=sys.stdout) as daemon_context:
        p = poller.Poller("/dev/ttyUSB0", 1)
        p.poll()

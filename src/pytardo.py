#!/usr/bin/env python
'''
Created on 17 mag 2018

@author: lorenzo
'''

import poller
import loggers

file_logger = loggers.FileLogger("prova.dat")
p = poller.Poller("/dev/ttyUSB0", 1)
p.add_logger(file_logger)

if __name__ == '__main__':
    p.poll()

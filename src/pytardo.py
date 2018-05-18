#!/usr/bin/env python
'''
Created on 17 mag 2018

@author: lorenzo
'''

import poller
import loggers
import monitor
import callbacks

p = poller.Poller("/dev/ttyUSB0", 1)

file_logger = loggers.FileLogger("prova.dat", True)
p.add_logger(file_logger)

conditions = ["T1 > 20"]
callback = callbacks.WriteToFile("warnings.dat", True)
monitor = monitor.Monitor(conditions)
monitor.add_warning_callback(callback)
p.add_monitor(monitor)

if __name__ == '__main__':
    p.poll()

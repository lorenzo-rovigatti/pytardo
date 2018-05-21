'''
Created on 17 mag 2018

@author: lorenzo
'''

import serial
from time import sleep


class Poller(object):
    '''
    A class that continously pesters arduino to get the current readings
    '''

    def __init__(self, port_name, polling_interval):
        '''
        Constructor
        '''
        self.ser = serial.Serial(port_name)
        self.polling_interval = polling_interval
        self.done = False
        self.loggers = []
        self.monitors = []
        
    def add_logger(self, new_logger):
        self.loggers.append(new_logger)
        
    def add_monitor(self, new_monitor):
        self.monitors.append(new_monitor)
        
    def poll(self):
        while not self.done:
            self.ser.write("0")
            line = self.ser.readline().strip()
            if line.endswith(">"):
                T1, T2 = [float(x) for x in line.split("|")[0:2]]
                values = {
                    "T1" : T1,
                    "T2" : T2
                    }
                
                for logger in self.loggers:
                    logger.log(values)
                    
                for monitor in self.monitors:
                    monitor.check(values)
            
            sleep(self.polling_interval)
        

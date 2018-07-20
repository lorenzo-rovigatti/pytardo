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
        self.port_name = port_name
        self.polling_interval = polling_interval
        self.done = False
        self.loggers = []
        self.monitors = []
        
    def add_logger(self, new_logger):
        self.loggers.append(new_logger)
        
    def add_monitor(self, new_monitor):
        self.monitors.append(new_monitor)
        
    def poll(self):
        ser = serial.Serial(self.port_name, 9600, timeout=1)
        while not self.done:
            data = ser.read(ser.inWaiting()).split("\r\n")
            # get rid of empty lines
            data = filter(lambda x: len(x.strip()) > 0, data)
            # select the last line
            if len(data) > 0:
                line = data[-1]
                values = {}
                for reading in line.split(","):
                    k, v = [x.strip() for x in reading.split("=")]
                    values[k] = float(v)
            
                for logger in self.loggers:
                    logger.log(values)
                     
                for monitor in self.monitors:
                    monitor.check(values)

            ser.write("0\n")            
            sleep(self.polling_interval)
        ser.close()
        

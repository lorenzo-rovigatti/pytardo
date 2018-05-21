'''
Created on 21 mag 2018

@author: lorenzo
'''

import ConfigParser

import callbacks
import loggers
import monitor
import poller


def init_from_config_file(config_file):
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)

    port = config.get("poller", "port")
    polling_interval = config.getfloat("poller", "polling_interval")

    p = poller.Poller(port, polling_interval)

    if config.has_option("loggers", "file_logger"):
        file_logger = loggers.FileLogger(config.get("loggers", "file_logger"), True)
        p.add_logger(file_logger)
    
    conditions = ["T1 > 20"]
    callback_file = callbacks.WriteToFile("warnings.dat", True)
    callback_email = callbacks.SendEmail("lorenzo.rovigatti@gmail.com", ["lorenzo.rovigatti@uniroma1.it", ], 60)
    m = monitor.Monitor(conditions)
    m.add_warning_callback(callback_file)
    m.add_warning_callback(callback_email)
    p.add_monitor(m)
    
    return p

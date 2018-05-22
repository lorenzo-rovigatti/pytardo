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

    logger_sections = config.get("poller", "loggers").split(" ")
    for logger_section in logger_sections:
        logger_type = config.get(logger_section, "type")
        if logger_type == "FileLogger":
            logger = loggers.FileLogger(config.get(logger_section, "filename"), True)
        elif logger_type == "MySQLLogger":
            user = config.get(logger_section, "username")
            pwd = config.get(logger_section, "password")
            database = config.get(logger_section, "database")
            table = config.get(logger_section, "table")
            logger = loggers.MySQLLogger(user, pwd, database, table)
            
        p.add_logger(logger)
    
    conditions = ["T1 > 20"]
    callback_file = callbacks.WriteToFile("warnings.dat", True)
    callback_email = callbacks.SendEmail("lorenzo.rovigatti@gmail.com", ["lorenzo.rovigatti@uniroma1.it", ], 60)
    m = monitor.Monitor(conditions)
    m.add_warning_callback(callback_file)
    m.add_warning_callback(callback_email)
    p.add_monitor(m)
    
    return p

'''
Created on 21 mag 2018

@author: lorenzo
'''

import ConfigParser

import callbacks
import loggers
import monitor
import poller
import sys


def init_from_config_file(config_file):
    try:
        open(config_file)
    except:
        raise BaseException("Unreadable configuration file '%s'" % config_file)
    
    defaults = {
        "stream" : "stdout"
    }
    
    config = ConfigParser.SafeConfigParser(defaults=defaults)
    config.read(config_file)

    port = config.get("poller", "port")
    polling_interval = config.getfloat("poller", "polling_interval")

    p = poller.Poller(port, polling_interval)
    
    # TODO: move this part to a factory-like function in the loggers.py file
    logger_sections = config.get("poller", "loggers").split(" ")
    for logger_section in logger_sections:
        logger_type = config.get(logger_section, "type")
        if logger_type == "ScreenLogger":
            stream_name = config.get(logger_section, "stream")
            
            if stream_name == "stdout":
                stream = sys.stdout
            elif stream_name == "stderr":
                stream = sys.stderr
            else:
                raise BaseException("Invalid stream '%s'" % stream_name)
            logger = loggers.ScreenLogger(stream)
        elif logger_type == "FileLogger":
            append = config.getboolean(logger_section, "append")
            filename = config.get(logger_section, "filename")
            logger = loggers.FileLogger(filename, append)
        elif logger_type == "MySQLLogger":
            user = config.get(logger_section, "username")
            pwd = config.get(logger_section, "password")
            database = config.get(logger_section, "database")
            table = config.get(logger_section, "table")
            logger = loggers.MySQLLogger(user, pwd, database, table)
        else:
            raise BaseException("Invalid logger '%s'" % logger_type)
            
        p.add_logger(logger)
        
    # TODO: move this part to a factory-like function in the monitor.py file
    monitor_sections = config.get("poller", "monitors").split(" ")
    for monitor_section in monitor_sections:
        conditions = config.get(monitor_section, "conditions").split(",")
        m = monitor.Monitor(conditions)
    
        # TODO: move this part either in the above function or in a similar function in callbacks.py
        callback_sections = config.get(monitor_section, "callbacks").split(" ")
        for callback_section in callback_sections:
            callback_type = config.get(callback_section, "type")
            if callback_type == "WriteToFile":
                append = config.getboolean(callback_section, "append")
                filename = config.get(callback_section, "filename")
                callback = callbacks.WriteToFile(filename, append)
            elif callback_type == "SendEmail":
                from_address = config.get(callback_section, "from")
                recipients = config.get(callback_section, "recipients").split(",")
                min_interval = config.getfloat(callback_section, "min_interval")
                callback = callbacks.SendEmail(from_address, recipients, min_interval)
            elif callback_type == "CallScript":
                options = {
                 "script_path" : config.get(callback_section, "path")
                }
                if config.has_option(callback_section, "uid_gid"):
                    uid, gid = config.get(callback_section, "uid_gid").split()
                    options['uid'] = int(uid)
                    options['gid'] = int(gid)
                    
                callback = callbacks.CallScript(**options)
            else:
                raise BaseException("Invalid callback '%s'" % callback_type)
                
            m.add_warning_callback(callback)
            
        p.add_monitor(m)
    
    return p

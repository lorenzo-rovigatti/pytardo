'''
Created on 18 mag 2018

@author: lorenzo
'''

import time
import MySQLdb
from _mysql_exceptions import OperationalError


class FileLogger(object):
    '''
    Writes arduino readings to a file
    '''

    def __init__(self, filename, append):
        '''
        Constructor
        '''
        self.filename = filename
        self.append = append
        
    def log(self, dict_values):
        if self.append:
            mode = "a"
        else:
            mode = "w"

        line = time.strftime('%Y-%m-%d %H:%M:%S')
        for k in sorted(dict_values.keys()):
            line += " - %s %s" % (str(k), str(dict_values[k]))  
        
        with open(self.filename, mode) as logfile:
            print >> logfile, line


class MySQLLogger(object):
    '''
    Writes arduino readings to a mysql db. 
    The table should contain a column for each of the values to be logged, named accordingly.
    '''

    def __init__(self, user, pwd, database, table, host="localhost"):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.database = database

        # test the db connection
        try:
            db = MySQLdb.connect(host, user, pwd, database)
        except OperationalError as e:
            raise BaseException("Caught the following error while connecting to the MySQL database: %s" % (e))

        self.base_query = "INSERT INTO %s (%%s) VALUES (%%s)" % table

    def log(self, dict_values):
        sorted_keys = sorted(dict_values)
        names = ",".join(sorted_keys)
        values = ",".join(map(lambda x: str(dict_values[x]), sorted_keys))
        query = self.base_query % (names, values)

        db = MySQLdb.connect(self.host, self.user, self.pwd, self.database)
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()

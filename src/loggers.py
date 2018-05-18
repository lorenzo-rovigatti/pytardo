'''
Created on 18 mag 2018

@author: lorenzo
'''

import time


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

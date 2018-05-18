'''
Created on 18 mag 2018

@author: lorenzo
'''
import time


class WriteToFile(object):
    '''
    Writes the warnings to a file
    '''

    def __init__(self, filename, append):
        '''
        Constructor
        '''
        self.filename = filename
        self.append = append
        
    def react(self, warnings):
        if self.append:
            mode = "a"
        else:
            mode = "w"
            
        with open(self.filename, mode) as output:
            for w in warnings:
                line = time.strftime('%Y-%m-%d %H:%M:%S')
                condition = w.condition % w.value
                line += " %s = %s" % (w.name, condition)
                print >> output, line

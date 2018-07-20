'''
Created on 21 mag 2018

@author: lorenzo
'''

class Threshold(object):
    '''
    A condition that checks the current value against a given threshold
    '''


    ALLOWED_OPERATORS = ["<", ">", "<=", ">=", "!="]
    def __init__(self, condition_line):
        '''
        Constructor
        '''
        
        spl = [x.strip() for x in condition_line.split()]
        self.key = spl[0] 
        
        if spl[1] not in Threshold.ALLOWED_OPERATORS:
            raise BaseException("The '%s' condition is ill-formatted. The '%s' operator is not supported." % (condition_line, spl[1]))
        
        self.operator = spl[1]
        
        try:
            self.threshold = float(spl[2])
        except IndexError:
            raise BaseException("The '%s' condition lacks a threshold value." % (condition_line))
        except ValueError:
            raise BaseException("The '%s' condition contains the threshold value '%s' that cannot be parsed to float." % (condition_line, spl[2]))
            
    def is_met(self, value):
        return eval("%s %s %f" % (value, self.operator, self.threshold))
    
    def __str__(self):
        return "%%f %s %f" % (self.operator, self.threshold)

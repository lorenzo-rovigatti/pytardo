'''
Created on 18 mag 2018

@author: lorenzo
'''

class MonitorWarning(object):
    def __init__(self, name, condition, value):
        self.name = name
        self.condition = condition
        self.value = value
        

class Monitor(object):
    '''
    Checks the arduino readings against user-defined conditions. If the conditions are verified, call
    '''

    def __init__(self, conditions):
        '''
        Constructor
        '''
        self.conditions = {}
        for condition in conditions:
            spl = [s.strip() for s in condition.split()]
            if len(spl) != 3:
                raise BaseException(
                    "The '%s' condition is ill-formatted. A valid condition should "
                    "contain the name of the value to be checked, a mathematical "
                    "operator and a threshold value ('T1 > 25')" % condition)
            my_condition = "%%s %s %s" % (spl[1], spl[2])
            self.conditions[spl[0]] = my_condition
            
        self.warning_callbacks = []
        
    def add_warning_callback(self, callback):
        self.warning_callbacks.append(callback)
            
    def check(self, values):
        warnings = []
        
        for k in values.keys():
            if k in self.conditions:
                if eval(self.conditions[k] % str(values[k])):
                    warnings.append(MonitorWarning(k, self.conditions[k], values[k]))
        
        if len(warnings) > 0:
            for callback in self.warning_callbacks:
                callback.react(warnings)
        
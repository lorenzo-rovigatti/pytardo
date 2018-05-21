'''
Created on 18 mag 2018

@author: lorenzo
'''

import conditions

class MonitorWarning(object):
    def __init__(self, name, condition, value):
        self.name = name
        self.condition = condition
        self.value = value
        

class Monitor(object):
    '''
    Checks the arduino readings against user-defined conditions. If the conditions are verified, call
    '''

    def __init__(self, condition_lines):
        '''
        Constructor
        '''
        self.conditions = {}
        for condition_line in condition_lines:
            new_condition = conditions.Threshold(condition_line)
            self.conditions[new_condition.key] = new_condition
            
        self.warning_callbacks = []
        
    def add_warning_callback(self, callback):
        self.warning_callbacks.append(callback)
            
    def check(self, values):
        warnings = []
        
        for k in values.keys():
            if k in self.conditions:
                if self.conditions[k].is_met(values[k]):
                    warnings.append(MonitorWarning(k, self.conditions[k], values[k]))
        
        for callback in self.warning_callbacks:
            callback.react(values, warnings)
        
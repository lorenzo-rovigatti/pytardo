#!/usr/bin/env python
'''
Created on 17 mag 2018

@author: lorenzo
'''

import sys
import initialiser

if __name__ == '__main__':
    p = initialiser.init_from_config_file(sys.argv[1])
    p.poll()

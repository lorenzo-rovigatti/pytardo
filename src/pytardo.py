#!/usr/bin/env python
'''
Created on 17 mag 2018

@author: lorenzo
'''

import sys
import initialiser

def pytardo():
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage is %s config_file" % sys.argv[0]
        exit(1)
    
    try:
        p = initialiser.init_from_config_file(sys.argv[1])
    except (initialiser.ConfigParser.NoOptionError, initialiser.ConfigParser.NoSectionError, ValueError), e:
        print >> sys.stderr, "Caught an error while parsing the configuration file:", e
        exit(1)
    except:
        print >> sys.stderr, "Unexpected error:", sys.exc_info()
        exit(1)
        
    return p

if __name__ == '__main__':
    pytardo().poll()

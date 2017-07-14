#!/usr/local/bin/python3

# This file was created on 12/05/2016
# Author: George Kaimakis
# This code from 'Generator' tutorial by Corey Schafer (https://www.coreyms.com)


#from pympler import summary, muppy
#import psutil
import resource
import os
import sys

#def memory_usage_psutil():
#    # return the memory usage in MB
#    process = psutil.Process(os.getpid())
#    mem = process.get_memory_info()[0]/float(2**20)
#    return mem

def memory_usage_resource():
    rusage_denom = 1024
    if sys.platform == 'darwin':
        # ...it seems that in OSX the output is different units...
        rusage_denom = rusage_denom * rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem


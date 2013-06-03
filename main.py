#!/usr/bin/env python

import ConfigParser
import datetime
import time
import os
import sys
import gzip
from StringIO import StringIO

def show_man_q1():
    print "TO-DO. q1 manual page"
    print "Station array parameter compression: echo '[9,10,11,12,13,14,15,16,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]' | gzip -cf| base64"

def current_datetime(time_stamp):
        return datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    # Changing execution to main.py path to avid problems when reading cfg files
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    ts = time.time()

    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    print (current_datetime(ts)+" - Collecting data")
    try:
         print "Performing"
	 if (str(sys.argv[1])=='q1'):
	     if (len(sys.argv)!=5):
		 print "ERROR: Wrong number of arguments for q1"
		 show_man_q1()
	     else:
	         print "q1"
	         try:
                     gzipstring = sys.argv[2].decode('base64','strict')
                     station_list = gzip.GzipFile(fileobj=StringIO(gzipstring)).read()
		     print station_list.strip()
                 except Exception, e:
                     print "ERROR: An error occurred while trying to decode station array parameter"
    except Exception, e:
         print "ERROR"

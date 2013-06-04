#!/usr/bin/env python

import ConfigParser
import datetime
import time
import os
import sys
import gzip
from StringIO import StringIO
from pymongo import Connection
import json

def show_man_q1():
    print "TO-DO. q1 manual page"
    print "Station array parameter compression: echo '1,23,27,113,214,335' | gzip -cf| base64"

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
	     if (len(sys.argv)!=6):
		 print "ERROR: Wrong number of arguments for q1"
		 show_man_q1()
	     else:
	         print "q1"
	         try:
		     # Decode station array parameter
                     gzipstring = sys.argv[2].decode('base64','strict')
		     # Decompress decoded station array parameter
                     station_list = gzip.GzipFile(fileobj=StringIO(gzipstring)).read().strip()
		     # Create list from station array parameter
		     station_list = station_list.split(',')
		     # Converting string array to int array
		     station_list = map(int,station_list)
		     # Deduplicate possible repeated values within the station array
		     station_list = sorted(set(station_list))
                 except Exception, e:
                     print "ERROR: An error occurred while trying to decode station array parameter"
		     print e
		 try:
		     t1 = datetime.datetime.strptime(sys.argv[3],'%Y%m%d%H%M')
                 except Exception, e:
                     print "ERROR: An error occurred while converting t1 parameter to timestamp"
		     print e
		 try:
		     t2 = datetime.datetime.strptime(sys.argv[4],'%Y%m%d%H%M')
                 except Exception, e:
                     print "ERROR: An error occurred while converting t2 parameter to timestamp"
		     print e
		 if (t2<t1):
		     tmp_t1 = t1
		     t1 = t2
		     t2 = tmp_t1
		 try:
   	             config = ConfigParser.ConfigParser()
                     config.read('./mongodb.cfg')     
                     mongodbip = str(config.get('mongodb', 'ip'))
                     mongodbport = int(config.get('mongodb', 'port'))
                     mongodbuser = str(config.get('mongodb', 'user'))
                     mongodbpass = str(config.get('mongodb', 'pass'))
		     
		     connection = Connection(mongodbip,mongodbport)
		     try:
			 db = connection[sys.argv[5]]
		         collection = db['data']
                     except Exception, e:
                         print "ERROR: An error occurred connecting to MongoDB server"
			 print e
		     for station in station_list:
			 station_row = []
			 station_row.append("id="+str(station))
   		         cursor = collection.find( { "$and": [{"s" : station},{ "t": {"$gte": t1 ,"$lte": t2} }] })
                         for row in cursor:
                                station_row.append(json.dumps(row['f']))
                         print station_row 
		     
                 except Exception, e:
                     print "ERROR: An error occurred opening mongodb.cfg config file"
		     print e
		 
    except Exception, e:
         print "ERROR"

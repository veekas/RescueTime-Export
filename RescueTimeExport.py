#!/usr/bin/env python
#-*- coding: utf-8 -*-

# RescueTime Data Exporter
# Dan Nixon
# 18/09/2011
# forked from Chris Burgess (xurizaemon)

import urllib
import datetime

apiKey = "API_KEY"
fileDirectory = ""
filePrefix = "RescueTime Data"

def main():
    print "RescueTime Data Exporter"
    print "Dates in format YYYY-MM-DD"
    date_s = raw_input("Start Date: ") #TODO auto-populate the date of last modified
    date_e = raw_input("End Date: ") #TODO change to 'yesterday's' date: yesterday = datetime.now() - timedelta(days=1); yesterday.strftime('%Y%m%d')
    print "Getting Data for Interval", date_s, "to", date_e
    params = urllib.urlencode({'key':apiKey, 'perspective':'interval', 'format':'csv', 'restrict_begin':date_s, 'restrict_end':date_e})
    u = urllib.urlopen("https://www.rescuetime.com/anapi/data", params)
    CSVdata = u.read()
    filePath = fileDirectory + filePrefix + ".csv" #simplified and generalized the filepath
    f = open(filePath, "a") #changed to append the existing csv file instead of creating a new one
    #TODO delete the duplicate header row that is created with each update
    f.write(CSVdata)
    f.close()
    print "Data Saved to", filePath
    print ""
    #TODO make this process repeat daily/weekly/etc

main()

# I wrote these instructions for Mac. If you're running Windows, I think the only difference is that you'll open Command Prompt instead of Terminal
# install Python if you don't have it already: https://www.python.org/downloads/
#save this file as "RTExport.py" somewhere that is easy to find

#!/usr/bin/env python
#-*- coding: utf-8 -*-

# RescueTime Data Exporter
# Dan Nixon
# 18/09/2011

import urllib

apiKey = "API_KEY"
# change to your own API key. Create a new one here: https://www.rescuetime.com/anapi/manage
fileDirectory = ""
# change to the file directory in which you'd like the file saved
filePrefix = "RescueTimeData"
# optional: personalize filePrefix

def main():
    print "RescueTime Data Exporter"
    print "Dates in format YYYY-MM-DD"
    date_s = raw_input("Start Date: ")
    date_e = raw_input("End Date: ")
    print "Getting Data for Interval", date_s, "to", date_e
    params = urllib.urlencode({'key':apiKey, 'perspective':'interval', 'format':'csv', 'restrict_begin':date_s, 'restrict_end':date_e})
    u = urllib.urlopen("https://www.rescuetime.com/anapi/data", params)
    CSVdata = u.read()
    filePath = fileDirectory + filePrefix + date_s.replace("-", "") + "-" + date_e.replace("-", "") + ".csv"
    f = open(filePath, "w")
    f.write(CSVdata)
    f.close()
    print "Data Saved to", filePath
    print ""

main()

# open Terminal
# navigate to the folder where you saved this file using "cd [/folder/subFolder/subFolderWithFile/]"
# type "python ./RTExport.py" and follow the instructions to run the code
# note that it doesn't work if the time interval is over 6 months.

#test

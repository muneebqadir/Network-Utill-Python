from ping import *
import csv
from datetime import date
from time import gmtime, strftime
import time
#TO DO 
"""
0. Both files run can run in main creating the 16 second update faster and smoother updates


1. Delete previous data in the csv file
If data is current time - Time > 30 Delete
Then data from before 30 minutes will be deleted

2. Check for more types of graphs 
Network usage Graph 

Future work 
Alerts when ping not connected

"""

"""
check = pingTest("www.google.com")
#check = pinglat("www.google.com")
print(check)

"""

#The Longer this List is the more time it will take to run the script :(
# IT TAKES ABOUT 16 SECONDS TO RUN THE SCRIPT ONCE FOR 4 WEBSITES with 5 sec sleep right now
websites= ["www.google.co.uk","www.bbc.co.uk"]

#WebUP = WebCheck(websites)
trig = True
#SetScales(0)
#SetScales(20)
while trig:
  FileWrite(websites)
    #time.sleep(5)
print("Finish")
#"""




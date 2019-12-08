import subprocess
import platform
import csv
from datetime import date
from time import gmtime, strftime
import time
import uuid
from NtAnalyzer import *


#Checks if website is Down returns an error if it is 
#This will return false when no wifi is connected as well
"""
TEST FUNCTION

def WebCheck(websites):
  i =0
  WebTrig = True
  for sites in websites:
    WebStatus = pingTest(websites[i])
    if (WebStatus==False):
      print("Error",websites[i], " is down")
      WebTrig = False
      break
  return WebTrig
"""

# File Write Runs Ping Latency and then Writes it into a CSV FILE
def FileWrite(websites):
    Uid = uuid.uuid4()
    retLPing = LowestPing(websites)
    Mping = retLPing[0]
    WebName = retLPing[1]
    nLine = "\n"
    row = "{},{},{},{},{}"
    NowDate = strftime("%d-%m-%Y", gmtime())
    NowTime = strftime("%H:%M:%S", gmtime())
    rowf = row.format(Uid,NowDate,NowTime,Mping,WebName)
    with open('pings.csv','a') as fd:
     fd.write(nLine)
     fd.write(rowf)
    print("Written")
    DelTime("pings.csv",240)
    
def SetScales(yax):
    Uid = uuid.uuid4()
    nLine = "\n"
    row = "{},{},{},{},{}"
    NowDate = strftime("%d-%m-%Y", gmtime())
    NowTime = (datetime.datetime.now()).time()
    NowTime = time_minus(NowTime,timedelta(seconds=235))
    rowf = row.format(Uid,NowDate,NowTime,yax,"Y AXIS SET")
    with open('pings.csv','a') as fd:
     fd.write(nLine)
     fd.write(rowf)

#Method for checking lowest Ping out of the list
def LowestPing(websites):
 i = 0
 min = 1000000000
 WebName = ""
 for sites in websites:
   Lping = PingLatency(websites[i])
   Lping = int(Lping)
   if(min>Lping):
       min = Lping
       WebName = websites[i]
   i+=1
 retWM = [min,WebName]
 return retWM
    

#Method for extracting the Average ms
def PingLatency(website):
    pingstuf = pinglat(website)
    pingstuf = str(pingstuf)
    #String split everything after Average
    avgping = pingstuf.split("avg/max/mdev = ",1)[1]
    #String split everything before ms
    avgping = avgping.split("/",1)[1]
    #print(avgping)
    avgping = float(avgping.split("/",1)[0])
    avgping = int(avgping)
    return avgping

#Mehtod for running the ping command using subprocess
def pinglat(host):

    try:
        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-c'

        # Building the command. Ex: "ping -c 1 google.com"
        command = ['ping', param, '3', host]
        outpt = subprocess.check_output(command)
    except subprocess.CalledProcessError as e:
        print(host,"is unreachable")
        outpt = " min/avg/max/mdev = 100000000000000000000/100000000000000000000/100000000000000000000/0.595 ms"

    return outpt
"""
TEST FUNCTION
#Method to set PingStatus
def pingTest(hostname):
    p = pinglat(hostname)
    #p = subprocess.Popen('ping ' + hostname, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    pingStatus = True;

    #for line in p.stdout:
    for line in p:
        output = p
 
        if (output.endswith('unreachable.')) :
            #No route from the local system. Packets sent were never put on the wire.
            pingStatus = False
            break
        elif (output.startswith('Ping request could not find host')) :
            pingStatus = False
            break
        elif (output.startswith('Request timed out.')) :
            #No Echo Reply messages were received within the default time of 1 second.
            pingStatus = False
            break

    return pingStatus
 """   


# WriteToFile Method
def writeToFile(filename, data) :
    with open(filename, 'a') as output:
        output.write(data + '\n')
    #endWith
#endDef    


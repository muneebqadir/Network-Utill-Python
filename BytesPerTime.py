import matplotlib.pyplot as plt
import argparse
from os import getuid
from scapy.all import *
from datetime import datetime
import pandas as pd
from datetime import timedelta
import numpy as np


parser = argparse.ArgumentParser(description='Live Traffic Examiner')
parser.add_argument('interface', help="Network interface", type=str)
parser.add_argument('--count', help="Capture X packets and exit", type=int)
args=parser.parse_args()

if getuid() != 0 :
   print("Warning: Not running as root, packet listening may not work.")
   try:
       print("--Trying to listen on {}".format(args.interface))
       sniff(iface=args.interface,count=1)
       print("--Success!")
   except:
       print("--Failed!\nError: Unable to sniff packets, try using sudo.")
       quit()






i=0
pktBytes=[]
bytes = pd.Series(pktBytes).astype(int)
pktTimes=[]
times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
df = pd.DataFrame({"Bytes": bytes, "Times":times})
df2 = pd.DataFrame({"Bytes": bytes, "Times":times})
df = df.set_index('Times')

#plt.ion()

plt.tight_layout()
#plt.show()

def DFrame(packet):
    pktBytesTemp=[]
    pktTimesTemp=[]
    pktBytesTemp.append(1)
    bytes = pd.Series(pktBytesTemp).astype(int)
    pktTime=datetime.fromtimestamp(pkt.time)
    pktTimesTemp.append(pktTime.strftime("%H:%M:%S"))
    times = pd.to_datetime(pd.Series(pktTimesTemp).astype(str),  errors='coerce')
    temp_df = pd.DataFrame({"Bytes": bytes, "Times":times})
    temp_df = temp_df.set_index('Times')
    global df
    global df2
    df = df.append(temp_df, ignore_index=False)
    #df = df.set_index('Times')
    df = df.resample('1S').sum()
    df2 = df2.append(df, ignore_index=False)
    #df = df[0:0]
    """
    pktBytesTemp=[]
    pktTimesTemp=[]
    pktBytesTemp.append(a)
    bytes = pd.Series(pktBytesTemp).astype(int)
    pktTime=datetime.now()
    pktTimesTemp.append(pktTime.strftime("%H:%M:%S"))
    times = pd.to_datetime(pd.Series(pktTimesTemp).astype(str),  errors='coerce')
    temp_df = pd.DataFrame({"Bytes": bytes, "Times":times})
    temp_df=temp_df.set_index('Times')
    df = df.append(temp_df, ignore_index=False)
    df = df.resample('1S').sum()
    """
    DelTime(90)
    yData = df2['Bytes']
    xData = np.arange(len(df2.index))
    
    
    plt.pause(1)
    #print("Ydata: ", yData,'\n',"xData:   ", xData)
    plt.cla()
    plt.ylabel("Bytes")
    plt.xlabel("Time")
    plt.title("Real Time Network Traffic")
    #ax = plt.subplot(111)
    #ax.bar(xData, yData, width=10)
    #ax.xaxis_time()

    plt.bar(xData, yData, width=0.9, bottom=None,align='edge', data=None)
    #plt.plot(xData, yData)
    #plt.bar(xData,yData)
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    
    



def DelTime(tim):
    global df2
    tim = timedelta(seconds=tim)
    for Times, row in df2.iterrows():
        NowTime = (datetime.now()).time()
        Packet_Time = str(Times)
        NowTime = time_minus(NowTime,tim)
        Packet_Time = datetime.strptime(Packet_Time, "%Y-%m-%d %H:%M:%S" ).time()
        #print(Packet_Time<(time_minus(NowTime,tim)))
        #print("Packet_Time= ",Packet_Time,"<","  NowTime= ", NowTime)
        epochN = int(time.mktime(time.strptime(str(NowTime), "%H:%M:%S")))
        epochP = int(time.mktime(time.strptime(str(Packet_Time), "%H:%M:%S")))
        #print((epochP<epochN))
        if(epochP<epochN):
            #df2 = df2[df2. != times]
            #df2.drop(df2.loc[df2['Times']==Times].index, inplace=True)
            try:
                df2.drop(Times, inplace=True)
            except:
                pass
	#print(data)


def time_minus(time, timedelta):
    start = datetime(
        2000, 1, 1,
        hour=time.hour, minute=time.minute, second=time.second)
    end = start - timedelta
    return end.time()

    

while True:
    for pkt in sniff(iface=args.interface,count=1):
        try:
            if IP in pkt:
                DFrame(IP)
                
                i+=1
                if args.count:
                    if i >= args.count:
                        print("No Arguments")
                        quit()
        #Keyboard interrupt to stop script
        except KeyboardInterrupt:
            print("Captured {} packets on interface {} ".format(i, args.interface))
            breakpoint()
            quit()    





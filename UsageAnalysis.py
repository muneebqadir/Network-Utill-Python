import os
import time
import matplotlib.pyplot as plt
from scapy.all import *
from datetime import datetime
import pandas as pd
import numpy as np
from datetime import timedelta


pktByte=[]
pktTime=[]
bytes = pd.Series(pktByte).astype(int)
times = pd.to_datetime(pd.Series(pktTime).astype(str),  errors='coerce')
df2 = pd.DataFrame({"Bytes": bytes, "Times":times})
df2 = df2.set_index('Times')

def plist():
    global df2
    pktBytes=[]
    pktTimes=[]
    packets = rdpcap('capt.pcap')
    #Read each packet and append to the lists.
    for pkt in packets:
        if IP in pkt:
            if(pkt[IP].src==80 or pkt[IP].dst==80):
                try:
                        pktBytes.append(pkt[IP].len)
                        pktTime=datetime.fromtimestamp(pkt.time)
                        pktTimes.append(pktTime.strftime("%Y-%m-%d %H:%M:%S.%f"))

                except:
                        pass


    bytes = pd.Series(pktBytes).astype(int)
    times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
    df  = pd.DataFrame({"Bytes": bytes, "Times":times})
    df = df.set_index('Times')
    df=df.resample('1S').sum()
    df2 = df2.append(df, ignore_index=False)
    df2 = df2.drop_duplicates()
    
    #print(df2)
    DelTime(60)
    #print("\n \n AFTER",df2)
    yData = df2['Bytes']
    xData = np.arange(len(df2.index))
    #xData = df2.index
    #print(xData)
    
    #print("Ydata: ", yData,'\n',"xData:   ", xData)
    plt.cla()
    plt.ylabel("Bytes")
    plt.xlabel("Time")
    plt.title("Real Time Network Traffic")
    plt.bar(xData, yData, width=0.9, bottom=None,align='edge', data=None)
    plt.pause(1)
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    #ax = plt.subplot(111)
    #ax.bar(xData, yData, width=10)
    #ax.xaxis_time()

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
    try:
        plist()
    except:
        pass
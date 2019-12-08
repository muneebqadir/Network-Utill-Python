from collections import Counter
from scapy.all import sniff
from scapy.all import TCP
import csv
from datetime import date
from time import gmtime, strftime
import time
import uuid
from NtAnalyzer import *


## Create a Packet Counter
counta = 0

## Define our Custom Action function
def custom_action(packet):
    Uid = uuid.uuid4()
    src_packet = packet[0][1].src
    dst_packet = packet[0][1].dst
    if(TCP in packet):
        tsport = packet.sport
        tdport = packet.dport
        sumary = packet.summary()
    else:
        tsport = "NaN"
        tdport = "NaN"
        sumary = "Ether /IP /UDP ??.??"
    
    nLine = "\n"
    row = "{},{},{},{},{},{},{},{}"
    NowDate = strftime("%d-%m-%Y", gmtime())
    NowTime = strftime("%H:%M:%S", gmtime())
    rowf = row.format(Uid,NowDate,NowTime,src_packet,tsport,dst_packet,tdport,sumary)
    with open('packets.csv','a') as fd:
     fd.write(nLine)
     fd.write(rowf)
     DelTime("packets.csv",120)
     #countb=counta+1
     #print("Written")
     

## Setup sniff, filtering for IP traffic
###     ADD FILETER sniff(filter -'dst port 5555')
sniff(filter="ip", prn=custom_action, count=200000)

## Print out packet count per A <--> Z address pair
#print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: {count}" for key, count in packet_counts.items()))

import matplotlib.pyplot as plt
import argparse
from os import getuid
from scapy.all import *
from datetime import datetime
import pandas as pd


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

plt.ion()
plt.ylabel("Bytes")
plt.xlabel("Time")
plt.title("Real Time Network Traffic")
plt.tight_layout()
plt.show()


i=0
pktBytes=[]
bytes = pd.Series(pktBytes).astype(int)
pktTimes=[]
times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
df = pd.DataFrame({"Bytes": bytes, "Times":times})
df = df.set_index('Times')


def DFrame(packet):
    pktBytes.append(pkt.len)
    bytes = pd.Series(pktBytes).astype(int)
    pktTime=datetime.fromtimestamp(pkt.time)
    pktTimes.append(pktTime.strftime("%Y-%m-%d %H:%M:%S.%f"))
    times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
    temp_df = pd.DataFrame({"Bytes": bytes, "Times":times})
    global df
    df = df.append(temp_df, ignore_index=True)
    df = df.set_index('Times')
    df = df.resample('2S').sum()
    
    


while True:
    for pkt in sniff(filter="ip",iface=args.interface,count=1):
        try:
            if IP in pkt:
                DFrame(IP)
                print(df)
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
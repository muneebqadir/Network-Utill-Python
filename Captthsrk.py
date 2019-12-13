from scapy.all import *
import os
import time


# os.system("tshark  -T fields -e _ws.col.Info -e http -e frame.time -e  "
# "data.data -w Eavesdrop_Data.pcap -c 1000")
#x = "sudo tshark  -T fields -e _ws.col.Info -e frame.time -e data.data -w capt.pcap -c 1000"
x = "dumpcap -a duration:1 -w capt.pcap"
#x = "sudo tcpdump -c1000 -w capt.pcap -i enp0s3"
#x = "sudo tshark  -T fields -e _ws.col.Info -e frame.time -e data.data -w del.pcap -b duration:50000"
def capture(x):
    while True:
        try:
            subprocess.call(x, shell=True)
        except:
            pass

capture(x)

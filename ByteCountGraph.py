from scapy.all import *
import matplotlib.pyplot as plt
import argparse
from os import getuid

#ARGUMENTS
parser = argparse.ArgumentParser(description='Live Traffic Examiner')
parser.add_argument('interface', help="Network interface", type=str)
parser.add_argument('--count', help="Capture X packets and exit", type=int)
args=parser.parse_args()

#USER CHECK ROOT
#Check to see if we are root, otherwise Scapy might not be able to listen
if getuid() != 0 :
   print("Warning: Not running as root, packet listening may not work.")
   try:
       print("--Trying to listen on {}".format(args.interface))
       sniff(iface=args.interface,count=1)
       print("--Success!")
   except:
       print("--Failed!\nError: Unable to sniff packets, try using sudo.")
       quit()
"""
if args.count:
   print("Capturing {} packets on interface {} ".format(args.count, args.interface)
else:
   print("Capturing unlimited packets on interface {} \n--Press CTRL-C to exit".format(args.interface))
  """
#PLOT USING ION
#Interactive Mode
plt.ion()
#Labels
plt.ylabel("Bytes")
plt.xlabel("Count")
plt.title("Real Time Network Traffic")
plt.tight_layout()



#SETTING UP LOOP TO COUNT 1 PACKET AT A TIME AND THEN COUNT
#Empty list to hold bytes
yData=[]
i=0
#Listen indefinitely, or until we reach count
while True:
   #Listen for 1 packet
   #Count =1 packet will tell scapy to only snif 1 packet
   for pkt in sniff(iface=args.interface,count=1):
       #try/except is to allow the user to hit CTRL-C to exit
        try:
            #adding the size of the packet to yData to the plot, and draw it with plt.pause every 0.1 second
           if IP in pkt:
               yData.append(pkt[IP].len)
               plt.plot(yData)
               #Pause and draw
               plt.pause(0.1)
               i+=1
               if args.count:
                   if i >= args.count:
                       quit()
        #Keyboard interrupt to stop script
        except KeyboardInterrupt:
            print("Captured {} packets on interface {} ".format(i, args.interface))
            quit()

 
 
                       
 
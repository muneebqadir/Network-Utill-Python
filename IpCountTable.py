from scapy.all import *
from collections import Counter
from prettytable import PrettyTable

#Reading pcap into a list
packets = rdpcap('example.pcap')
#print(pkt[IP].src)
#Storing IPs in a list (For dhcp etc pass)
srcIP=[]
for pkt in packets:
    if IP in pkt:
        try:
            srcIP.append(pkt[IP].src)
        except:
            pass

#Intializing counter
cnt=Counter()

for ip in srcIP:
    cnt[ip] += 1

#Creating Table
table= PrettyTable(["IP", "Count"])
#High to Low
for ip, count in cnt.most_common():
   table.add_row([ip, count])

print(table)

#TEST sudo tcpdump -w example.pcap -c10000
#PCAP FILE REQUIRED FOR THE TABLE


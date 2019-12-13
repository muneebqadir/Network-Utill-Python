from scapy.all import *
import plotly
from datetime import datetime
import pandas as pd

#Read the packets from file
packets = rdpcap('capt.pcap')

#Lists to hold packet info
pktBytes=[]
pktTimes=[]

#Read each packet and append to the lists.
for pkt in packets:
   if IP in pkt:
        try:
                pktBytes.append(pkt[IP].len)
                pktTime=datetime.fromtimestamp(pkt.time)
                pktTimes.append(pktTime.strftime("%Y-%m-%d %H:%M:%S.%f"))

        except:
                pass

#This converts list to series
bytes = pd.Series(pktBytes).astype(int)
#Convert the timestamp list to a pd date_time
times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
#Create the dataframe
df  = pd.DataFrame({"Bytes": bytes, "Times":times})
#set the date from a range to an timestamp
df = df.set_index('Times')
#Create a new dataframe of 2 second sums to pass to plotly
df2=df.resample('2S').sum()
print(df2['Bytes'])
#Create the graph
plotly.offline.plot({"data":[plotly.graph_objs.Scatter(x=df2.index, y=df2['Bytes'])],"layout":plotly.graph_objs.Layout(title="Bytes over Time ",xaxis=dict(title="Time"),yaxis=dict(title="Bytes"))})
import matplotlib.pyplot as plt
import argparse
from os import getuid
from scapy.all import *
from datetime import datetime
import pandas as pd
from datetime import timedelta
import numpy as np

a=1
pktBytes=[]
bytes = pd.Series(pktBytes).astype(int)
pktTimes=[]
times = pd.to_datetime(pd.Series(pktTimes).astype(str),  errors='coerce')
df = pd.DataFrame({"Bytes": bytes, "Times":times})
for i in range(10000):
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
    #df = df.set_index('Times')

print(df)
from time import gmtime, strftime
import time
import pandas as pd
import uuid
import datetime
from datetime import timedelta

def DelTime(path, tim):
	data = pd.read_csv(path, index_col ="Uid",header =0)
	tim = timedelta(seconds=tim)
	for Uid, row in data.iterrows():
		NowTime = (datetime.datetime.now()).time()
		Packet_Time = (row['Time'])
		Packet_Time = datetime.datetime.strptime(Packet_Time, '%H:%M:%S' ).time()
		#print(Packet_Time<(time_plus(NowTime,tim)))
		print("Packet_Time= ",Packet_Time,"<","  NowTime= ", NowTime)
		if(Packet_Time<(time_minus(NowTime,tim))):
			data = data.drop(Uid, axis =0)
	data.to_csv(path)
	#print(data)

def time_minus(time, timedelta):
    start = datetime.datetime(
        2000, 1, 1,
        hour=time.hour, minute=time.minute, second=time.second)
    end = start - timedelta
    return end.time()
#Noi= (datetime.datetime.now()).time()
#delta = timedelta(hours=9)
#print(time_plus(Noi,delta))

#DelTime("packets.csv",5)

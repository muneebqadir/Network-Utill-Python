import random
from itertools import *
import pandas as pd 
#import kiwisolver
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from NtAnalyzer import *
from collections import Counter



def get_col(arr, col):
    return map(lambda x : x[col], arr)
def col(matrix, i):
    return [row[i] for row in matrix]
"""
data = pd.read_csv("packets.csv", index_col ="Uid",header =0)
cTime = Counter(data['Time']).most_common()
print(cTime)
x = get_col(cTime,0)
print("X values are: ", x)
y1 = get_col(cTime,1)
print("Y values are: ", y1)
  
plt.cla()
plt.bar(x, y1, align='center', alpha=0.5)
plt.tight_layout()
plt.show()
""" 
def animate(i):

    data = pd.read_csv("packets.csv", index_col ="Uid",header =0)
    cTime = Counter(data['Time']).most_common()
    print(cTime)
    x = col(cTime,0)
    print("X values are: ", x)
    y1 = col(cTime,1)
    print("Y values are: ", y1)
    
    plt.cla()
    plt.bar(x, y1, align='center', alpha=0.5)
    plt.tight_layout()
    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(False)
    

    #plt.yticks(np.arange(0, 20, step=2))
    #plt.ylim(0, 20)
    #plt.plot(x,y1)
    #plt.legend(loc='upper left')

#plt.autoscale(False)
ani = FuncAnimation(plt.gcf(), animate, interval=1300)

#frame1.autoscale(False)
plt.ylabel('Usage')
plt.title('Pusage')
plt.tight_layout()

plt.show()


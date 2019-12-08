import random
from itertools import count
import pandas as pd 
#import kiwisolver
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np




"""
data = pd.read_csv('pings.csv')
y1 = data['PingLatency']
x = data['Time']

print(x)
print(y1)

"""
#plt.style.use('fivethirtyeight')



def animate(i):
    data = pd.read_csv('pings.csv')
    x = data['Time']
    y1 = data['PingLatency']
    
    plt.cla()
    plt.yticks(np.arange(0, 20, step=2))
    plt.ylim(0, 20)
    plt.plot(x,y1)
    plt.legend(loc='upper left')
    plt.tight_layout()

plt.autoscale(False)
ani = FuncAnimation(plt.gcf(), animate, interval=4000)
frame1 = plt.gca()
frame1.autoscale(False)

plt.tight_layout()
frame1.axes.get_xaxis().set_visible(False)
plt.show()

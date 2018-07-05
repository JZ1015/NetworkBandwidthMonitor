import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig=plt.figure()

def animate(i):
    data=open('monitor.txt','r').read() #file reader
    dataArray=data.split('\n') #data manipulation, split
    DateTime=[]  #data structure list
    sent=[]
    rev=[]
    for record in dataArray:  #for loop
        if len(record)>2:     #if condition
            d,s,r=record.split(',')
            DateTime.append(pd.to_datetime(d))  #queue
            sent.append(int(s))
            rev.append(int(r))
            if len(DateTime)>20:
                DateTime.pop(0)
                sent.pop(0)
                rev.pop(0)
    fig.clear()
    plt.title("Network Bandwidth Monitor")
    plt.xlabel('DateTime')
    plt.ylabel('KB Sent/Reveived')
    plt.plot(DateTime,sent,label='KB Sent')
    plt.plot(DateTime,rev,label='KB Received')
    plt.legend()
    plt.xticks(rotation=80)

animation=ani.FuncAnimation(fig,animate,interval=2000)
plt.show()

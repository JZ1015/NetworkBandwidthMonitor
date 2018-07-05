import pandas as pd
import numpy as np
import psutil
import time
import datetime
import sys
import os
import matplotlib.pyplot as plt

def report():        #user defigned function
    data=open('monitor.txt','r').read()
    dataArray=data.split('\n')
    monitor=[]
    for record in dataArray:
        if len(record)>2:
            t,s,r=record.split(',')
            monitor.append((pd.to_datetime(t),int(s),int(r)))
    df=pd.DataFrame(monitor,columns=["DateTime","KB_sent","KB_received"])     #DataFrame
    top_10_sent=df.sort_values(by="KB_sent",ascending=False).head(10)
    top_10_rev=df.sort_values(by="KB_received",ascending=False).head(10)
    print 'Top 10 sent :\n',top_10_sent
    print '\n'
    print 'Top 10 received:\n', top_10_rev
    plt.figure()
    plt.xlabel('DateTime')
    plt.ylabel('KB Sent/Reveived')
    plt.plot(df.DateTime,df.KB_sent,label='KB Sent')
    plt.plot(df.DateTime,df.KB_received,label='KB Received')
    plt.legend()
    plt.title("Network Bandwidth Monitor")
    plt.xticks(rotation=80)
    plt.show()


sent_0=psutil.net_io_counters().bytes_sent
rev_0=psutil.net_io_counters().bytes_recv
print ('Enter Control+C to exit!')
try:                                               #error handling, exception
    while True:                                    #While loop
    #for i in xrange(20):
        sent_1= psutil.net_io_counters().bytes_sent
        rev_1=psutil.net_io_counters().bytes_recv
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sentKB=(sent_1-sent_0)/1024
        revKB=(rev_1-rev_0)/1024
        bandwidth=dt+','+str(sentKB)+','+str(revKB)  #string manipulation
        with open('monitor.txt','a')as monitor_file:
            monitor_file.write(bandwidth+'\n')       #file write
        sent_0=sent_1
        rev_0=rev_1
        time.sleep(2)
except (KeyboardInterrupt,SystemExit):
    report()
    os.remove('monitor.txt')
    sys.exit(0)

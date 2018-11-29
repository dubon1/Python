#!/usr/bin/python3 
from matplotlib import pylab
from pylab import * 
import csv
from time import gmtime, mktime

filepath='qqq2.csv'
data=[]
for row in csv.reader(open(filepath), delimiter=','):
  data.append(row)

# split the data to header and values
header=data[0]
values=array(data[2:])

yearday=zeros(len(values[:, 0]))
for i, day in enumerate(values[:, 0]):
 market_close_time=(int(day[6:]), int(day[:2]), int(day[3:5]), 16,0,0,0,0,0)
 yearday[i]=gmtime(mktime(market_close_time)).tm_yday

# plot the data
for i in range(1, 5):
 plot(yearday, values[:, i], label=header[i], linewidth=3)

# annotate the start and end dates
text(yearday[0], values[0, 1], values[0, 0], ha='center')
text(yearday[-1], values[-1, 1], values[-1, 0], ha='center')

grid()
legend(loc='best')
ylabel('stock price [USD]')
xlabel('Days from start of the year '+values[0, 0][6:])
title('NASDAQ-100 (INCEX) stock price, period %s-%s ' % (values[-1, 0], values[0, 0]))
savefig('stock_price.png', dpi=150)

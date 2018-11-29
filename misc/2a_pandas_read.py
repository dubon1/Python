#!/usr/bin/python3


import pandas as pd
import dateutil 

conv=pd.read_csv('phone_data.csv', sep='\t', skiprows=1)
df=pd.DataFrame(conv.values, columns=['date', 'duration', 'item', 'month', 'network', 'network_type'])

df['date'] = df['date'].apply(dateutil.parser.parse, dayfirst=True)
print(df['date'])

print('total row count ')
print(df['item'].count())
print('max duration ')
print(df['duration'].max())

print(' How many seconds of phone calls are recorded in total?')
print(df['duration'][df['item'] == 'call'].sum())

print(df.groupby(['month']).groups.keys())

# not sorted by month
print(' How many entries/rows are there for each month?')
print(df['month'].value_counts())

# sort by month, downside is show indexes as well
#df.set_index('month', inplace=True)
print(' How many entries/rows are there for each month?')
print(df.groupby(['month'])['month'].value_counts())

print(' Number of non-null unique network entries')
print(df['network'].nunique())

print('\n\n sort by total no of rows, show index though')
print(df.groupby(['network'])['network'].value_counts().sort_values(ascending=False))

print('\n\n')
print(df.groupby(['month']).groups.keys())
print('\n\n')

print('get the first row for each month ')
print(df.groupby(['month']).first())
print('\n\n')
print(df.groupby(['month']))

print('\n Get the sum of the durations per month \n')
print(df.groupby('month')['duration'].sum())

print('\n Get the number of dates / entries in each month sort by month \n')
print(df.groupby('month')['date'].count())

print('\n\n What is the sum of durations, for calls only, to each network ')
print(df[df['item'] == 'call'].groupby('network')['duration'].sum())



#print(df.groupby(['network'])['network'].value_counts())
# NG
#xx=df.groupby(['month'])['month'].value_counts()
#print(xx.sort_values(['month']))




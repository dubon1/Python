#!/usr/bin/python3


import pandas as pd
import dateutil 

conv=pd.read_csv('phone_data.csv', sep='\t', skiprows=1)
df=pd.DataFrame(conv.values, columns=['date', 'duration', 'item', 'month', 'network', 'network_type'])

df['date'] = df['date'].apply(dateutil.parser.parse, dayfirst=True)
#print(df['date'])

print('\n\n What is the sum of durations, for call/sms/data, to each network ')
print(df.groupby(['item', 'network'])[['duration']].sum())

#  select month, network_type, sum(duration) 
#    from table
#   group by month, network_type;
#print('\n\ntotal calls/texts/data are sent per month, split by network_type?')
#print(df.groupby(['month', 'network_type'])['date'].count())
#print(df.groupby(['month', 'network_type'], as_index=False)['duration'].sum())

#print('\n\n')
#print(df.groupby('month', as_index=False).agg({"duration": "sum"}))

print(' very powerful groupby ')
print(df.groupby(['month', 'item']).agg({'duration':sum,   'network_type': "count", 'date': 'first'}))   
   # find the sum of the durations for each group
   # find the number of network type entries
   # get the first date per group

print('\n\n Group the data frame by month and item and extract a number of stats from each group')
print(df.groupby(['month', 'item']).agg({'duration': [min, max, sum],    
                                     'network_type': "count", 
                                     'date': [min, 'first', 'nunique']}))    
  # find the min, max, and sum of the duration column
  # find the number of network type entries
  # get the min, first, and number of unique dates per group

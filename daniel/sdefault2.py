#!/usr/bin/python3 

from collections import defaultdict, OrderedDict


# list 
s=[('yellow',1),('blue',2),('blue',10),('yellow',3),('blue',4),('red',1)]

dict2=defaultdict(list)
for k, v in s:
    dict2[k].append(v)

for each in dict2:
   print('key is ', each, ' value: ', dict2[each])

print('\n\n\n')
# YAHOO
for k, v in dict2.items():
    for each_value in v:
      print('key is ', k, ' EACH KEY:', each_value)     

#print(zip(*(v for k,v in dict2.items())))
#print(list(zip(*(v for k,v in dict2.items()))))

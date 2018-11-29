#!/usr/bin/python3 

# show to conver tubles into dictionary
from collections import defaultdict, OrderedDict

DATA_SOURCE = (('key1', 'value1'),
               ('key1', 'value2'),
               ('key2', 'value3'),
               ('key2', 'value4'),
               ('key2', 'value5'),)

#  method 1
newdata1 = {}
for k, v in DATA_SOURCE:
  # if newdata1.has_key(k):      # for python 2
    if newdata1.setdefault(k):   # for python 3
        newdata1[k].append(v)
    else:
        newdata1[k] = [v]
print(newdata1)
print('\n\n\n')


#  method 2
newdata2 = {}
for k, v in DATA_SOURCE:
    newdata2.setdefault(k, []).append(v)  
print(newdata2)
print('\n\n\n')


#  method 3
newdata3 = defaultdict(list)
for k, v in DATA_SOURCE:
    newdata3[k].append(v)
 
for k, v in newdata3.items():
  print('key is ', k, '  value: ', v)
  for each_value in v:
    print('key is ', k, ' each value : ', each_value)




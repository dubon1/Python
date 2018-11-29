#!/usr/bin/python3 

import collections

def default_factory():
    return 'How are you Today '


#d = collections.defaultdict(default_factory, foo='bar')
#print('d:', d)
#print('foo =>', d['foo'])
#print('bar =>', d['bar'])

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
  d[k].append(v)

print(sorted(d.items()))

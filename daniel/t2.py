#!/usr/bin/python3 

import collections

s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
  d[k] += 1

print(sorted(d.items()))
print("\n\n")


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
e = collections.defaultdict(list)
for k, v in s:
  e[k].append(v)
print(sorted(e.items()))

print("\n\n")

#somedict = {}
#print(somedict[3]) # KeyError

somedict = collections.defaultdict(int)
print(somedict[3]) 


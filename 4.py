#!/usr/bin/python3

import numpy as np

#  animals = ['cat', 'dog', 'monkey']
#  for idx, animal in enumerate(animals):
#      print('#%d: %s' % (idx + 1, animal))


#choices=['pizza', 'pasta', 'salad', 'nachos']
choices=['pizza']
for idx, item in enumerate(choices, start=3):
 print (idx, item)

print ("if you like %s then you will love" % (choices))

#for i in range(5):
# print(i, "  ")

b=np.array([[1,10,106], [2, 20, 200]])
print(b.shape)
print(b[0, 0], b[0, 2], b[1,1], b[1,2])



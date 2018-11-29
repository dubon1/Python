#!/usr/bin/python3 

import random, string

def randomword(length):
 return ''.join(random.choice(string.ascii_lowercase) for i in range(length)) 

print(randomword(10))
 

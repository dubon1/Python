#!/usr/bin/python3

# print out word shows only once
#
from string import punctuation, whitespace
import re

 
def nonce(filename):
 data=open(filename, 'rt').read()
 d, result = dict(), []

 for word in re.split('['+punctuation+whitespace+']', data):
   d[word.lower()] = d.get(word.lower(), 0)+1

 for word, occur in d.items():
   if occur == 1:
      result.append(word)
 return result

out1=nonce('new_out.txt')
print(out1) 
print(help(re.match)) 
   

#!/usr/bin/python3

import sys

# need massage line 200 for ceo John since he has no boss 
#
with open("emp_mgr_raw", encoding="ISO-8859-1") as f1, open("d1.txt", 'w') as f2:
   next(f1)
   for ea in f1:
     a1=ea.strip().split("\t")
     f2.write(a1[0].lower() + '|' + a1[1].lower() + '|')
     f2.write(a1[5].lower() + '|') 
     f2.write(a1[6].lower().split()[0] + '|' + a1[6].lower().split()[1] + '\n')



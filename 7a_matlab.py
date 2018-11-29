#!/usr/bin/python3


with open('matlab_license2.csv') as f1, open('mat7b.txt', 'w') as f2:
 next(f1)
 for ea in f1:
   a1=ea.strip().split("|")
 # f2.write(a1[0] + '|' +  a1[1] + '|' + a1[5] + '|' + a1[6]  + '\n')
   f2.write(a1[0] + '|' +  a1[1] + '|' + a1[4] + '|'  + a1[7] + '|' + a1[8] + '|'  +  a1[11]  +  '\n')

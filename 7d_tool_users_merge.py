#!/usr/bin/python3

previousu='xxxx'
with open("pds2.txt", encoding="ISO-8859-1") as f1, open("prod_users_list.txt", 'w', encoding='ISO-8859-1') as f2:
  next(f1)
  for ea in f1:
    a1=ea.strip().split("|")
    if previousu in a1[0]:
       f2.write(',' + a1[1])
    else:
       f2.write('\n')
       f2.write(a1[0] +  '|' + a1[1])
    previousu=a1[0]
    previoust=a1[1]


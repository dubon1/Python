#!/usr/bin/python3

# araceli.garza|TAG00924
# atul.khiste|TAG00465
# atul.khiste|TAG00927


previousu='xxxx'
with open("d2.txt", encoding="ISO-8859-1") as f1, open("d3.txt", 'w') as f2:
  next(f1)
  for ea in f1:
    a1=ea.strip().split("|")
    if previousu in a1[0]:
       f2.write(',' + a1[1]) 
    else:
       f2.write('\n')
       f2.write(a1[0].lower() +  '|' + a1[1])
    previousu=a1[0] 
    previoust=a1[1] 


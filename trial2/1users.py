#!/usr/bin/python3


# after get d1.txt, DO   sort -t "|"  -k 1 d1.txt > d2.txt

with open("user_computer.csv", encoding="ISO-8859-1") as f1, open("d1.txt", 'w') as f2:
  next(f1)
  for ea in f1:
    a1=ea.strip().split("\t")
    f2.write(a1[2].lower() +  '|' + a1[0] + '\n')
 #  f2.write(a1[0] +  '|' + a1[2].lower() + '\n')

#   f2.write(a1[2] + '|' +a1[7] + '\n')
#   try:
#       f2.write(a1[2].lower() + '\n')
#   except IndexError:
#       pass

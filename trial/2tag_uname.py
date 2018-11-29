#!/usr/bin/python3


with open("trial_data1.csv") as f1, open("tag_uname.txt", 'w') as f2:
  next(f1)
  for each_line in f1:
    line_array=each_line.strip().split(",")
    if (len(line_array[1]) > 1):
       f2.write(line_array[0] + '|' + line_array[1].lower().replace(' ','.') + '\n')

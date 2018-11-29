#!/usr/bin/python3

with open("trial_data1.csv") as f1, open("user_name.txt", 'w') as f2:
  next(f1)
  for each_line in f1:
    line_array=each_line.strip().split(",")
    if (len(line_array[2]) > 1):
       f2.write(line_array[2].lower() + '\n')

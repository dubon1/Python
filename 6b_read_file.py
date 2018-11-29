#!/usr/bin/python3

### NG
import pandas as pd

f1 = pd.read_csv('my_data3.txt', sep='|', encoding='ISO-8859-1')
f2 = open("new_out.txt", 'w')

#with each_line in f1:
with pd.read_csv('my_data3.txt', sep='|', encoding='ISO-8859-1') as f1:
 for each_line in f1:
# each_line_array=f1.strip().split("|")

  each_line_array=each_line.strip().split("|")
  f2.write(each_line_array[0] + '|' + each_line_array[1] + '|' + each_line_array[2] + '|' + each_line_array[3] + '\n') 
# print(each_line_array[0] + '|' + each_line_array[1] + '|' + each_line_array[2]) 
    
 

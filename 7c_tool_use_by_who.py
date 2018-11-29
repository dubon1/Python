#!/usr/bin/python3

#   sort -t "|" -k 1 pds.txt > pds2.txt

import pandas as pd
import numpy as  np

with open("matlab_license2.csv") as f1, open("pds.txt", 'w') as f2:
  for each_line in f1:
   array=each_line.strip().split("|")
   if ('Individual' in array[4]): 
      f2.write(array[7] +  '|' + array[1] + '\n')


#df=pd.DataFrame(conv.values, columns=['License Number','License Label','Master License Number','Master License Label','License Option','License Use','Activation Key','Product Name','Product Seats','License Term','File Expiration Date','Software Maintenance Service End Date','Validate From Product Setting'])




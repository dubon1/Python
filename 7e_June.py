#!/usr/bin/python3


import pandas as pd
import numpy as  np

def check(product_name):
  ufile=open("matlab_up.csv")
  yahoo=-12000  
  for eline in ufile:
      a4=eline.split("|")
      if product_name in a4[0]:
         if 'Individual' in a4[1]:
           yahoo=a4[3]
           break
  return yahoo



with open("matlab_license2.csv") as f1, open("june_ind.txt", 'w') as f2:
  for each_line in f1:
   array=each_line.strip().split("|")
   if ('Individual' in array[4]): 
      if('Jun' in array[11]):
        google=check(array[7]) 
        print("the price is ",  int(google))
        if  (int(google) > 0):
            f2.write(array[7] +  '|' + array[1] + '|' + array[11] + '|'  + google +'\n')


#df=pd.DataFrame(conv.values, columns=['License Number','License Label','Master License Number','Master License Label','License Option','License Use','Activation Key','Product Name','Product Seats','License Term','File Expiration Date','Software Maintenance Service End Date','Validate From Product Setting'])




#!/usr/bin/python3

import numpy as np
import pandas as pd

data={'Name': ['Tom', 'Daniel', 'Rita', 'Aaron', 'Vincent'],
      'Age' : [28, 32, 98, 32, 43]} 
df=pd.DataFrame(data)
print(df)
print("\n")

print("             Sort by Age, then Name \n")
print(df.sort_values(["Age", "Name"], ascending=[True, True]))
print("\n\n")

print("             Rename index 0,1 ... to custom name \n")
dg=pd.DataFrame(data, index=['My Colleague', 'Youngest kid', 'Wife', 'Son', 'Self'])
#print(dg)
print(dg.sort_values(["Age", "Name"], ascending=[True, True]))


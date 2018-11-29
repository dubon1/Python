#!/usr/bin/python3

import numpy as np
import pandas as pd

from pandas import DataFrame, Series

df = pd.DataFrame({'int_col'   : [1, 10, 100, -1000, 30], 
                   'float_col' : [0.1, 0.01, 29.99, 3.45, None],
                   'string_col': ['Daniel', 'Rita', 'Aaron', 'Vincnt', 'ftp']}) 
#print(df)
print(df[['float_col', 'string_col']])
print("\n\n\n")

d = {'foo':[100, 111, 222], 
     'bar':[333, 444, 555]}
df = pd.DataFrame(d)
print(df)
print("\n\n\n")


data={'Name': ['Tom', 'Daniel', 'Rita', 'Aaron', 'Vincent'],
      'Age' : [28, 45, 98, 32, 43]} 
df=pd.DataFrame(data)
print(df)
print("\n\n\n")

#!/usr/bin/python3

import numpy as np
import pandas as pd

# list (row oriented)
sales1   = [('Jones LLC', 150, 200, 340),
           ('Google', 2500, 4500, 6000),
           ('Facebook', 3500, 2500, 6300),
           ('Hewlett Packard Enterprise', 2500, 1500, 3300),
           ('Yahoo', 18, 46, 60)]
labels1 = ['Company Name', 'January', 'February', 'March']

df=pd.DataFrame.from_records(sales1, columns=labels1)
print("         Row oriented data, easy to understand\n")
print(df)
print("\n\n")

print("          sort by Company name\n")
print(df.sort_values(by='Company Name'))
print("\n\n")

print("          sort by February sales volume \n")
print(df.sort_values(by='February'))
print("\n\n")

dg=pd.DataFrame.from_records(sales1, index=['Nobody Company', 
                                           'VIP',
                                           'Next to Best Company',
                                           'Rundown Company',
                                           'Dinago'])
print("          sort by February sales volume with new index \n")
print(dg)

#!/usr/bin/python3

import numpy as np
import pandas as pd

# list (column oriented)
sales1   = [('Company Name', ['Google', 'Facebook', 'Hewlett Packard Enterprise', 'Yahoo']),
            ('January', [2500, 3500, 2500, 18]),
            ('February', [4500, 2500, 1500, 46]),
            ('March', [6000, 6300, 3300, 60])]


# is from_items,  NOT from_records
df=pd.DataFrame.from_items(sales1)
print("\n                       Column name oriented's list, please compare to 5c* pgm \n")
print(df)
print("\n\n")


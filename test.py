#!/usr/bin/python3

import pandas as pd
import numpy as np

conv=pd.read_csv('mat7b.txt', sep='|', header=None)
df=pd.DataFrame(conv.values, columns=['License_No',  'License_Type', 'Ind_or_Con', 'Product_Name', 'copy', 'Expiration_Date'])

xx=df.groupby(['Product_Name', 'Ind_or_Con'])['copy'].sum().reset_index()
print(xx.sort_values(['Product_Name', 'Ind_or_Con', 'copy'], ascending=True))

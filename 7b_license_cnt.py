#!/usr/bin/python3

import pandas as pd
import numpy as np


conv=pd.read_csv('mat7b.txt', sep='|', header=None)
df=pd.DataFrame(conv.values, columns=['License_No',  'License_Type', 'Ind_or_Con', 'Product_Name', 'copy', 'Expiration_Date'])
#grouped=df.groupby('Product_Name')
#print(grouped['copy'].agg([np.sum]))

# method 1
#grouped=df.groupby(['Product_Name', 'Ind_or_Con'])
#print(grouped['copy'].agg([np.sum]))

# method 2
#print(df.groupby(['Product_Name', 'Ind_or_Con'])['copy'].sum())

# method 3
xx=df.groupby(['Product_Name', 'Ind_or_Con'])['copy'].sum().reset_index()
print(xx.sort_values(['Product_Name', 'Ind_or_Con', 'copy'], ascending=True))




#print(df.groupby(['Product_Name', 'Ind_or_Con']).sum('copy').sort('Product_Name'))   NG
#print(df.groupby('Product_Name')['Ind_or_Con'].sum('copy').sort('Product_Name'))     NG


#col_names=["License_No",  "License_Type", "Ind_or_Con", "Product_Name", "copy", "Expiration_Date"]
#df=pd.read_csv('mat7b.txt', sep='|', names=col_names





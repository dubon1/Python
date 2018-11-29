#!/usr/bin/python3

import pandas as pd

reviews=pd.read_csv("ign.csv")
#print(reviews.shape)
#print(reviews.head())
print(reviews.iloc[1:3, 4:])

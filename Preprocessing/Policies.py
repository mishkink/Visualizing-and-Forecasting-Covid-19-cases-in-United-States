import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df2 = pd.read_csv('policies1.csv')

print(df2.columns)

# print(df2['STAYHOME'])
df2=df2.iloc[4:55]
df2.drop(df2.columns.difference(['State','STATE','RELIGEX','FMFINE','RSTOUTDR','NOPAYCOV','VBMAUTOBAL']), 1, inplace=True)


frame2 = pd.DataFrame(df2)
frame2.to_csv('PP.csv')

d=pd.read_csv('PP.csv')






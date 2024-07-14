import pandas as pd
import numpy as np
df=pd.read_csv('mydata1.csv')
print("Before Droping values")
print(df)
print()
# print("After Droping  row Values")
# newdf=df.dropna(axis=0)
# print(newdf)
print("After Droping column Values")
newdf=df.dropna(axis=1)
print(newdf)
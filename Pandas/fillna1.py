import pandas as pd
import numpy as np
df=pd.read_csv('mydata1.csv')
print("Before filling NaN values")
print(df)
print()
print("After filling NaN Values")
newdf=df.fillna(100)
print(newdf)
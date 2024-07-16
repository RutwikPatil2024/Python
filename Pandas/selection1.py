import pandas as pd
import numpy as np
df=pd.read_csv('mydata1.csv')
# print("Before Replacing")
# print(df)
# print("After Replacing")
# newdf=df.replace(np.nan,0,inplace=True)
# df.replace(np.nan,0,inplace=True)
print()
# newdf=df.loc[1:3,["Maths","Science"]]
# Selecting single row
# newdf=df.iloc[1]
# print(newdf)
# print(df.loc[1])
# print(pd.options.display.max_rows)
print(df.info())

import pandas as pd
import numpy as np
df=pd.read_csv('mydata1.csv')
print(df)
# row=df.loc[[1,2,3]]
# row=df.loc[1:3]
# print(row)
# col=df.loc[:,"Maths"]
# col=df.loc[:,["Maths","Science"]]
# print(col)
rowcol=df.loc[[1,2],["Maths","Science"]]
print(rowcol)

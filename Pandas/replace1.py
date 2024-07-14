import pandas as pd
import numpy as np
df=pd.read_csv('mydata1.csv')
print("Before Replacing Vaues")
print(df)
print("After replacing values")
# newdf=df.replace(90,1000)
# newdf=df.replace(np.nan,2000)
newdf=df.replace({np.nan:88,100:88})
print(newdf)
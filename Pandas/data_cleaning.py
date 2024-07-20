import numpy as np
import pandas as pd
df=pd.read_csv("data.csv")

#calculating mean
# x=df["Calories"].mean()

# filling empty values with mean
# df["Calories"]=df["Calories"].fillna(x)

# to save changes back to dataframe to csv
# df.to_csv("data.csv",index=False)
#  -----------------------------------------
# me=df["Duration"].mean()
# print(me.dtype)
# for x in df.index:
#     if df.loc[x,"Duration"] >90:
#         df.loc[x,"Duration"]=np.int64(me)
# data in Duration is int64 so to convet mean data(float64) to int64

# save changes to csv from dataframe
# df.to_csv("data.csv",index=False) 
# -------------------------------------------
for x in df.index:
    if df.loc[x,"Calories"]>1000:
        df.loc[x,"Calories"]=350

df.to_csv("data.csv",index=False)



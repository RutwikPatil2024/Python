import pandas as pd
import numpy as np
data={
    "Maths":[80,np.nan,85,100,90,95],
    "Science":[100,90,95,np.nan,85,80],
    "English":[90,95,80,90,100,np.nan]
}
index=["Ram","Shyam","Rutwik","Raju","Ganesh","Varun"]
column=["Maths","Science","English"]
copy=False
df=pd.DataFrame(data=data,index=index,columns=column,copy=copy)
# print(df)
df.to_csv("mydata1.csv",index=False)
print("Data Written Sucessfully to csv file")
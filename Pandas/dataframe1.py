import pandas as pd
data={
    "Maths":[80,90,85,100,90,95],
    "Science":[100,90,95,80,85,80],
    "English":[90,95,80,90,100,80]
}
index=["Ram","Shyam","Rutwik","Raju","Ganesh","Varun"]
column=["Maths","Science","English"]
name="Student info"
copy=False

df=pd.DataFrame(data=data,index=index,copy=copy,columns=column)
print(df)
print("Transpose is : \n",df.T)
print()
print("Shape is : ",df.shape)
print()
print(df["Maths"])
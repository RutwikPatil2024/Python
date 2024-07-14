import pandas as pd
data=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]
# index=["A","B","C","D","E"]
dtype=int
name="series"
copy=True

ser=pd.Series(data=data,dtype=dtype,name=name,copy=copy)
# print(ser["A":"D"])
# print(ser.axes)
# print(ser.dtype)
# print(ser.name)
# print(ser.empty)
# print(ser.ndim)
# print(ser.size)
# print(ser.head())
# print(ser.tail())
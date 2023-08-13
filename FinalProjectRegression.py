import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
data = pd.read_excel("FinalProjectRegression.xlsx")

# IsNull = data.isnull().sum()

data = data.drop(["Id","Alley","FireplaceQu","PoolQC","Fence","MiscFeature"],axis=1)
IsNull = data.isnull().sum()
data = data.dropna()
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_Object= x.select_dtypes(include="object")
x_NotObject= x.select_dtypes(exclude="object")

l=LabelEncoder()

for i in range (0,x_Object.shape[1]):
    x_Object.iloc[:,i]=l.fit_transform(x_Object.iloc[:,i])  
All_X= pd.concat([x_Object,x_NotObject],axis=1)

x_train,x_test,y_train,y_test = train_test_split(All_X,y,train_size=.9)
# m=LinearRegression()
# m.fit(x_train,y_train)
# print(m.score(x_train,y_train))
# print(m.score(x_test,y_test))
r = RandomForestRegressor()
r.fit(x_train,y_train)
print(r.score(x_train,y_train))
print(r.score(x_test,y_test))
















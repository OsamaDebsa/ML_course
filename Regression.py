# Regression

"""
When we need to make Regression on something
the PC must study old data for this thing 
to make Regression - so we give the PC all old data ?? 
No we give The pc some of this data to PC and the
other some of this data we use it to make test for model
after PC Study or train on the Data 
"""


# EX.1 : 
# linear Regression only one variable.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_excel("Regression1.xlsx")

# To print Specific columns ---> print(head())
# print(data.head(4))

# To know the size of the Table ---> shape
# print(data.shape)

# To cheak if the data has any None value ---> isnull().sum()
# print(data.isnull().sum())

# To Remove any Column that has None value
# data = data.dropna()

data = data.dropna()
print(data.isnull().sum())
print("\n")

# We all know loc[] Function and we know that it cut specifi rows and columns
# and also know iloc[] function such as loc function but we used index .

x = data.iloc[:,:1] # all Rows & specific columns
y = data.iloc[:,1:]


# Now we need to give PC Some Data and Save Other Some ---> train_test_split 
# train_test_split() ---> take (Row & column & test_size).
# train_test_split() ---> Return Four variable two train & two test.
x_train,x_test ,y_train ,y_test = train_test_split(x,y,test_size=.75)



# Then We Call LinearRegression() and save as variable <--- This Object.
# Then We Pass The Train Data.
m = LinearRegression()
m.fit(x_train,y_train)


# Finnaly To Know the accuracy ---> score().
# score function take Test Data.
print("accuracy of training :")
print(m.score(x_train, y_train)) # ---> accuracy of Learning.
print("\n")

print("accuracy of testing :")
print(m.score(x_test, y_test)) # ---> accuracy of cheack .
print("\n")


# Print Plots :
    
x_train =np.array(x_train)
y_train = np.array(y_train)

plt.scatter(x_train, y_train,color="r")
plt.plot(x_train, m.predict(x_train), color="k")
plt.show()

x_test =np.array(x_test)
y_test = np.array(y_test)

plt.scatter(x_test, y_test,color="b")
plt.plot(x_test, m.predict(x_test),color="k")
plt.show()

"""




# EX.2 :
# linear Regression multi variable.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data = pd.read_excel("Regression2.xlsx")

# print(data.head(5))
# print(data.isnull().sum())

x = data.iloc[:,:-1]
y = data.iloc[:,-1:]



# If I have Grade Of Stydent such as (A & B & C)
# and I want to transfprm this Grade into GPA to take 
# some descision the progrma need to operate with only numbers 
# so i must convert Grade into GPA - this operation called preprocessing.



# I will split x into two variable : one is all data string and other int .
# Then I will convert sting data (object) to labels .

x_object = x.select_dtypes(include=["object"])
x_non_object = x.select_dtypes(exclude=["object"])


l=LabelEncoder()
for i in range(x_object.shape[1]):                          # ---> for i in range column in table :
    x_object.iloc[:,i]=l.fit_transform(x_object.iloc[:,i])  # ---> Transport object's column by int.


all_x=pd.concat([x_object,x_non_object],axis=1)


x_train,x_test,y_train,y_test = train_test_split(all_x,y,test_size=.75)


m = LinearRegression()
m.fit(x_train, y_train)


print("accuracy of training :")
print(m.score(x_train, y_train)) # ---> accuracy of Learning.
print("\n")


print("accuracy of testing :")
print(m.score(x_test, y_test)) # ---> accuracy of cheack .
print("\n")

"""



# EX.3 :
# Non-linear Regression (polynomial Regression)

    
        # if we solve this EX. as (linear Regression) we find the solv is not true :
"""
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import LabelEncoder
        data = pd.read_excel("Regression3.xlsx")
        #print(data.head(5))
        #print(data.isnull().sum())
        
        x = data.iloc[:,:-1]
        y = data.iloc[:,-1:]
        
        x_train,x_test ,y_train ,y_test = train_test_split(x,y,test_size=.7)
        m = LinearRegression()
        m.fit(x_train,y_train)
        print("accuracy of training :")
        print(m.score(x_train, y_train)) # ---> accuracy of Learning.
        print("\n")
        print("accuracy of testing :")
        print(m.score(x_test, y_test)) # ---> accuracy of cheack .
        print("\n")
        
        x=np.array(x)
        y=np.array(y)
        plt.scatter(x, y)
        plt.plot(x,m.predict(x))
        plt.show()
"""


# The solve using Non-linear Regression (polynomial Regression) :
    
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_excel("Regression3.xlsx")

x = data.iloc[:,:-1]
y = data.iloc[:,-1:]



# degree = Type Of Function 
# We will add x becouse degree = 2 so ===> (x*x) as a new column  
# p = PolynomialFeatures(degree=2)
# p = PolynomialFeatures(degree=3)

p = PolynomialFeatures(degree=4) # in this EX. ===> (degree = 4) give the best score.

p_x = p.fit_transform(x)

m = LinearRegression()
m.fit(p_x, y)

print(m.score(p_x, y))

x = np.array(x)
y = np.array(y)
p_x = np.array(p_x)

plt.scatter(x, y)
plt.plot(x, m.predict(p_x))
plt.show()

"""








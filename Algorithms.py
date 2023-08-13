# Decision Tree Algorithm :
# EX.1 - Classification :
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
data = pd.read_excel("Algorithms1.xlsx")
# print(data.isnull().sum())
# print(data.shape)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.9)
m = DecisionTreeClassifier()
# m = DecisionTreeClassifier(max_depth=(5)) # ===> max_depth=() : depth of Nodes Tree.
m.fit(x_train, y_train)
print(m.score(x_train, y_train))
print(m.score(x_test, y_test))
"""

# EX.2 - Regresision :
"""
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
data = pd.read_excel("Algorithms2.xlsx")
# print(data.isnull().sum())
data = data.dropna()
# print(data.shape)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.9)
m = DecisionTreeRegressor()
# m = DecisionTreeRegressor(max_depth=(5)) # ===> max_depth=() : depth of Nodes Tree.
m.fit(x_train, y_train)
print(m.score(x_train, y_train))
print(m.score(x_test, y_test))
"""


# Random Forest Algorithm :
# EX.1 - Classification :
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
data = pd.read_excel("Algorithms1.xlsx")
# print(data.isnull().sum())
# print(data.shape)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.9)
m = RandomForestClassifier()
# m = RandomForestClassifier(n_estimators=5,max_depth=(5)) # ===> n_estimators : N. of tree
m.fit(x_train, y_train)
print(m.score(x_train, y_train))
print(m.score(x_test, y_test))
"""

# EX.2 - Regresision :
"""
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
data = pd.read_excel("Algorithms2.xlsx")
# print(data.isnull().sum())
data = data.dropna()
# print(data.shape)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.9)
m = RandomForestRegressor()
# m = RandomForestRegressor(n_estimators=5,max_depth=(5)) # ===> n_estimators : N. of tree
m.fit(x_train, y_train)
print(m.score(x_train, y_train))
print(m.score(x_test, y_test))
"""


# Nearest Neighbor Algorithm :
# EX.1 - Classification :
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
data = pd.read_excel("Algorithms1.xlsx")
# print(data.isnull().sum())
# print(data.shape)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.9)
m = KNeighborsClassifier()
# m = KNeighborsClassifier(n_neighbors=9) ===> n_neighbors : it prefer to give it odd N.
m.fit(x_train, y_train)
print(m.score(x_train, y_train))
print(m.score(x_test, y_test))
"""

# EX.2 - Regresision :
"""
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
data = pd.read_excel("Algorithms2.xlsx")
# print(data.isnull().sum())
data = data.dropna()
# print(data.shape)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=.9)
m = KNeighborsRegressor()
# m = KNeighborsRegressor(n_neighbors=9) ===> n_neighbors : it prefer to give it odd N.
m.fit(x_train, y_train)
print(m.score(x_train, y_train))
print(m.score(x_test, y_test))
"""











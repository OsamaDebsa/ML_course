# classification :
    
# EX.1:
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearnex.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_excel("Classification1.xlsx")
# print(data.head(4))
# print(data.shape)
# print(data.isnull().sum())
x = data.iloc[:,:12]  # OR ---> x = data.iloc[:,:-1]
y = data.iloc[: ,12:] # OR ---> y = data.iloc[: ,-1]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m = LogisticRegression()
m.fit(x_train,y_train)

print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
"""


# EX.2 :
# multi-classification
# first method for multi-classification "OVA" OR "OVR" :
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data = pd.read_excel("classification2.xlsx")

# print(data.head(4))
# print(data.shape)
# print(data.isnull().sum())
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m = LogisticRegression(multi_class="ovr")
m.fit(x_train, y_train)

print(m.score(x_train, y_train))
print(m.score(x_test,y_test))
"""


# EX.3 :
# multi-classification
# second method for multi-classification "OVA" OR "OVR" :
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
data = pd.read_excel("classification2.xlsx")

# print(data.head(4))
# print(data.shape)
# print(data.isnull().sum())
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m = OneVsRestClassifier(LogisticRegression())
m.fit(x_train, y_train)

print(m.score(x_train, y_train))
print(m.score(x_test,y_test))
"""

# EX.4 :
# multi-classification
# multi-classification "OVO":
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsOneClassifier
data=pd.read_excel("classification2.xlsx")
# print(data.head(4))

x = data.iloc[:,:-1]
y = data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m = OneVsOneClassifier(LogisticRegression())
m.fit(x_train, y_train)

print(m.score(x_train, y_train))
print(m.score(x_test,y_test))

"""










































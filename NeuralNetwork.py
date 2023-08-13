# neural network :
# classification :
# EX.1 :
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
data = pd.read_excel("NeuralNetwork1.xlsx")
# print(data.head(4))
# print(data.isnull().sum())
# print(data.shape)
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m=MLPClassifier(hidden_layer_sizes=(64,128,32),learning_rate="constant",learning_rate_init=.002,max_iter=500) # three layers and Number Of Cell in each layer = (64,128,32) # learning_rate ===> α - Alpha 
m.fit(x_train,y_train)
print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
"""


# EX.2 :
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
data = pd.read_excel("NeuralNetwork1.xlsx")
# print(data.head(4))
# print(data.isnull().sum())
# print(data.shape)
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m=MLPClassifier()
m.fit(x_train,y_train)
print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
"""


# Regrssion :
# EX.3 :
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
data = pd.read_excel("NeuralNetwork2.xlsx")
data = data.dropna()
# print(data.head(4))
# print(data.isnull().sum())
# print(data.shape)
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)
m=MLPRegressor()
m.fit(x_train, y_train)
print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
"""

# EX.4 :
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
data = pd.read_excel("NeuralNetwork2.xlsx")
data = data.dropna()
# print(data.head(4))
# print(data.isnull().sum())
# print(data.shape)
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=.9)

m=MLPRegressor(activation="relu",max_iter=200)
# m=MLPRegressor(activation="identity")
# m=MLPRegressor(activation="tanh",max_iter=2000)
# m=MLPRegressor(activation="logistic",max_iter=2000)

m.fit(x_train, y_train)
print(m.score(x_train,y_train))
print(m.score(x_test,y_test))
"""











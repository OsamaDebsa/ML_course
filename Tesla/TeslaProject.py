import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Building the regression model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# For preprocessing
from sklearn.preprocessing import StandardScaler
# For model evaluation
from sklearn.metrics import mean_squared_error as mse


tesla = pd.read_excel("tesla.xlsx")

# print(tesla.head(6))

# print(tesla.shape)

# print(tesla.isnull().sum())

# tesla.info()

# print(tesla)
# print("\n")

# tesla['Date'] = pd.to_datetime(tesla['Date'])
# print(f'Range of Date is between {tesla.Date.min()} {tesla.Date.max()}')
# print(f'Total N. of Days = {(tesla.Date.max()  - tesla.Date.min()).days} days')
# Total Days = 3181 days.


"""
plt.title("Stock Prices of Tesla")
plt.xlabel("Date")
plt.ylabel("price")
plt.plot(tesla['Date'], tesla['Close'], "-r", linewidth=.75)
# plt.legend() // if i want to give inner label
plt.show()
"""
# loc[] Function that it cut specific rows and columns
# Split the data into train and test
X = np.array(tesla.index).reshape(-1, 1)
Y = tesla['Close']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.3, random_state=101)

# Feature scaling
#This is done to ensure that all the features are on a similar scale,
# which can improve the performance of the model.
scaler = StandardScaler().fit(X_train)

# Creating a linear Model
LR = LinearRegression()
LR.fit(X_train, Y_train)

plt.style.use("seaborn")
x = X_train.T[0]
y = Y_train

plt.scatter(x, y, marker="o", c="r", s=50, label="Actual") # ---> Note : c --> Color & s --> Size of the symbol
# marker ---> "o" OR "O" OR "x" OR "X" OR "+" OR "v" OR "^" OR "<" OR ">" OR "." OR "," OR "s" OR "d" .

plt.plot(x, LR.predict(X_train).T, linewidth=4, color="blue",label= "Predicted")
plt.legend()
plt.show()


# Finnaly To Know the accuracy ---> score().
# score function take Test Data.
print("\n")
print("Accuracy of Training :")
print(LR.score(X_train, Y_train)) # ---> accuracy of Learning.
print("\n")
print("Accuracy of Testing :")
print(LR.score(X_test, Y_test)) # ---> accuracy of cheack .
print("\n")

#Mean squared error MSE : Mean for (Actual-Predicted)^2
print("MSE for Training :")
print(mse(Y_train, LR.predict(X_train)))
print("\n")
print("MSE for Testing :")
print(mse(Y_test, LR.predict(X_test)))
print("\n")

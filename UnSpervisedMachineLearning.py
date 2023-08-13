# UnSpervised Machine Learning :
# We Don't need "y" OR output We need Only "x" .
# EX.1 :
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_excel("UnSpervisedMachineLearning.xlsx")

# print(data.head(4))
# print(data.isnull().sum()) 

data = data.drop(["label"],axis=1)

# We make two empity lists The first For N. of Clusters and The Other For {Costs Function OR J-Function (Mistakes)}.
ClusterNumbers=[]
CostFunction = []
# We make for loop to Know Which N. of Claster give me The Less N. of Cost.
for i in range (1,10):
    m=KMeans(n_clusters=i)
    m.fit(data)
    ClusterNumbers.append(i)
    CostFunction.append(m.inertia_)
    
plt.plot(ClusterNumbers,CostFunction)
plt.show()
"""

# After We Know That 4 Cluster Will give me The less N. of Cost :
    
import pandas as pd 
from sklearn.cluster import KMeans

data = pd.read_excel("UnSpervisedMachineLearning.xlsx")

data = data.drop(["label"],axis=1)

m=KMeans(n_clusters=4)
m.fit(data)
   




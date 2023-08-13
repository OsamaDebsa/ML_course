"""
If I have Grade Of Stydent such as (A & B & C)
and I want to transfprm this Grade into GPA to take 
some descision the progrma need to operate with only numbers 
so i must convert Grade into GPA - this operation called preprocessing.
"""

"""
# EX.1 :
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_excel("DataReprocessing1.xlsx")
print(data)
print("\n")

l = preprocessing.LabelEncoder()
labeling = l.fit_transform(data["Grade"])
print(labeling)
print("\n")

data["Grade"]=labeling
print(data)
print("\n")

print(l.classes_)
print("\n")
"""

# EX.2 :
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_excel("DataReprocessing2.xlsx")
print(data)
print("\n")

l = preprocessing.LabelEncoder()
labeling = l.fit_transform(data["Town"])
print(labeling)
print("\n")

data["Town"]=labeling
print(data)
print("\n")

print(l.classes_)
print("\n")
"""





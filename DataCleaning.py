# ---> to make Data Cleaning There are many method to make it <--- #

# First method ---> dropna()
# Remove any raw that have any None.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("DataCleaning.xlsx")
print(data,"\n")
# Note to print size of table : 
print(data.shape,"\n")
NewData = data.dropna()
print(NewData,"\n")
print(NewData.shape,"\n")
"""


# Seconed method ---> drop()
# Remove any column that have any None.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("DataCleaning.xlsx")
print(data,"\n")
print(data.shape,"\n")
# drop([columnsName],axis=1)
# drop([RowsName],axis=0)
NewData = data.drop(["Area","Price"],axis=1)
print(NewData,"\n")
print(NewData.shape,"\n")
"""


# Third method ---> SimpleImputer()
# repalce any None value with determined value.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean") # Note ---> this object.
# strategy ===> "mean" OR "median" OR "most_frequent" OR "Constant" .

data = pd.read_excel("DataCleaning.xlsx")
print(data,"\n")
print(data.shape,"\n")

Cleared_data = imputer.fit_transform(data)
print(Cleared_data,"\n")
print(Cleared_data.shape,"\n")

# To make The output of the data lokelike The input: 
# DataFrame(data,columns=///)
New_Data = pd.DataFrame(Cleared_data,columns=data.columns)
print(New_Data)
"""


















#                    ********** seaborn **********
# first --->  corr() :
#    To print correlation.
#    EX.1 :
"""
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot
data = pd.read_excel("FlatEX.xlsx")       
print(data,"\n")
cor = data.corr()
print(cor,"\n")
"""


# second --->  heatmap() :
#    To print (heat map correlation).
#    EX.1 :
"""
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot
data = pd.read_excel("FlatEX.xlsx")       
print(data,"\n")
cor = data.corr()
print(cor,"\n")
# sns.heatmap(#CorrelationData,# annot=True ---> to print correlation percentile in heatmap)
# sns.heatmap(cor)
sns.heatmap(cor,annot=True)
plt.show()
"""


# third --->  pairplot() :
#    looklike heatmap function but it print scatter plot or histogram . 
#    EX.1 :
"""
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot
data = pd.read_excel("FlatEX.xlsx")       
print(data,"\n")
cor = data.corr()
print(cor,"\n")
# sns.pairplot(#CorrelationData)
sns.pairplot(cor)
plt.show()
"""
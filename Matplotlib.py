#                    ********** Matplotlib **********
# first ---> plot() :
#   to draw satatistical line.
#   EX.1 :
"""       
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60]
y = [100,200,300,400,500,600]
plt.plot(x,y)
plt.show()
"""
#   Ex.2 :
"""
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60]
y = [100,550,500,700,400,900]
plt.plot(x,y)
plt.show()
"""
#   Ex.3 :
"""
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60]
y = [100,550,500,700,400,900]
plt.plot(x,y,linewidth=2.5,color="red")  # ---> color="red"    OR ---> color="r"    OR--->   color="#FF0000" 
plt.show()
"""

# Second ---> style.use() :
#   to make style for plots.
#   EX.1 :
"""
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60]
y = [100,200,300,400,500,600]
#plt.style.use("classic")
#plt.style.use("bmh")
#plt.style.use("seaborn") # ---> perfect
#plt.style.use("seaborn-whitegrid")
#plt.style.use("seaborn-paper")
#plt.style.use("dark_background")
plt.plot(x,y,linewidth=2.5,color="red")
plt.show()
"""
#   EX.2 :
"""
import matplotlib.pyplot as plt
x = [10,20,30,40,50,60]
y = [100,200,300,400,500,600]

#plt.plot(x,y,linewidth=2.5,color="red",linestyle="solid")
#plt.plot(x,y,linewidth=2.5,color="red",linestyle="-")
#------------------------------------------------------------

#plt.plot(x,y,linewidth=2.5,color="red",linestyle="dashed")
#plt.plot(x,y,linewidth=2.5,color="red",linestyle="--")
#------------------------------------------------------------

#plt.plot(x,y,linewidth=2.5,color="red",linestyle="dashdot")
#plt.plot(x,y,linewidth=2.5,color="red",linestyle="-.")
#------------------------------------------------------------

#plt.plot(x,y,linewidth=2.5,color="red",linestyle="dotted")
#plt.plot(x,y,linewidth=2.5,color="red",linestyle=":")
#------------------------------------------------------------

plt.show()

"""
#   EX.3:
"""
import matplotlib.pyplot as plt
x = [20,30,40,50,60,70]
y = [150,250,300,250,270,200]
a = [15,35,45,50,75]    
b = [150,300,255,305,250]
plt.plot(x,y,linewidth=3,color="r",linestyle="--")
plt.plot(a,b,linewidth=3,color="b")
plt.show()
"""
#   EX.4:
"""
import matplotlib.pyplot as plt
x = [20,30,40,50,60,70]
y = [150,250,300,250,270,200]
a = [20,30,40,50,60,70]    
b = [160,250,340,220,290,215]

plt.plot(x,y,"--r",linewidth=3)
#plt.plot(x,y,linewidth=3,color="r",linestyle="--")

plt.plot(a,b,"-b",linewidth=3)
#plt.plot(a,b,linewidth=3,color="b")
plt.show()
"""

# Third ---> title() :
#   to make title to plot.
#   EX.1 :
"""     
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price = np.array([100,200,300,400,500,600])
plt.title("Metr & Price")
plt.plot(metr,price,"--r",linewidth=4)
plt.show()
"""

# Fourth --->  axes() :
#   looklike (xlabel & ylabel & title) but its the best.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price1 = np.array([100,200,300,400,500,600])
price2 = np.array([150,200,350,475,500,550])
a = plt.axes()
a.set(title="Graph",xlabel="X",ylabel="Y")
plt.plot(metr,price1)
plt.show()
"""


#  Fifth ---> xlabel() OR ylabel():
#   to make title to X-axis OR Y-axis.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price = np.array([100,200,300,400,500,600])
plt.title("Metr & Price")
plt.xlabel("Metr")
plt.ylabel("price")
plt.plot(metr,price,"--r",linewidth=4)
plt.show()
"""


#  Sixth ---> xlim() OR ylim():
#   to give serial number to X-axis OR Y-axis.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price = np.array([100,200,300,400,500,600])
plt.title("Metr & Price")
plt.xlabel("Metr")
plt.ylabel("price")
plt.xlim(.5, 10)
plt.ylim(50,1000)
plt.plot(metr,price,"--r",linewidth=4)
plt.show()
"""

#  Seventh --->  label=() & legend() :
#   inner label : we make it to give name as a Note to satatistical line.
#   we must write legend function to make this inner label.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price1 = np.array([100,200,300,400,500,600])
price2 = np.array([150,200,350,475,500,550])
plt.title("Metr & Price")
plt.xlabel("Metr")
plt.ylabel("price")
plt.plot(metr,price1,"--r",linewidth=4,label="tower 1")
plt.plot(metr,price2,"-b",linewidth=4,label="tower 2")
plt.legend()
plt.show()
"""


# Eighth --->  subplot() :
#   subplot function used to make : two separate plots in only one window.
#   subplot(x,y,z) ---> x : is the row of the window , y : is the column in the window , z is the index of the plot.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price1 = np.array([100,200,300,400,500,600])
price2 = np.array([150,200,350,475,500,550])
plt.subplot(2,1,1)
plt.plot(metr,price1,"--r",linewidth=4,label="tower 1")
plt.legend()
plt.subplot(2,1,2)
plt.plot(metr,price2,"-b",linewidth=4,label="tower 2")
plt.legend()
plt.show()
"""
#   EX.2 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price1 = np.array([100,200,300,400,500,600])
price2 = np.array([150,200,350,475,500,550])
plt.subplot(1,2,1)
plt.plot(metr,price1,"--r",linewidth=4,label="tower 1")
plt.legend()
plt.subplot(1,2,2)
plt.plot(metr,price2,"-b",linewidth=4,label="tower 2")
plt.legend()
plt.show()
"""
#   EX.3 :
"""
import matplotlib.pyplot as plt
import numpy as np
metr = np.array([1,2,3,4,5,6])
price1 = np.array([100,200,300,400,500,600])
price2 = np.array([150,200,350,475,500,550])
plt.title("Metr & Price")
plt.xlabel("Metr")
plt.ylabel("price")
plt.subplot(2,1,1)
plt.plot(metr,price1,"--r",linewidth=4,label="tower 1")
plt.legend()
plt.subplot(2,1,2)
plt.plot(metr,price2,"-b",linewidth=4,label="tower 2")
plt.legend()
plt.show()
"""

# Ninth --->  scatter() :
#  to draw satatistical point.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5,6])
y = np.array([10,20,30,40,50,60])
plt.scatter(x, y, marker="o",c="r",s=50) # ---> Note : c --> Color & s --> Size  
# marker ---> "o" OR "O" OR "x" OR "X" OR "+" OR "v" OR "^" OR "<" OR ">" OR "." OR "," OR "s" OR "d" .
plt.show()
"""

#   EX.2 :
"""
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn") # Note ---> this to make style.
x = np.random.rand(20)   # Note ---> this to give me (20) decimal number between (0 to 1)
y = np.random.rand(20)   # Note ---> this to give me (20) decimal number between (0 to 1)
plt.scatter(x, y, marker="X",c="r",s=50)
plt.show()
"""

# Tenth --->  hist() :
#  to draw histogram.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn")
data = ["tiota","kia","marcidis","kia","tiota","BMW","hondai","BMW","tiota"]
plt.hist(data, histtype="bar",alpha=1,bins=15)
plt.show()

# histtype ---> "bar" OR "barstacked" OR "step" OR "stepfilled".
# alpha ---> is responsible for transparency ("1" is zero transparency )
# bins ---> is responsible for the Number of possible bar and it affect on (the Number and size of bar and the space between bars also).
"""

#   EX.2 :
"""
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn")
data = [["tiota","kia","marcidis"],["kia","tiota","BMW"],["hondai","BMW","tiota"]]
plt.hist(data, histtype="bar",alpha=1,bins=9)
plt.show()
"""

#   EX.3 :
"""
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn")
data = [["tiota","kia","marcidis"],["kia","tiota","BMW"],["hondai","BMW","tiota"]]
plt.hist(data, histtype="barstacked",alpha=1,bins=9)
plt.show()
"""

# Eleventh --->  bar() :
#  looklike histogram but bar take (x & y).
#   EX.1 :
"""
import numpy as np
import matplotlib.pyplot as plt 
x = np.array(["tiota","kia","marcidis"])
y = np.array([60,95,120])
plt.bar(x,y,color="r",alpha=1)
plt.show()
"""
#   EX.2 :
"""
import numpy as np
import matplotlib.pyplot as plt 
x = np.array(["tiota","kia","marcidis"])
y = np.array([60,95,120])
plt.bar(x,y,color="r",alpha=1,edgecolor="k",facecolor="w")
# edgecolor ---> is the color of the bar's strock.
# facecolor ---> is the color of the bar itself.
plt.show()
"""

# Twelfth --->  Review EX. :
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("DataNumbers.xlsx",header=0)
print(data)
x = data["name"]
y = data["Sales"]
plt.style.use("seaborn")
a = plt.axes()
a.set(title="Names&Sales",xlabel="Names",ylabel="Sales")
plt.plot(x,y, color="r",linestyle="--") 
plt.bar(x,y,edgecolor="k",facecolor="y")
plt.scatter(x, y, marker="X",c="b",s=100)
plt.show()
"""

# Thirteenth --->  pie() :
#  to draw pie graph.
#   EX.1 :
"""
import matplotlib.pyplot as plt
import numpy as np
CarsNumber = np.array([3,5,9,1])
CarsName = np.array(["tiota","kia","marcidis","BMW"])
plt.pie(CarsNumber, labels = CarsName, labeldistance = 1.1 ,rotatelabels=False,autopct="%1.0f%%",explode=[.1,0,0,0],radius = 1.5,colors=["r","g","c","y"])
plt.show()

# explode=[] ---> if I want to take any pices out of circle.
# radius ---> if I want change the area of circle.
# autopct = "%1.0f%%" ---> to give each pice of circle its percentile.
# rotatelabels ---> if I want to make rotate of the label.
"""

#Fourteenth ---> 3D shapes:
#   EX.1 :
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
a = plt.axes(projection="3d")
XFlatMetr = np.array([100,200,300,400,500])
YpreiceMetr = np.array([1000,1500,2000,2500,3000])
ZNumberOfRooms = np.array([2,3,4,3,2])
a.plot3D(XFlatMetr,YpreiceMetr,ZNumberOfRooms,"red")
plt.show()
"""
#   EX.2 :
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
a = plt.axes(projection="3d")
XFlatMetr = np.array([100,200,300,400,500])
YpreiceMetr = np.array([1000,1500,2000,2500,3000])
ZNumberOfRooms = np.array([2,3,4,3,2])
a.scatter3D(XFlatMetr,YpreiceMetr,ZNumberOfRooms,c="b")
plt.show()
"""
#   EX.3 :
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
a = plt.axes(projection="3d")
XFlatMetr = np.array([100,200,300,400,500])
YpreiceMetr = np.array([1000,1500,2000,2500,3000])
ZNumberOfRooms = np.array([2,3,4,3,2])
a.plot3D(XFlatMetr,YpreiceMetr,ZNumberOfRooms,"red")
a.scatter3D(XFlatMetr,YpreiceMetr,ZNumberOfRooms,c="b")
plt.show()
"""














































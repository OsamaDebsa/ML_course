#                    ********** Pandas **********
# first ---> Series() :
#   give the list arranged index when you print
#   EX.1 :       
"""
import pandas as pd
ls = ["mazen","osama","mohamed","yousef","sara","abdo","ahamed"]
# ls = [30,22,10,14,11,13,9,1,0,64,14,15,17,7]
print(ls,"\n")
ser = pd.Series(ls)
print(ser)
"""
#   EX.2 :       
"""
import pandas as pd
ls = ["mazen","osama","mohamed","yousef","sara","abdo","ahamed"]
print(ls,"\n")
ser = pd.Series(ls,index = ['a','b','c','d','e','f','g']) # Note ---> the number of (index) must = the number of value in list. 
print(ser)
"""
#   EX.3 :       
"""
import pandas as pd
ls = ["mazen","osama","mohamed","yousef","sara","abdo","ahamed"]
print(ls,"\n")
ser = pd.Series(ls,index = ['a','b','c','d','e','f','g']) # Note ---> the number of (index) must = the number of value in list. 
print(ser,"\n")
print(ser.index,"\n")
print(ser.values,"\n")
"""


# Second ---> describe() :
#   give me some mathematical information. 
#   ---> count & mean & std & min & max & IQR. 
#   ---> count & unique & top(mode) & freq.
#   EX.1 :       
"""
import pandas as pd
ls = [30,22,10,14,11,13,9,1,0,64,14,15,17,7]
ser = pd.Series(ls)
print(ser,"\n")
print(ser.describe(),"\n")
"""
#   EX.2 :       
"""
import pandas as pd
ls = ["mazen","osama","mohamed","yousef","osama","sara","abdo","ahamed"]
ser = pd.Series(ls)
print(ser,"\n")
print(ser.describe(),"\n")
"""
#   EX.3 :       
"""
import pandas as pd
ls = [30,22,10,14,11,13,9,1,0,64,14,15,17,7]
ser = pd.Series(ls)
print(ser,"\n")
print(ser.mean(),"\n")
print(ser.std(),"\n")
print(ser.max(),"\n")
print(ser.sum(),"\n")
"""

# Third ---> agg([]) :
#   aggregation ---> تجميع
#   aggregation is function used to give me some specific mathematical information 
#   EX.1 :       
""" 
import pandas as pd
ls = [30,22,10,14,11,13,9,1,0,64,14,15,17,7]
ser = pd.Series(ls)
print(ser,"\n")
print(ser.agg(["min","std","mean"]),"\n")
"""

# Fourth ---> DataFrame() :
#   looklike series but it give index to raws and columns.
#   it make frame from data to your table _-_   
#   EX.1 :       
"""
import pandas as pd
ls = [30,22,10,14,11,13,9,1,0,64,14,15,17,7]
print(ls,"\n")
frame = pd.DataFrame(ls)
print(frame)
"""
#   EX.2 :       
"""
import pandas as pd
ls = [30,22,10,14,11,13,16]
print(ls,"\n")
frame = pd.DataFrame(ls,index = ['a','b','c','d','e','f','g'],columns=["First"])
print(frame)
"""
#   EX.3 :       
"""
import pandas as pd
ls = [30,22,10,14,11,13,16]
print(ls,"\n")
frame = pd.DataFrame(ls,index = ['a','b','c','d','e','f','g'],columns=["First"])
print(frame,"\n","\n","\n")
print(frame.index,"\n","\n")
print(frame.values,"\n","\n")
print(frame.columns,"\n","\n")
print(frame.describe(),"\n","\n","\n")
print(frame.mean(),"\n")
print(frame.std(),"\n")
print(frame.max(),"\n")
print(frame.sum(),"\n","\n","\n")
print(frame.agg(["min","std","mean"]),"\n")
"""

# Fifth - Continue to ---> DataFrame() :   
#   EX.1 :       
"""
import pandas as pd
ls1 = [30,22,10,14]
ls2 = [36,18,9,45]
ls3 = [49,32,7,11]
ls4 = [10,33,45,0]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["First","Second","Third","Fourth"])
print(frame)
"""
#   EX.2 : 
"""      
import pandas as pd
ls1 = ["Osama",22,9000,9000000]
ls2 = ["Ali",18,900,4500]
ls3 = ["Yaser",32,7000,110000]
ls4 = ["Shadi",33,4500,60000]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account"],index = ['1','2','3','4'])
print(frame)
"""
#   EX.3 : 

"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,4500,"single"]
ls3 = ["Yaser",32,7000,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
print(frame)
print(frame.describe())
print(frame["Marital Status"]) # Note ---> If you want print specific column
print(frame["Marital Status"].describe()) 
print(frame["Name"].describe()) 
print(frame["Age"].describe()) 
"""

# Sixth - Continue to ---> DataFrame() : 
#   dtypes ---> used to know data types.     
#   EX.1 : 
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,4500,"single"]
ls3 = ["Yaser",32,7000,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
DataType = frame.dtypes
print(frame,"\n","\n")
print(DataType)
"""
#   EX.2 : 
#   select_dtypes(include=[]) ---> used to select specific (data types columns) to print this columns.     
"""
import pandas as pd
ls1 = ["Osama",22,9000.500,9000000,"single"]
ls2 = ["Ali",18,900.250,4500,"single"]
ls3 = ["Yaser",32,7000.750,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
DataTypeSelect1 = frame.select_dtypes(include=["object"])   # Note ---> object = string
DataTypeSelect2 = frame.select_dtypes(include=["int"])
DataTypeSelect3 = frame.select_dtypes(include=["double"])
print(frame,"\n","\n")
print(DataTypeSelect1,"\n")
print(DataTypeSelect2,"\n")
print(DataTypeSelect3,"\n")
"""
#   EX.3 : 
#   select_dtypes(exclude=[]) ---> used to select all (data types columns) to print exclude specific columns.     
"""
import pandas as pd
ls1 = ["Osama",22,9000.500,9000000,"single"]
ls2 = ["Ali",18,900.250,4500,"single"]
ls3 = ["Yaser",32,7000.750,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
DataTypeSelect = frame.select_dtypes(exclude=["object"])   # Note ---> object = string
print(frame,"\n","\n")
print(DataTypeSelect,"\n")
"""


# Seventh -concat() : 
#    Continue to ---> DataFrame()
#    concat() ---> used to make concatunation between two Frame.     
#    EX.1 :
"""    
import pandas as pd
data1 = [["Adel",20],["Fadi",30],["Hassan",35],["Mando",25]]
data2 = ["stud","Doc","Mr","Prog"]
DataFrame1 = pd.DataFrame(data1,columns=["Name","Age"])
DataFrame2 = pd.DataFrame(data2,columns=["Job"])
print(DataFrame1,"\n")
print(DataFrame2,"\n")
con = pd.concat([DataFrame1,DataFrame2],axis=1)
print(con,"\n")
"""

# Eighth---> loc[] : 
#   location function used to cutting specific Rows or Columns
#   EX.1 :
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,4500,"single"]
ls3 = ["Yaser",32,7000,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
print(frame,"\n","\n")
print(frame.loc["2":"3","Age":"Account"])      #Note ---> cuting from Row (// : //) , Column (// : //).
"""
#   EX.2 :
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,4500,"single"]
ls3 = ["Yaser",32,7000,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
print(frame,"\n","\n")
print(frame.loc["2":   ,   :"Account"])      #Note ---> cuting from Row (// : //) , Column (// : //).
"""

#  Ninth ---> iloc[] : 
#   looklike (loc[] function) but  it dealing with (index) instead of dealing with (Name Of Variable) 
#   EX.1 :
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,4500,"single"]
ls3 = ["Yaser",32,7000,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
print(frame,"\n","\n")
print(frame.iloc[2: ,0:2])      #Note ---> cuting from Row (// : //) , Column (// : //).
"""


#  Tenth ---> drop([]) :
#   used to delet specific Rows or Columns
#   EX.1 :       
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,4500,"single"]
ls3 = ["Yaser",32,7000,110000,"single"]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
AfterDrop1 = frame.drop(["1","3"],axis=0)  #Note (axis=0) ---> cuting from Row.
AfterDrop2 = frame.drop(["Age","Account"],axis=1) #Note (axis=1) ---> cuting from Column.
print(frame,"\n","\n")
print(AfterDrop1,"\n")
print(AfterDrop2,"\n")
"""

#  Eleventh ---> dropna() :
#   used to delet any (rows) that contain "None".
#   EX.1 :       
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,None,"single"]
ls3 = ["Yaser",32,7000,110000,None]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
DeleteNone = frame.dropna()
print(frame,"\n","\n")
print(DeleteNone)
"""


#   EX.2 :       
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,None,"single"]
ls3 = ["Yaser",32,7000,110000,None]
ls4 = ["Shadi",33,4500,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
print(frame,"\n","\n")
frame.fillna("NO NO NO",inplace=True)
print(frame,"\n","\n")
"""
#   EX.3 :       
"""
import pandas as pd
ls1 = ["Osama",22,9000,9000000,"single"]
ls2 = ["Ali",18,900,None,"single"]
ls3 = ["Yaser",32,7000,110000,None]
ls4 = ["Shadi",33,None,60000,"married"]
frame = pd.DataFrame([ls1,ls2,ls3,ls4],columns=["Name","Age","Income","Account","Marital Status"],index = ['1','2','3','4'])
print(frame,"\n","\n")
frame["Account"].fillna(0,inplace=True)
frame["Marital Status"].fillna("unknown",inplace=True)
print(frame,"\n","\n")
"""

# Thirteenth ---> insert(#index,#col name,#value) :
#   used to insert column.
#   EX.1 :       
"""
import pandas as pd
data1 = [["Adel",20],["Fadi",30],["Hassan",35],["Mando",25]]
data2 = ["stud","Doc","Mr","Prog"]
DataFrame1 = pd.DataFrame(data1,columns=["Name","Age"])
DataFrame2 = pd.DataFrame(data2,columns=["Job"])
print(DataFrame1,"\n")
print(DataFrame2,"\n")
con = pd.concat([DataFrame1,DataFrame2],axis=1)
# con.insert(0, "Salary", 10500)
con.insert(0, "Salary",  [None,30000,2500,30000])
print(con,"\n")
"""

# Fourteenth ---> merg():
#   used to merge two Frame but the two frame must have common coulumn.
#   Note ---> not duplicated any column.
#   EX.1 :       
"""
import pandas as pd
data1 = [["Adel",20],["Fadi",30],["Hassan",22],["Mando",25]]
data2 = [["Fadi","stud"],["Adel","Doc"],["Mando","Mr"],["Hassan","Prog"]]
DataFrame1 = pd.DataFrame(data1,columns=["Name","Age"])
DataFrame2 = pd.DataFrame(data2,columns=["Name","Job"])
print(DataFrame1,"\n")
print(DataFrame2,"\n","\n")
conc = pd.concat([DataFrame1,DataFrame2],axis=1)
print(conc,"\n","\n")
merg = pd.merge(DataFrame1, DataFrame2)
print(merg,"\n","\n")
"""
#  EX.2 :
"""
import pandas as pd
data1 = [["ahamed","Eng"],["hassan","HR"],["bassant","Doc"],["Ali","Doc"],["karem","Doc"],["Talat","Prog"],["Osama","Prog"],["Khaled","Eng"]]
data2 = [["Sara","Eng"],["Abdo","Doc"],["Ayman","Prog"],[None,"HR"]]
DataFrame1 = pd.DataFrame(data1,columns=["Name","job"])
DataFrame2 = pd.DataFrame(data2,columns=["Manger","job"])
merg = pd.merge(DataFrame1, DataFrame2)
print(merg)
"""

# Fifteenth ---> groupby() :
#    looklike describe function.
#    it give me information about specific column.
#    EX.1 :
"""
import pandas as pd
data1 = [[30,"ahamed","Eng"],[35,"hassan","HR"],[40,"bassant","Doc"],[30,"Ali","Doc"],[30,"karem","Doc"],[30,"Talat","Prog"],[45,"karem","Doc"],[25,"Osama","Prog"],[27,"Khaled","Eng"]]
DataFrame1 = pd.DataFrame(data1,columns=["Age","Name","Job"])
GroupCount = DataFrame1.groupby("Job").count()
GroupSum = DataFrame1.groupby("Job").sum()
GroupMean = DataFrame1.groupby("Job").mean()
print(DataFrame1,"\n")
print(GroupCount,"\n")
print(GroupSum,"\n")
print(GroupMean,"\n")
"""

# Sixteenth ---> read() :
#   used to read data file (exel) from outside the program
#   EX.1 :
"""
import pandas as pd
data = pd.read_excel("Data.xlsx")
print(data)
"""
#   EX.2 :
"""
import pandas as pd
#data = pd.read_excel("Data.xlsx",header=None,names=["A","B","C","D","E","F"])
data = pd.read_excel("Data.xlsx",header=0)
data.insert(0,"Score",[7.5,8,9.75,6,9])
print(data)
"""
#   EX.3 :
"""
import pandas as pd
#data = pd.read_excel("Data.xlsx",header=None,names=["A","B","C","D","E","F"])
data = pd.read_excel("Data.xlsx",header=0)
data.insert(0,"Score",[7.5,8,9.75,6,9])
print(data)
# Note ---> to save file after edit:
data.to_excel("DataNew_new.xlsx")
"""


























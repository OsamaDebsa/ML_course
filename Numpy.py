#                  ********** NUMPY **********
# first ---> array() :
#   convert from list to (Matrix or array).
#   EX.1 - list one dimensional :       
""" 
import numpy as np
ls = [1,2,3,4]
array = np.array(ls) 
print(ls)
print(array)
"""
#   EX.2 - list two dimensional :
"""
import numpy as np
ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
array = np.array(ls)   # ---> array()
print(ls)
print(array)
"""


# second ---> arange() :
#   print the range of numbers you determined.
#   EX.1 - print numbers from 1 to 15 :
"""
import numpy as np
arange = np.arange(1,16)
print(arange)
"""
#   EX.2 - print numbers from 0 to 16 and (jump or step) by 2 :
"""
import numpy as np
arange = np.arange(0,17,2)
print(arange)
"""


# third ---> zeros() :
#   print (Matrix or array) of zero.
#   EX.1:
"""
import numpy as np
z = np.zeros(4)
print(z)
"""
#   EX.2:
"""
import numpy as np
z = np.zeros((3,4))   # --->   Rowx & columns
print(z)
"""


# forth ---> random.rand() :
#   print Random decimal numbers as (Matrix or array) .
#   EX.1:
"""
import numpy as np
RandomDecimal = np.random.rand(3)
print(RandomDecimal)
"""
#   EX.2:
"""
import numpy as np
RandomDecimal = np.random.rand(3,4)  # --->   Rowx & columns
print(RandomDecimal)
"""


# fifth ---> random.randint():
#   print Random intger positive numper in range you determined  as (Matrix or array) if you want it.
#   EX.1:
"""
import numpy as np
PositiveRandomIntegerNumber = np.random.randint(100)
print(PositiveRandomIntegerNumber)
"""
#   EX.2:
"""
import numpy as np
PositiveRandomIntegerNumber = np.random.randint(170,261) # ---> lower & Uper 
print(PositiveRandomIntegerNumber)
"""
#   EX.3:
"""
import numpy as np
PositiveRandomIntegerNumber = np.random.randint(10,61,6) # ---> lower & Uper & number of digits
print(PositiveRandomIntegerNumber)
"""
#   Ex.4:
"""
import numpy as np
PositiveRandomIntegerNumber = np.random.randint(1,151,(3,3)) # ---> lower & Uper & Matrix dimensions
print(PositiveRandomIntegerNumber)
""" 
 

# sixth ---> random.shuffle():
#   mixed the arranged number to make it (shuffle or confused).
#   EX.1:
"""
import numpy as np 
arange = np.arange(1,16)
print(arange,"\n")
np.random.shuffle(arange)  # Note ---> we Don't make new variable with shuffle.
print(arange)
"""


#  EX.2:
"""
import numpy as np 
num = np.arange(1,16)
reshape = num.reshape(3,5)  # ---> we can make reshape (3,5) or (5,3) or (1,15) or (15,1)
print(reshape,"\n")
np.random.shuffle(reshape)
print(reshape)
"""

# seventh ---> reshape():
#   make Resahpe to numbers to make it (Matrix or array).
#   EX.1 :
"""
import numpy as np 
NoShape = np.random.randint(10,61,6)
shape = NoShape.reshape(2,3) # ---> we can make reshape (2,3) or (3,2) or (6,1) or (1,6)
print(shape)
"""


# eighth ---> some information about matrix:
#   min & max & IndexOfMax & IndexOfMin & Matrix dimensions & Number of Rows & Number of columns
#   Ex.1:
"""
import numpy as np
nums = np.random.randint(1,51,(3,4))# ---> lower & Uper & Matrix dimensions
MaxNum = nums.max()
MinNum = nums.min()
IndexOfMax = nums.argmax()
IndexOfMin = nums.argmin()
MatrixDimensions = nums.shape   # Note ---> shape : without "()".
MatrixRows = nums.shape[0]
MatrixColumns = nums.shape[1]
print(nums,"\n")
print("max :",str(MaxNum) )
print("min : ",str(MinNum) )
print("Index Of Max : ",str(IndexOfMax) )
print("Index Of Min : ",str(IndexOfMin) )
print("Matrix dimensions : ",str(MatrixDimensions) )
print("Number of Rows : ",str(MatrixRows) )
print("Number of columns : ",str(MatrixColumns) )
"""


# ninth ---> ceil() & floor() & round():
# EX.1:
"""
import numpy as np
x = np.ceil(2.3)
y = np.ceil(2.6)
z = np.ceil(2.5)
print(x , " ", y," " ,z)
a = np.floor(2.3)
b = np.floor(2.6)
c = np.floor(2.5)
print(a , " ", b," " ,c)
k = np.round(2.3)
l = np.round(2.6)
m = np.round(2.5)
print(k , " ", l," " ,m)
"""


# tenth ---> add():
# EX.1:
"""
import numpy as np
x = np.add(2,3)
print(x)

ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
array = np.array(ls)
print(array)

y = np.add(array,2)
print(y)

SumTwoMatrix = np.add(array,y)  # Note ---> the two matrix must the same size to add.
print(SumTwoMatrix)
"""


# eleventh ---> multiply():
# EX.1:
"""
import numpy as np
x = np.multiply(2,3)
print(x)

ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
array = np.array(ls)
print(array)

y = np.multiply(array,2)
print(y)

SumTwoMatrix = np.multiply(array,y)  # Note ---> the two matrix must have the rules of multiply.
print(SumTwoMatrix)
"""


# twelfth ---> divide():
# EX.1:
"""
import numpy as np
x = np.divide(2,3)
print(x)

ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
array = np.array(ls)
print(array)

y = np.divide(array,2)
print(y)

SumTwoMatrix = np.divide(array,y)
print(SumTwoMatrix)
"""













































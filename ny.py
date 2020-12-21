import numpy as np
# Creating array
a = np.array([2,3.2,4])
print("Creating an array")
print(a)
print("-------------------")
print("finding the type(float,int,char) of array ")
print(a.dtype.name)
print("-------------------")
print("finding the dimension of of array ")
print(a.ndim)
print("-------------------")
print("finding the shape(no of col, no of row) of of array ")
print(a.shape)
print("-------------------")
print("finding the type of element of of array ")
print(type(a))
print("-------------------")
# Multidimention array
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print("finding the type(float,int,char) of array ")
print(b.dtype.name)
print("-------------------")
print("finding the dimension of of array ")
print(b.ndim)
print("-------------------")
print("finding the shape(no of col, no of row) of of array ")
print(b.shape)
print("-------------------")
print("finding the type of element of of array ")
print(type(b))
print("-------------------")

# Complex term in array
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print("-------------------")
print("finding the type(float,int,char) of array ")
print(c.dtype.name)
print("-------------------")
print("finding the dimension of of array ")
print(c.ndim)
print("-------------------")
print("finding the shape(no of col, no of row) of of array ")
print(c.shape)
print("-------------------")
print("finding the type of element of of array ")
print(type(c))
print("-------------------")
#Creating Zeros & Ones array
d = np.zeros((3,4))
print("Zeros matrix of 3X4 ")
print(d)
print("-------------------")
d = np.ones((2,3,4),dtype=np.int16)
print("Zeros matrix of 3X4 ")
print(d)
print("-------------------")
print(np.empty((2,3)))
print("-------------------")

#arange function to create sequence of no analogues to range
e = np.arange(10,30,5) #10 15 20 25 30
print("arange for creating seqeunce of  no")
print(e)
e = np.arange(0,2,0.3) #10 15 20 25 30
print("-------------------")
print("arange for creating seqeunce of  no decimals")
print(e)
#When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function linspace that receives as an argument the number of elements that we want, instead of the step:
from numpy import pi
linespace_= np.linspace(0,2,9)
print("-------------------")
print("Printing 9 no from 0 to 9")
print(linespace_)
linespace_= np.linspace(0,2*pi,100)
sin = np.sin(linespace_)
print("-------------------")
print("Print 100 values of sin from 0 to 2pi")
print(sin)

# Creating array of of various size or dim using arange & reshape
a = np.arange(6)
print("-------------------")
print("One Dimension array")
print(a)
a = np.arange(12).reshape(4,3)
print("-------------------")
print("two Dimension array")
print(a)
a = np.arange(24).reshape(4,2,3)
print("-------------------")
print("Three 3D/ Dimension array")
print(a)
a = np.arange(10000).reshape(100,100)
print("-------------------")
print("100 X100 array")
print(a)

# Basic Operation of Array using Arithmatic operators
a = np.array([20,30,40,50])
print("-------------------")
print("Array a")
print(a)
b = np.arange(4)
print("-------------------")
print("Array b")
print(b)
c = a-b
print("-------------------")
print("Subtraction of array a -b")
print(c)
c = c**2
print("-------------------")
print("Squaring Each element of c")
print(c)
c = 10*np.sin(c)
print("-------------------")
print("Squaring Each element of c")
print(c)
c = a<35
print("-------------------")
print("Comparing of with 35")
print(c)

# Multi plication operation in array
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
print("-------------------")
print(A)
print(B)

print("Element wise product")
print("-------------------")
c = A*B
print(c)
print("matrix product")
print("-------------------")
c = A@B
print(c)
print(" Another matrix product")
print("-------------------")
c= A.dot(B)
print(c)
# Indexing, Slicing and Iterating¶
a = np.arange(10)**3
print("-------------------")
print("A")
print(a)

print("-------------------")
print("A[2]")
print(a[2])
print("-------------------")
print("A[2:5]")
print(a[2:5])
print("-------------------")
print("A[::-1] reverse of array")
print(a[::-1])
for i in a:
    print(i**(1/3))

def f(x,y):
    return 10*x + y
b = np.fromfunction(f,(5,4),dtype=int)
print(b)

for row in b:
    print(row)

for element in b.flat:
    print(element)

#shape manipulation
a = np.array([[2,41,8],[3,4,5]])
print(a)
print(a.shape)
#flating the a
print(a.ravel())
#reshaping 6,2
print(a.reshape(3,2))
#tranpose
print(a.T)
print(a.T.shape)
print(a.shape)
print(a.resize(6,1))

d = a.copy()
d = a
print(d is a)
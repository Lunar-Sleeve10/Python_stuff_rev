import numpy as np


#Create a 1D NumPy array of numbers from 1 to 20.
'''a = np.arange(1,21)
print(a)'''


#Create a 3×3 array filled with zeros, ones, and random numbers.
'''
b = np.zeros((1,3))
print(b)

c = np.ones((1,3))
print(c)

array_float = np.random.random((1,3))
print(array_float)

d = np.concatenate([b,c,array_float],axis =0)
print(d)


new_d = np.reshape(d,(3,3))
print(new_d)'''

#Find the shape, size, dtype, ndim of an array.
'''
a = (np.arange(1,11).reshape(2,5))
print(a)
print(np.shape(a))
print(a.dtype)
print(np.size(a))
print(np.ndim(a))'''

#Convert a Python list [1,2,3] into a NumPy array and multiply it by 5.
'''lst = [1,2,3]
a = np.array(lst) *5
print(a)'''

#Create a 4×4 identity matrix.
'''
ar_dia = np.eye(4) 
print(ar_dia)'''
#Create an array of 10 values equally spaced between 0 and 1.

#Create an array of 10 values equally spaced between 0 and 1.
'''a = np.linspace(0,1,10)
print(a)'''

#Create an array of 25 random integers between 1–100.
'''
a = np.random.randint(1,101,25)
print(a)'''

#Reshape a 1D array of 12 elements into 3×4.
'''a = np.arange(1,13)
print(a)
print(np.reshape(a,(3,4)))'''


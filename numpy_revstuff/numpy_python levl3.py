import numpy as np
#Add a 1D array [1,2,3] to every row of a 3×3 matrix.
'''n = np.arange(1,10).reshape(3,3)
a = np.array([1,2,3])

print(np.add(n,a))'''

#Multiply every column of a matrix by [1,2,3].
'''n = np.arange(1,10).reshape(3,3)
a = np.array([1,2,3])

b = n*a[:,None]
print(b)'''
####or
'''b = n*a.reshape(3,1)'''


#Given two arrays, compute element-wise maximum without loops.
'''a = np.array([1, 5, 3])
b = np.array([2, 4, 6])

result = np.maximum(a, b)
print(result)

'''
#Normalize an array (subtract mean, divide by std) using vectorized ops.
'''
x = np.array([[1,2,3,4,5,332],[33,3,22,3,43,3]])
#####mean
print(x.mean())
#######standard deviation
print(x.std())
######normalisation
print((x-x.mean())/x.std())'''


####Stack two arrays vertically and horizontally.

'''a = np.array([[1,2,3,4,5],[5,4,3,2,1]])
b = np.array([[1,2,3,4,5],[5,4,3,2,1]])
c = np.hstack((a,b))
print(c)
print(np.vstack((a,b)))'''


####Split a 1D array of length 12 into 3 equal parts.
'''a = np.arange(12)
b = np.split(a,3)
print(b)'''


#Flatten a 3×3 matrix to 1D and then reshape back.
'''a = np.arange(1,10).reshape(3,3)
print(a)
b = a.flatten()
print(b)
c= b.reshape(3,3)
print(c)
####or
c = a.reshape(-1)
print(c)
###or
d = a.ravel()
print(d)
'''

#####Convert a 3×4 matrix to a 2×6 matrix.
'''a = np.arange(1,13).reshape(3,4)
print(a)
a = a.reshape(2,6)
print(a)'''

#Find mean, median, std of an array.
'''a= np.array([[1,2,4,2,3,2,3,5,3],[7,5,5,5,4,4,3,2,2]])
print(a.mean())
print(a.std())

print(np.median(a))'''
#Compute row-wise and column-wise sums of a 2D array.

'''a= np.array([[1,2,4,2,3,2,3,5,3],[7,5,5,5,4,4,3,2,2]])
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
'''

#Find the index of maximum and minimum elements.

'''a = np.array([1,2,4,5,4,4,3,3,333,3,4,545553,4444])
print(a.min(),a.argmin())
print(a.max(),a.argmax())'''

#Given a 2D array, find the row with the highest sum.

'''a= np.array([[1,2,4,2,3,2,3,5,3],[7,5,5,5,4,4,3,2,2]])
b = np.sum(a,axis = 1)
c = np.argmax(b)
print(b,c)
'''

###Generate a 1000-sample normal distribution, compute its mean & std.
'''a = np.random.normal(loc = 0,scale = 1, size =1000)
print(np.mean(a))
print(np.std(a))
'''

#Generate a 5×5 matrix with random values and replace all values < 0.2 with 0.

'''a = np.linspace(0,2,25).reshape(5,5)
print(a)
a[a<0.2] = 0
print(a)'''


######### to generate sample woth normal distribution
'''a = np.random.normal(loc=0, scale=1, size=1000)
print(a.mean())
print(a.std())'''

###Compute dot product of two vectors using NumPy.

'''a = np.array([1,2,3,2])
b = np.array([5,4,3,2])
print(np.dot(a,b))'''

###Perform matrix multiplication of two 3×3 matrices.

'''a = np.arange(1,10).reshape(3,3)
b = np.linspace(0,2,9).reshape(3,3)

c = np.matmul(a,b).astype(np.int32)
print(c)
'''
###to find determinant

'''a = np.arange(1,10).reshape(3,3)
print(np.linalg.det(a))'''


### to find inverse
'''a = np.array([
    [[1, 2], [3, 4]],
    [[2, 0], [0, 2]],
    [[1, 1], [1, 2]]
])

print(np.linalg.inv(a))
'''
###Solve a system of linear equations using np.linalg.solve.
'''a = np.array([[1,1],[2,3]])
b = np.array([[10],[27]])
print(np.linalg.solve(a,b))'''



#Compute eigenvalues of a matrix.
'''a = np.array([[1,2,4],[4,32,4],[443,23,2]])
print(f"eigen values and eigen vectors are {np.linalg.eig(a)}")
'''
###just eigen values
'''a = np.array([[1,2,4],[4,32,4],[443,23,2]])
print(f"eigen values  are {np.linalg.eigvals(a)}")'''
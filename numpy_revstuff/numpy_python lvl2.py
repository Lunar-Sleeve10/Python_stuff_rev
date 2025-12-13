import numpy as np
'''
n = np.arange(1,51)
print(n[20:29])'''

###or boolean way
'''n= np.arange(1,51)
result = n[(n>20)&(n<30)]
print(result)

'''

#Replace elements > 50 in an array with 50.
'''n = np.array([10,20,30,40,33])
n[n<50] = 50
print(n)
'''
#Extract the 2nd column of a 4×4 matrix.

'''
n = np.eye(4,4)
print(n[1])
'''
#Extract the last row using negative indexing.
'''n = np.eye(4)
print(n[-1])'''


#Reverse every row of a 2D array.
'''n = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(n[:,::-1])
'''

#Given a 2D matrix, set the diagonal elements to 0.
'''n = np.arange(1,9).reshape(2,4)
np.fill_diagonal(n,0)
print(n)
'''


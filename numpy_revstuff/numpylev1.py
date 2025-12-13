'''import timeit
def f():
    [j**4 for j in range(1,9)]

t = timeit.Timer(f)
print(t.timeit(number=100000))
'''

####
'''import numpy as np
import timeit

def f():
    np.arange(1,9)**2

t = timeit.Timer(f)
print(t.timeit(number = 100000))
    '''

import numpy as np
'''a = np.array([1,2,3,4,5])
print(a)
'''
###########
'''l = []
for i in range(1,5):
    int_i = int(input("enter :"))
    l.append(int_i)

print(np.array(l))
print(np.array(l).ndim)
'''
 ##################
'''ar2 = np.array([[1,2,3,4],[1,2,3,4]])
print(ar2)
print(ar2.ndim)'''

###############
'''ar3 = np.array([[1,2,3,4],[12,2,3,2],[101,201,201,43]])
print(ar3)
print(ar3.ndim)'''

###########
'''
arn = np.array([1,2,3,4],ndmin = 10)
print(arn)
print(arn.ndim)'''


#####zero
'''ar_zero = np.zeros((3,4))
print(ar_zero)
'''
####Ones
'''ar_one = np.ones((3,4))
print(ar_one)'''

#####empty
'''ar_em =np.empty((3,4))
print(ar_em)
'''


#######range

'''ar_range = np.arange(1,9)**2
print(ar_range)
'''
#####2d
'''ar_range2 = (np.arange(1,9)**2).reshape(2,4)
print(ar_range2)
'''

#######diagonal
'''ar_dia = np.eye(4) ##square matrix stuff
print(ar_dia)'''
'''ar_dia = np.eye(2,3) #non square matrix
print(ar_dia)'''

######linespace
'''ar_lin = np.linspace(1,10, num = 5)
print(ar_lin)'''

######Rand()
'''var = np.random.rand(3,4)
print(var)'''
####randn()
'''var = np.random.randn(3,4)
print(var)'''
#####ranf()
'''var = np.random.ranf((3,4))
print(var)'''
#####randint()
'''var = np.random.randint(1,30,size = (3,4),dtype = int)
print(var)'''

########to know datatype
'''var = np.array(['1','2','3','4','5'])
print(var.dtype)'''

####to establish new datatype
'''var = np.array([1,2,3,4],dtype= 'U1')
print(var)'''

###OR
'''var = np.array([1,2,3,4,5])
var1 = np.float32(var)
print(var1)'''

###ARTHEMTIC OPERATION

'''var = (np.arange(1,9)**2).reshape(2,4)
#print(var)
var1 = np.arange(1,9).reshape(4,2)
a = np.divide(var,var1).astype(np.int32)
print(a)

a = np.dot(var,var1) + 3
print(a)'''

###mim and max stuff with arg for position and mores stuff
'''var = np.linspace((3,5),5)

print(np.min(var),np.argmin(var))'''
'''
var = np.array([1,2,3,22,4,2,0.1])
print(int(np.min(var)),int(np.argmin(var)))
print(int(np.max(var)),int(np.argmax(var)))

a = np.tan(var)
print(a)
b = np.sin(var)
c = np.cos(var)
d = np.divide(b,c)

print(np.allclose(a,d))

print(np.cumsum(d))

print(np.shape(b))
var = np.append(var,[5,3,2])
print(var)

b = np.reshape(var, (5,2))
print(b)'''


## broadcasting either equal or one of them has one
'''a = np.array([[1],[2]])
n = np.array([[1,2],[1,2]])

print(np.shape(a))
print(np.shape(n))
print(np.add(a,n))'''

#indexing
'''n = np.array([[[1,2,3],[2,2,3]],[[1,2,3],[2,3,5]]])
print(n[1,1,2])'''

#slicing 
'''n = np.array([[[1,2,3],[2,2,3]],[[1,2,3],[2,3,5]]])
print(n[1,0,::-1])'''


#iternation
'''n = np.array([1,2,3,2,2,2,2,3,3,2,2,32])
for i in range(np.size(n)):
    print(n[i] , end=" ")'''

'''n = np.array([[1,2,3,4,3],[2,3,4,3,2]])
#print(((n[0])))
for i in n:
         for j in i:
                 print(j, end = " ")'''



#####Boolean indexing
'''arr = np.array([10,20,30,40,50,40])
arr[arr>25] = 0
print(arr)'''


####Using where function and stuff
'''arr = np.array([1,2,3,4,3,2,1])
result = np.where(arr < 25 , 100 ,arr)
print(result)
'''

'''x = np.array([[1,2,3,4,5,332],[33,3,22,3,43,3]])
#####mean
print(x.mean())
#######standard deviation
print(x.std())
######normalisation
print((x-x.mean())/x.std())'''



########numpy split function
'''x = np.arange(12)
n = np.split(x,3)
print(n)
'''



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

print(np.linalg.inv(a))'''

#linear equations using np.linalg.solve.
'''a = np.array([[1,1],[2,3]])
b = np.array([[10],[27]])
print(np.linalg.solve(a,b))'''

###for eigen value or vectros
'''a = np.array([[1,2,4],[4,32,4],[443,23,2]])
print(f"eigen values and eigen vectors are {np.linalg.eig(a)}")
'''
###just eigen values
'''a = np.array([[1,2,4],[4,32,4],[443,23,2]])
print(f"eigen values  are {np.linalg.eigvals(a)}")'''
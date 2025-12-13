
#Lambda & Map: Use map and lambda to square every number in a list.
'''def square_list(s):
    squared = list(map(lambda x:x**2 , s))
    return s
'''
#Lambda & Filter: Use filter and lambda to extract only even numbers from a list.
'''def even_list(s):
    return s%2 ==0

def evenlist(a):
    b = filter(even_list,a)
    return list(b)

'''

#Matrix Creation: Create a 3x3 matrix using a list of lists.

'''

matrix = []
n = 3
for i in range(n):
    row =[]
    for j in range(n):
        k = int(input("enter number"))
        row.append(k)
    matrix.append(row)
print(matrix)

'''
#Matrix Element Access: Access the element in the 2nd row, 3rd column of your matrix.
'''element = matrix[1][2]  # 2nd row, 3rd column
print(element)'''


'''def matrix_addtion(a,b,n):
    matrix_adder = []
    for i in range (n):
        row =[]
        for j in range (n):
            row.append(a[i][j]+b[i][j])

        matrix_adder.append(row)
    return matrix_adder

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
  [5, 3, 4],
  [6, 7, 2],
  [1, 9, 8]
]
print(matrix_addtion(m1,m2,3))
'''

#Matrix Transpose: Write a function to swap rows and columns of a matrix.
'''def transpose_matrix(s,n):
    for i in range (n):
        for j in range (i+1,n):
            s[i][j], s[j][i] = s[j][i], s[i][j]

            
    return s
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose_matrix(m1,3))'''

#Calculate the dot product of two lists manually (sum of products of corresponding elements).

'''def dotproduct(s,b):
    if len(s) == len(b):
        return None
    
    result = 0
    for i in range(len(s)):
        result += s[i]*b[i]
    return result
'''

###or crazy stuff zip method

'''def dotproduct(s,b):
    return sum(x*y for x,y in zip(s,b))'''

#Recursion: Write a recursive function to calculate factorial.

'''
def fact_no(s):
    if s ==0 or s == 1:
        return 1
    else:
        return s *(fact_no(s-1))
    
    '''


#Safe Division: Write a function to divide two numbers that handles division by zero using try-except.
'''
def devison_stuff(s,b):
    try:
        result = s/b
        return result 
    except ZeroDivisionError:
        return "Error devison by zero not possible"
'''



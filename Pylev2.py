
#Sum of Range: Calculate the sum of all numbers from 1 to 100.

'''sum = 0
for i in range (1,101):
    sum = sum+i
print(sum)'''

#Multiples of 7: Print all numbers between 1 and 200 that are divisible by 7.
'''
for i in range (1,201):
    if i%7==0:
        print(i)

'''
#Factorial: Write a program to compute the factorial of a number
"""s = int(input("enter any number"))
p = 1
for i in range(1,s+1):
    p *= i 
print(p)
"""

#Reverse Integer: Reverse the digits of a number
'''s = int(input("enter the nuber to be reversed"))
reverse = 0
while s>0:
    digit = s%10
    reverse = (reverse*10)+digit
    s = s//10
print(reverse)

    '''
###OR###
'''s = int(input("enter the number"))
a = str(s)
print(a[::-1])'''

#Count Digits: Count how many digits are in a number (e.g., 500 has 3 digits).
"""s = int(input("enter the number"))
print(len(str(s)))
"""

#WGenerate the Fibonacci sequence up to the n-th term.

'''###Iterative Method (Recommended for Efficiency)
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence
a = int(input("enter the number"))
print(fibonacci_iterative(a)) 


 ###Recursive Method (Simple but Slow for Large Numbers)
def fibonacci_new(n):
    if n<= 1:
        return n
    else:
        return fibonacci_new(n-1) + fibonacci_new(n-2)
    
s = int(input("enter a number of terms"))
print("series")
for i in range(s):
    print(fibonacci_new(i), end = "")'''



#Write a script to check if a given input number is Prime.
'''n = int(input ("enter a number"))
a = True

if n<=1:
    print("lol")
else:
    for i in range(2,(n//2)+1):
        if n%i==0:
            a = False
            break    
if a:
    print("prime")  
else:
    print('not prime') '''



#Print all prime numbers between 1 to n

'''
def find_Prime(n):

    if n<=1:
        return False
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return False
                
    return True      

b = int(input('enter till what number' ))
c = []
for i in range(2,b+1):
    if find_Prime(i)== True:
     c.append(i)
    
print(c)

    '''

#Sum Even Numbers: Write a loop to sum all even numbers between two user-given values
'''n = int(input ("enter the start number"))
k = int(input("enter the end number"))
c=0
for i in range(n,k+1):
    if i%2==0:
        c=c+i
print(c)'''


#Multiplication Table: Print the multiplication table for a number $n$
'''n = int(input('enter the number for multiplication table'))
k = int(input('enter upto what number'))
for i in range (1,k+1):
    print(f"{n} x {i} = {n * i}")'''


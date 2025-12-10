#Basic Arithmetic: Take two numbers as input and print their sum, difference, product, and division.
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a+b
diffrence = a-b
product = a*b
quotient = a/b
print("Sum:", sum)
print("Difference:", diffrence)
print("Product:", product)
print("Quotient:", quotient)
"""


#Swap Variables: Swap the values of a = 5 and b = 10 without using a third variable.
'''
a =5
b=10
a,b =b,a
print("After swapping: a =", a, "b =", b)


'''

#Temperature Converter: Write a program to convert Celsius to Fahrenheit ($C * 9/5 + 32$).

''' 
a = float(input("Enter temperature in Celsius: "))
fahrenheit = (a * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)'''

#Even or Odd: Check if a number is even or odd.
'''

a = int(input("Enter a number: "))
if a%2==0:
    print(a, "is even")
else:
    print(a, "is odd")  
'''
#Largest of Three Numbers: Find the largest among three numbers.
'''
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter third number: "))
if a>=b and a>=c:
    print(a, "is the largest number")
elif b>=a and b>=c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")       
    '''


#Leap Year Check: Write a program to check if a year is a leap year (Divisible by 4, but not 100 unless also by 400).
'''a = int(input("enter year"))
if (a % 4 ==0 and a%100 != 0) or a %400 == 0:
    print("leap")
else:
    print("not leap year")

'''

#String Slicing: Given s = "DataScience", print the first 4 characters and the last 3 characters.

'''
s= "DataScience"
print(s[:4])
print(s[-3:])'''



#Type Conversion: Given a string price = "150", convert it to an integer and add 50 to it.

'''s = '150'
a = int(s)

print(a+50)'''

#Exponentiation: Calculate $5^4$ using Python operators.
'''print(5**4)'''


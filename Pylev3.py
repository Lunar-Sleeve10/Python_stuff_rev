#Palindrome Check: Check if a string is a palindrome (reads same forwards and backwards) using slicing
'''s = input("enter a string")
if s[0::] == s[::-1]:
    print("palindrom")
else:
    print("not palindrome")
'''
###without using slicing

'''def palindromecheck(s):
    left_pointer = 0
    right_pointer = len(s)-1
    while left_pointer < right_pointer:
        if s[left_pointer] != s[right_pointer]:
            return False 
        
        left_pointer +=1
        right_pointer -=1
    
    return True
    
n = input("enter")
print(palindromecheck(n))'''


#Vowel Remover: Write a function that removes all vowels from a given string.

'''
s = input("enter string")
a = ''
for i in s:
    if i not in ['a','e','i','o','u']:
        a = a+i
print(a)'''



#Word Counter: Count the number of words in a sentence.
"""s = input()
words = s.split()
print(words)
print(len(words))
"""

###OR###

"""
s = input()
count = 0
in_words = False
for ch in s:
    if ch!= " " and not in_words:
        count = count + 1
        in_words = True
    elif ch == " ":
        in_words = False
print(count)"""


#Count vowels, consonants, and digits in a string.
'''

s = input("eneter a string")
c = 0
v = 0
d = 0
vowels = 'aeiouAEIOU'
for ch in s:
    if ch.isdigit():
        d = d+1
    elif ch.isalpha():
        if ch in vowels:
            v+=1
        else:
            c = c+1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)'''

#Replace all spaces in a string with underscores (common in standardizing column names).
'''s = input('enter a string')
a = ''
for ch in s:
    if ch == ' ':
        a += '_'
    else:
        a += ch

print(a)'''

###OR##


'''s = input("enter a string")
a = s.split()
e = "_".join(a)
print(e)'''

###OR###

"""s = input("enter a string")
a = s.replace(" ", "_")
print(a)"""


#First Non-Repeating: Find the first character in a string that does not repeat.
"""s = input("enter a string")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1

for ch in s:
    if freq[ch]==1:
        print(ch)
        break
else:
        print('no non repeating first')
"""

#Anagram Check: Check if two strings are anagrams (contain same characters in different order).
"""a = input("enter string 1")
b = input("enter string 2")
if sorted(a) == sorted(b):
    print('anagram')
else:
    print('not anagram')"""

###OR###

"""a = input("enter string1 ")
b = input("enter string 2")
freq = {}

if len(a)!= len(b):
    print("not anagram")
else:
    for ch in a:
        freq[ch] = freq.get(ch,0) + 1
    for ch in b:
        if ch not in freq:
            print("not anagram")
            break
        freq[ch] -=1
        if freq[ch]<0:
            print("not anagram")
            break
    else:
        print('anagram')
"""
###OR###
'''
from collections import Counter
s = input('enter string1')
b = input("enter string2")
if Counter(s) == Counter(b):
    print("anagram")
else:
    print("not anagram")
'''


#Currency Cleaner: Given "$1,000.00", remove symbols to convert it to a float 1000.0.
'''s = input("enter the money")
a = ''
for ch in s:
    if ch.isdigit():
        a = a+ch
print(float(a))
'''
###OR###
'''s  = input("enter the money")
a = s.replace("$","").replace(";","")
print(float(a))'''

#Title Case: Convert a string to Title Case (first letter caps) without using .title().
'''
s = input("enter a string")
st_word = False
a = ""
for ch in s:
    if ch != " " and not st_word:
       a += ch.upper()
       st_word = True
    elif ch == ' ':
        a += ch
        st_word = False
    else:
        a += ch
print(a)

'''

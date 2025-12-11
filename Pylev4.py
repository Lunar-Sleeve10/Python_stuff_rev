#Find the maximum and minimum in a list without using max() or min()
'''def max_min_finderlist(a):
    if not a:
        return None , None
    
    max_v = a[0]
    min_v = a[0]
    for i in a :
        if i>max_v:
            max_v = i
        elif i<min_v:
            min_v = i
    return min_v , max_v

n = int(input("enter the number of elements"))
list1=[]
for b in range(n):
    object_name = int(input("enter the object"))
    list1.append(object_name)

print(f" min and max = {max_min_finderlist(list1)}")
    

'''
#Remove duplicates from a list using a Set.
'''def remove_duplicates(s):
    a = set(s)
    return list(a)
n = int(input("enter the number of elements"))
list1=[]
for b in range(n):
    object_name = int(input("enter the object"))
    list1.append(object_name)

print(f" new list is  = {remove_duplicates(list1)}")
  
 '''
###OR without using set
'''def remove_duplicates_preserve_order(s):
    result = []
    for x in s:
        if x not in result:
            result.append(x)
    return result
'''

#Find the intersection (common items) and union (all items) of two Sets.
'''
def intersection_union(s,b):
    intersection_set = set()
    for i in s:
        if i in b:
            intersection_set.add(i)
    set_union = s|b

    return intersection_set , set_union

a= {'2','3','4'}
c = {'2','5','4'}
print(f" intersection and union are  {intersection_union(a,c)}")
'''

### or union differentmethod
'''set_a = {1, 2, 3}
set_b = {3, 4, 5}

set_c = set_a.union(set_b)
print(set_c)'''


#Use a dictionary to count how often each element appears in a list.
'''def freq_counter_list(a):
    freq= {}
    for ch in a:
        freq[ch] = freq.get(ch,0) + 1
    return freq

list1 = [2,3,2,4,4,3,4,5,4,3,2,1,23,3,3,3,3,1,2]
print(f"frquencies are {freq_counter_list(list1)}")'''


#Second Largest: Find the second largest number in a list.
'''def second_larget(s):
    if len(s) <2:
        return None
    
    first = second = float('-inf')
    for num in s:
        if num > first:
            second = first
            first = num
        elif first>num>second:
            second = num
        return second'''

#Flatten List: Convert a nested list [[1,2], [3,4]] into a flat list [1,2,3,4]
'''
def flatten_list(s):
    new_list = []
    for ch in range(0 , len(s)):
        for i in range(len(s[ch])):
            new_list.append(s[ch][i])

    print(new_list)

b = [[1,2], [3,4]]

flatten_list(b)'''
    
####OR###
'''def flatten_list(s):
    new_list = []
    for sublist in s:
        for item in sublist:
            new_list.append(item)
    return new_list
'''

#Merge Dictionaries: Write a script to merge two dictionaries into one.

#Manual
'''def merged_dict(a,b):
    merged = {}
    for key in a:
        merged[key] = a[key]
    for key in b:
        merged[key] = b[key]
    return merged


'''
###or

'''def merged_dict(a,b):
    merged = a.copy()
    merged.update(b)

    return merged'''

###OR###
'''merged = (**d1,**d2)'''
###or###

'''merged = d1|d2'''


####List of Tuples to Dict: Convert [("a", 1), ("b", 2)] into {"a": 1, "b": 2}.
'''def kist_tupleconv(s):
    a = dict(s)
    return a
'''
###Manual
'''def list_tuple_conv(s):
    a = {}
    for key,value in s:
        a[key] = value
    return a
    
'''
#Sort by Key: Sort a list of dictionaries (e.g., employees) by a specific key (e.g., "salary").
'''def sorted_dict(a):
    sorted_stuff = sorted(a,key = lambda x: x["salary"])
    return sorted_stuff
'''

#List Comprehension: Create a list of squares of even numbers from 0-20 using a single line of code.
'''def square_list(a):
    new_list = [x**2 for x in a]
    return new_list
'''

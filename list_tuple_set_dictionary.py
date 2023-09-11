# -*- coding: utf-8 -*-
"""2.4. List Tuple Set Dictionary.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12joBMY18TBcDnfgG5cvwhipQqam3f9fR

Types of Objects in Python:
1. Immutable Objects
2. Mutable Objects

Immutable Objects:
1. int
2. float
3. string
4. bool
5. tuple

Mutable Objects:
1. List
2. Set
3. Dictionary

List
"""

# list should be included in the square brackets
my_list = [1,2,3,4,5]
print(my_list)
type(my_list)

# lists can have multiple data types
my_list = [2, 3, 1.8, 'English', True]
print(my_list)

"""Lists are Mutable --> Changeable"""

# add elements to a list
my_list = [2, 3, 1.8, 'English', True]
my_list.append(6)
print(my_list)

# print elements of a list using their index
print(my_list[0])
print(my_list[2])

# lists allow duplicate values
list_1 = [1,2,3,4,5,12,2,3]
print(list_1)

print(len(list_1))

# initiating an empty list
list_2 = []
print(list_2)

list_2.append(5)
print(list_2)

# delete an item in a list
list_2 = [2, 3, 1.8, 'English', True, 6]
print(list_2)

del list_2[2]
print(list_2)

# join two lists
list_3 = [1,2,3,4,5]
list_4 = [6,7,8,9,10]

list_5 = list_3 + list_4
print(list_5)

"""Tuple"""

tuple_1 = (2,3,4,5)
print(tuple_1)
type(tuple_1)

# tuple allows multiple data types
tuple_2 = (1,2,3.5, 'Machine Learning', False)
print(tuple_2)

# converting  a list to a tuple

my_list = [3,4,5,6]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[1])

"""Tuples are immutable --> Unchangeable"""

my_tuple.append(6)

print(len(my_tuple))

"""Set"""

# set --> Curly brackets
my_set = {1,2,3,4,5}
print(my_set)
type(my_set)

print(my_set[0])

# convert a list to a set
list_5 = [4,5,6,7,8]

x = set(list_5)
print(x)

# set does not allow duplicate values
set_3 = {1,2,3,4,5,1,2,3}
print(set_3)

"""Dictionary

Key-Value Pair
"""

my_dictionary = {'name':'David','age':30,'country':'India'}
print(my_dictionary)
type(my_dictionary)

print(my_dictionary['name'])
print(my_dictionary['age'])
print(my_dictionary['country'])

# dictionary does not allow duplicate values
dictionary_2 = {'name':'David','age':30,'country':'India','name':'David','age':30,'country':'India'}
print(dictionary_2)


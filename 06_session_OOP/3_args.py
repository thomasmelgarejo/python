# args
# args er en tuple, så den kan itereres
# * kaldes unpacking operators
def my_sum(*args ): 
    result = 0
    # Iterere args
    for x in args:
        result += x
    return result

#print(my_sum(4, 2, 3)) #9


# *args med andre parametre ->def my_function(a, b, **kwargs, *args):
def my_sum(para1, *args ): # args is a tuple
    result = 0
    # Iterere args
    for x in args:
        result += x
    return result*para1

#print(my_sum(4, 2, 3)) #20


# **kwargs
# som args men med named arguments, og bruge dict 
def my_kwargs_sum(**kwargs ): 
    result = 0
    # Iterere args
    for x in kwargs.values():
        result += x
    return result

#print(my_kwargs_sum(a=4, b=2, c=8)) #14


# **kwargs
# 
def my_kwargs_named(**kwargs ): 
    result = ""
    
    for x in kwargs:
        result += x
    return result

#print(my_kwargs_named(a=4, b=2, c=8)) #abc


# *unpacking operator 
def my_sum(a, b, c):
    print(a+b+c)

my_list = [1,2,3]
# my_sum(my_list) #[1,2,3] vil blive modtaget som et argument, derfor fejl
#my_sum(*my_list) #6


# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

*a, b, c = my_list

# print(a) #[1, 2, 3, 4]
# print(b) #5
# print(c) #6


# *unpacking operator brugt til at merge to lists
list1 = [1,2,3,4,5,6]
list2 = [11,22,33,44,55,66]
merge_list = [list1, list2]
#print(merge_list) #[[1, 2, 3, 4, 5, 6], [11, 22, 33, 44, 55, 66]]

merge_list = [*list1, *list2]
#print(merge_list) #[1, 2, 3, 4, 5, 6, 11, 22, 33, 44, 55, 66]


*a, = "RealPython"  # kommaet definere en tuple
#print(a) #['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']

a = "RealPython"
#print(a) #RealPython

a = [*"RealPython"]
#print(a) #['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
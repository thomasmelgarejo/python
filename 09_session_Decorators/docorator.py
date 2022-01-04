#By definition, a decorator is a function that takes another function and extends the behavior of the latter function 
# without explicitly modifying it.

#decorator
def decorator(func):
    def wrapper():
            print("Before")
            func() #execute function
            print("After")
    
    return wrapper

#function
def greet():
     print('Hello from function') 

#decorating happens here
greet = decorator(greet)

#greet() #Køre metode

#************************************************************************************************

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 17:
            func()
        else:
            print("ssssssssh!")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

#say_whee()

#************************************************************************************************

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")


#say_whee()

#*************************************************************************************************
#Genbrug af decorators fra module

from importdecor import do_twice

@do_twice
def say_whee():
    print(f"Hello")

#say_whee()

#**************************************************************************************************
#Decorator funktioner med arguments

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Before1")
        func(*args, **kwargs)
        print("After1")
    return wrapper

@decorator1
def say_name(name):
    print(f"My name is {name}")

#say_name("Peter")

#****************************************************************************************************
#Sætte den decorerede funktion op til en return værdi

def decorator2(func):
    def wrapper2(*args, **kwargs):
        print("Before1")
        func(*args, **kwargs)
        print("After1")
        return func(*args, **kwargs)
    return wrapper2

@decorator2
def say_name(name):
    print(f"My name is {name}")
    return name

#print(f"Return værdi:", say_name("Hans"))

#*****************************************************************************************************
#Sørge for at den decorerede funktion beholder korrekt dokumentation

#help(say_name) #wrapper2(*args, **kwargs)

import functools

def decorator3(func):
    @functools.wraps(func)
    def wrapper3(*args, **kwargs):
        print("Before1")
        func(*args, **kwargs)
        print("After1")
        return func(*args, **kwargs)
    return wrapper3

@decorator3
def say_name3(name):
    print(f"My name is {name}")
    return name

#help(say_name3) #say_name3(name)


#*************************************************************************************
#Real world eksempel, tager tid på en funktions eksekvering

import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(9999)
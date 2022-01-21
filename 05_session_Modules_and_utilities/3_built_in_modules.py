#built-in modules er programmeret i C
#https://www.tutorialsteacher.com/python/collections-module

#6 grupper modules
#OS
#Sys 
#Math
#Statistics
#Collection
#Random

#BRUG AF BUILT-IN MODULES

#operating system****************************************
import os

#Fang gældende diretory
print('What the dir here? ', os.getcwd())

#--Ændre til directory
#os.chdir(C:\proram\aa)

#sys module************************************************
import sys

#sys.exit      #--> exit tilbage til console
print('Largest int a variable can take: ',sys.maxsize)
# print('python modules locations: ' , sys.path)

#math******************************************************
import math

print('pi: ', math.pi)
print('Fra grader til radianer', math.radians(180))
print('3^2: ', int(math.pow(3,2)))     #-> returnere float


#collections************************************************
import collections   
Student = collections.namedtuple('Student', ['name', 'age', 'grade'])

s1 = Student("Imran", 21, 98)
print('studente: ', s1[0])
print('studente: ', s1.name)

#random*******************************************************
import random

print('random() 0-1: ',random.random())
print('random 1-100: ', random.randint(1, 100))
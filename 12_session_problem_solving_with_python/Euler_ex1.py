#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
from taketime import timer

#Min løsning-1; dårlig løsning, første forløkke får metoden til at køre dobbel antal iterationer, resultat er ikke præcist (overlap)
@timer
def find_multiples(limit, *num):
    multiples = []  
    
    for argsNumber in num:
        for i in range(1,limit):
            if argsNumber * i < limit:
                multiples.append(argsNumber*i)

    #print(multiples)
    return sum(multiples) 

find_multiples(10000000,3,5)


#Claus løsning
@timer
def calculate(n):
    c = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            c += i
    return c

calculate(100_000_00)


#Claus anden løsning
@timer
def calculate_comp(n):
    return sum([i for i in range(1,n) if i % 3 == 0 or i % 5 == 0])

calculate_comp(100_000_00)


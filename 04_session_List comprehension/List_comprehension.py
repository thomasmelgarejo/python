#List comprehension er et slags for-loop over en collection
#Syntaks er mere komprimeret

squares = [x*x for x in range(1, 3)] #sidste tal ikke includeret 1 og 2 ganget med sig selv

squares1 = [x*x for x in range(10)] #0-9 ganget med sig selv

even_squares = [x*x for x in range(10) if x>5 and x<8]

print(even_squares)

#List comprehension SYNTAKS
#values = [expression
#          for item in collection
#          if condition]

#For-loop SYNTAKS
#values = []
#for item in collection:
#    if condition:
#        values.append(expression)

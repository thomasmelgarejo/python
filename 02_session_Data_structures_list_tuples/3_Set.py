# Sets are unordered.
# Set elements are unique.
# A set itself may be modified, but the elements contained in the set must be of an immutable type.

#Creating set 2 ways
#First way:
set1 = set([1,2,3,4,5])
print('Set1', set1)

#Second way:
set2 = {'a', 'b', 'c', 2, 1}

# set3 = {[1,2]}  #mutable-NOT working
# set4 = {(1,2)}  #imutable-working

#Working on set by methods or Operator
    #Union
set3 = set1 | set2
print('set3: ' , set3)  #operator (only sets)

set4 = set1.union(set2)
print('set4: ' , set4)  #method

    #intersection
set5 = set1.intersection(set2)
print('set5', set5)

    #difference
set6 = set1.difference(set2) 
print('set6', set6) #set6 {3, 4, 5}

set7 = set2.difference(set1) 
print('set7', set7) #set7 {'b', 'c', 'a'}

set8 = set2-set1
print('set8', set8) #set8 {'b', 'a', 'c'}

#isdisjoint
#issubset
#issuperset

#check if value is in set
print(7 in set1) #False

print('***************************************************************************')
#modifying Sets

    #add
set1.add(6)
print(set1)

    #remove
set1.remove(6)
print(set1)

#discard
#pop
#clear
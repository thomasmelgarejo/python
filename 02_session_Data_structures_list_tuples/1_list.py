def funki():
    print("tekst print fra funktion, embedded i list ")

#list karakteristika
#-are defined by []
#-are ordered.
#-can contain any arbitrary objects.
#-elements can be accessed by index.
#-can be nested to arbitrary depth.
#-are mutable.
#-Lists are dynamic.


lis =[]
lis1 = [1,2,3,4,5,6]#atomic type
lis2 = [1 ,True, ['Hejsa', 'Farvel'], 'Hej', ('tuple', 'tub'), 2.12, funki]


print(lis) #[]
print(lis1) #[1,2,3,4,5,6]
print(lis1[2]) #3
print(lis2[2][0]) #Hejsa
print(lis2[4][1]) #tub
lis2[6]() #function
lis2[-1]() #function
print(lis2[-4:]) #['Hej', ('tuple', 'tub'), 2.12, <function funki at 0x000001CF24EFF040>]

print(lis2[1:5:2])
#forklaring: a[start:stop:step] er det samme som a[slice(start, stop, step)]

#HJÆLPE FUNKTIONER


    #DELETE
# del lis1[0]
# print(lis1)

# lis1[0] =1
# print(lis1)


    #APPEND(<obj>)
lis1.append('ff') 
print(lis1)


    #EXTEND(<iterable>)
lis1.extend([1,2,3]) #er stadig den samme list
print([lis1])

lis1 += ['ee']
print(lis1)


    #REMOVE(<obj>)
lis1.remove('ee')
print(lis1)

    #POP(index=-1)
lis1.pop()   #pop(1)
print(lis1)
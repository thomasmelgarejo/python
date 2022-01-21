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


list =[]
list1 = [1,2,3,4,5,6]#atomic type
list2 = [1 ,True, ['Hejsa', 'Farvel'], 'Hej', ('tuple', 'tub'), 2.12, funki]
list1[2]=44

print(list) #[]
print(list1) #[1,2,3,4,5,6]
print(list1[2]) #3
print(list2[2][0]) #Hejsa
print(list2[4][1]) #tub
list2[6]() #function
list2[-1]() #function
print(list2[-4:]) #['Hej', ('tuple', 'tub'), 2.12, <function funki at 0x000001CF24EFF040>]

print(list2[1:5:2])
#forklaring: a[start:stop:step] er det samme som a[slice(start, stop, step)]

#HJÆLPE FUNKTIONER


    #DELETE
del list1[0]
print('del', list1)

list1[0] =1
print(list1)


    #APPEND(<obj>)
list1.append('ff') 
print(list1)


    #EXTEND(<iterable>)
list1.extend([1,2,3]) #er stadig den samme list
print('extend', list1)

list1 += ['ee']
print(list1)


    #REMOVE(<obj>)
list1.remove('ee')
print(list1, '-->remove()')

    #POP(index=-1)
list1.pop()   #pop(1)
print(list1 , '--> list1 efter pop()')
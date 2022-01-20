#tuple karakteristika
#Defined with ()
#-imutable

tuple1 = ('1', '2', '3', '4', '5', '6')
tuple2 = ('a', 'b', 'c', 'd', 'e')

print(tuple1)
print(tuple2)

    #Zip function
tuple3 = zip(tuple1, tuple2)
print(tuple3) #<zip object at 0x000001DB7914DC00>
print(list(tuple3)) 


#Hvorfor bruge tuples
#-Er hurtigere end list
#-Når man ikke ønsker sin data ændret

print(type(tuple1)) #<class 'tuple'>

t= (2)
print(type(t)) #<class 'int'>

t1= (2,)
print(type(t1)) #<class 'tuple'>
a =['a', 'b', 'c', 'd', 'e','f'] #list

print(a[1:5]) #['b', 'c', 'd', 'e']                1
print(a[:2])  #['a', 'b']                          2
print(a[4:])  #['e', 'f']                          3
print(a[3:4]) #['d']                               4
print(a[::2]) #['a', 'c', 'e']                     5
print(a[::-1]) #['f', 'e', 'd', 'c', 'b', 'a']     6


b =('a1', 'b1', 'c1', 'd1', 'e1','f1')
print(b[::-1]) #('f', 'e', 'd', 'c', 'b', 'a')     7


#forklaring: a[start:stop:step] er det samme som a[slice(start, stop, step)]
#- er bagfra

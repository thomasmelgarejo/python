#how to make your classes iterable.
#Generator returnere en "lazy" iterator, den gemmer ikke data i memory (modsat lister), 
# hvilket gør at man kan arbejde med store filer

#Return vs Yield: 
# Return: If you execute a function again it starts from beginning
# Yield: The execution begins from where it was previously paused
class Compute:
    def __iter__(self): #Bruger dunder metoden
        pass

    def infinite_sequence():
        num = 0
        while True:
            yield num
            num += 1


    #for i in infinite_sequence():
    #    print(i, end=" ")

    gen = infinite_sequence()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
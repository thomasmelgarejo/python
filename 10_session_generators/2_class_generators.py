#how to make your classes iterable.
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
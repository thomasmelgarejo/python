import math
#how to make your classes iterable.
#Generator returnere en "lazy" iterator, den gemmer ikke data i memory (modsat lister), 
# hvilket gør at man kan arbejde med store filer
#an Iterable is just an object capable of returning its members one at a time.

#Return vs Yield: 
# Return: If you execute a function again it starts from beginning
# Yield: The execution begins from where it was previously paused

#Åbner txt fil og loader til csv_gen
pathToFile ="C:\\Users\\thoma\\Dropbox\\Thomas Dropbox\\KEA\\4 SEMESTER\\PYTHON\\PROGRAMMER\\10_session_generators\\filnavn.txt"
csv_gen = open(pathToFile,"r")

#Dvs csv_gen indeholder nu den fulde fil, som ses herunder
for line in csv_gen: 
    print(line)

#"generator expression" også kaldet "generator comprehension"
csv_gen2 = (row for row in open(pathToFile))
print(csv_gen2) #<generator object <genexpr> at 0x0000026935F49510>

#next() 
print(next(csv_gen2)) #anna1;kurt1;Peter1;Hans1;Soeren1;Leif1;
print(next(csv_gen2)) #anna2;kurt2;Peter2;Hans2;Soeren2;Leif2;


# #send()
# def generator1(n=None):
#     for item in range(n):
#         n = yield n

# g = generator1(3)
# print(next(g))
# print(next(g))

# g2 = generator1(5)
# print(next(g2))
# print(g2.send(4))


def num(number):
    while True:
        number *=2 
        number =yield number #En funktion der indeholder yield bliver automatisk til en generatorfunktion

n = num(2)
print(next(n))      #4
print( n.send(10))  #20

# def genr():
#     yield 1
#     yield 2
#     yield 3

# ga = genr()

# for line in ga:
#     print(line)

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1 # <<<<<<<<<<

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


test = is_prime(7)
print("is_prime: " + str(test))

solve_number_10()

# send() #Sender til generator
# throw() #til exception
# close() #lukker generator
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
def printFile():
    for line in csv_gen: 
        print('for loop: ', line)

# printFile()


#generator function****************************************************************

def generatorFunc(path):
    for line in open(path,"r"):
        yield line

# print(generatorFunc(pathToFile))
# print(next(generatorFunc(pathToFile)))
# print(next(generatorFunc(pathToFile)))


#generator expression ************************************************************** 
#også kaldet "generator comprehension"
#next()

csv_gen2 = (row for row in open(pathToFile))

# print(csv_gen2) #<generator object <genexpr> at 0x0000026935F49510>
# print(next(csv_gen2)) #anna1;kurt1;Peter1;Hans1;Soeren1;Leif1;
# print(next(csv_gen2)) #anna2;kurt2;Peter2;Hans2;Soeren2;Leif2;


# #send()***********************************************************

def generator4(number):
    while True:
        number *= 2 
        number = yield number

g4 = generator4(4)
g4.send(None)
# print(g4.send(5))
# print(g4.send(100))

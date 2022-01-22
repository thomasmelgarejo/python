class Dog: # class name uppercase

# Class attribute (ala global variable)    
    species = "Canis familiaris" 

#instance attributes
    def __init__(self, name, age): 
        self.name = name
        self.age = age

#dunder methood
    def __str__(self): 
        return f"Her er navnet på hunden: {self.name} med alder {self.age}, den har racen {self.species}"

#instance metode
    def visernavn(self, sound): 
        return f"Metode: Hundens navn {self.name} og lyd fra hund {sound}"

#instanciate hunde object
dogObj = Dog("Otto", 3)
#print(dogObj)

#Ændre navn på attributten otto (mutable)
dogObj.name = "Otto2" 
# print('dogObj.name: ',dogObj.name) 

#Kalder instance Metode med en parameter
objMilner = Dog("Milner", 6)
# print('objMilner: ', objMilner.visernavn("vufvuf"))

#**********************************************************************
#**********                Ny Klasse                     **************
#**********************************************************************

#Child klasse af Dog, har tilføjet en attribute mere "color"
class DogChild1(Dog): 
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self): 
        return f"Dogchild1 navn{self.name} og farven er {self.color}"

#Overload af metode
    def visernavn(self,sound, antalBen):
        return f"Lyd: {sound} Antal ben: {antalBen}"

dogChildObj = DogChild1("Karl",12,"Red")
#print(dogChildObj)

print(dogChildObj.visernavn("vurf", 4))

#Anden Child klasse af Dog, har tilføjet en attribute mere "hight"
class DogChild2(Dog): 
    def __init__(self, name, age, color, hight):
        self.name = name
        self.age = age
        self.color = color
        self.hight = hight

    def __str__(self): 
        return f"Dogchild2 navnet er {self.name} og farven er {self.color} og højden {self.hight}"

dogChildChildObj = DogChild2("Karl",12,"Red",50)
#print(dogChildChildObj)

#Child af childKlasse af Dog
class DogChildChild(DogChild2):
    
    def __init__(self, name, age, color, hight, shape):
        self.name = name
        self.age = age
        self.color = color
        self.hight = hight
        self.shape = shape
    
    def __str__(self): 
        return f"DogChildChild navn er {self.name} og den højde er{self.hight} og dens form er {self.shape}"

objChildChild = DogChildChild("Bob",4,"red",45,"rund")
#print(objChildChild)

#isinstance(), Tager 2 parameter; tjekker om object tilhøre klasse
#print(isinstance(objChildChild, Dog)) #true
#print(isinstance(objChildChild, DogChild2)) #true
#print(isinstance(objChildChild, DogChildChild)) #true
#print(isinstance(objChildChild, DogChild1)) #false

#type() returner hvilken klasse object tilhøre
#print(type(objChildChild)) #<class '__main__.DogChildChild'>

#super kalder her parent klasse metoden
class DogChild3(Dog):
    def visernavn(self, sound="bak bak"):
        return super().visernavn(sound)

objChild3 = DogChild3("Vuffer",22)

# print(objChild3.visernavn()) #bak bak
# print(objChild3.visernavn("lurf lurf")) #lurf lurf
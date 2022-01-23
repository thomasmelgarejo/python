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
print(dogObj)

#Ændre navn på attributten otto (mutable)
dogObj.name = "Otto2" 
# print('dogObj.name: ',dogObj.name) 

#Kalder instance Metode med en parameter
objMilner = Dog("Milner", 6)
# print('objMilner: ', objMilner.visernavn("vufvuf"))

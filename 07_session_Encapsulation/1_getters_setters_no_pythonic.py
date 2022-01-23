#Encapsulation IKKE pythonic måde
class Myclass:
    
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return f"Myclass: {self.x}"
    
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x

# objMyclass1 = Myclass(100)
# print(objMyclass1.get_x())

#Tilføjer funktionalitet
class Myclass2:
    
    def __init__(self, x):
        self.set_x(x)
    
    def __str__(self):
        return f"Myclass2: {self.x}"
    
    def get_x(self):
        return self.__x
   
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

# objMyclass2 = Myclass2(1001)
# print(objMyclass2.get_x())


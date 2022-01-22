class Myclass:
    def __init__(self,x):
        self.x = x
    
    def __str__(self):
        return f"Myclass: {self.x}"


objMyclass = Myclass(5)
print(objMyclass)


class Myclass2:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return f"Myclass2: {self.x}"
    
    #@property
    def x(self):
        return self.__x
    
    #@x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

# objMyclass2 = Myclass2(5000)
# print(objMyclass2)

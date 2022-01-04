class Myclass:
    
    def __init__(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x


class Myclass2:
    
    def __init__(self, x):
        self.set_x(x)
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x




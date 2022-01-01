class Myclass:
    def __init__(self, x):
        self.x = x
    
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x

class PytonicWay:
    
    def __init__(self, *args):
        self.number = args[0]

    @property
    def number(self):
        return self.__number #__ meaning-> the interpreter replaces this name with _classname__number

    @number.setter
    def number(self, number):
        self.__number = number


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


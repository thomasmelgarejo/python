class Student:

    def __init__(self, name, age, ):
        self.name = name
        self.age = age


class ChildStudent(Student):

    def __init__(self, name, age, color):
        self.color = color
        Student.__init__(self, name, age)

    def __str__(self):
        return f"Navnet er {self.name}, Alderen er {self.age}, Farven er {self.color}"

    
objchild = ChildStudent("Kurt",33, "green")
#print(objchild)

#Child af en Child
class ChildChildStudent(ChildStudent):
    def __init__(self,name, age, color, glasses):
        self.glasses = glasses
        # Student.__init__(self, name, age)
        ChildStudent.__init__(self, name, age, color)

    def __str__(self):
        return f"Navnet er {self.name}, Alderen er {self.age}, Farven er {self.color}, Briller {self.glasses}"

objchildchild = ChildChildStudent("Kurt",33, "green", True)
# print(objchildchild)


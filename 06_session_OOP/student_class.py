class Student:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def metodenavn(self, status):
        print(f"Studentens status er {status}")


objstudent = Student("Peter", 34, "male")
objstudent.metodenavn("aktiv")




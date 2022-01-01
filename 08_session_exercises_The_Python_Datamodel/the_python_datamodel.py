class Deck:
    def __init__(self):
        self.cards = ['A', 'K', 4, 7]

    def __getitem__(self, key):
        return self.cards[key]

    def __repr__(self):
        return f'{self.__dict__}'

    def __len__(self):
        return len(self.cards)



d = Deck()
print("getitem: " + d[1])
print("len: " + str(len(d)))
print("str: " + str(d)) #informal til at vise objecter som text
print("repr: " + repr(d)) # compute the “official” string med ''. representation of an object til debugging

#hejsa = "kong gulerod"

#print("{hejsa}  jojo") #{hejsa}  jojo
#print(f"{hejsa}  jojo") #kong gulerod  jojo


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"fuk you {self.name} med din skide alder paa: {self.age}" #svarre til tostring i java model klasse

persin1 = person(name="kaj", age=2)
print(persin1) #fuk you kaj med din skide alder paa: 2
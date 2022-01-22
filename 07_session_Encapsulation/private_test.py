class A_Class:
    def __init__(self, privatAtt, publicAtt):
        self.__privatAtt = privatAtt
        self.publicAtt = publicAtt

    def __str__(self):
        return f"__str__; public: {self.publicAtt}, Private: {self.__privatAtt}"

    def funk(self):
        return f"FUNK Private: {self.publicAtt} og {self.__privatAtt}"

    def __funk1(self):
        return f"FUNK Private: {self.publicAtt}"


# objA_class = A_Class(3,6)
# print(objA_class)







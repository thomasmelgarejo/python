class AprivateClass:
    def __init__(self, privatAtt, publicAtt):
        self.__privatAtt = privatAtt
        self.publicAtt = publicAtt

    def __str__(self):
        return f"{self.publicAtt}"




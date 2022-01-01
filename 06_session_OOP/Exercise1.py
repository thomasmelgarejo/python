#Bank exercise

class Bank:
    def __init__(self):
        self.accounts = []



class Account:
    def __init__(self, accountNumber, saldo):
        self.accountNumber = accountNumber
        self.saldo = saldo

    def __str__(self): #dunder methood
        return f"Her er navnet: {self.name} and {self.accountNumber}"

class Costumer:
    def __init__(self, name, accountNumber):
        self.name = name
        self.accountNumber = accountNumber

    def __str__(self): #dunder methood
        return f"Her er navnet: {self.name} and {self.accountNumber}"
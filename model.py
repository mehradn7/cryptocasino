# A class describing the model of the game

class Model:
    def __init__(self):
        self.balance = 100
        self.mise = 1
        self.case = 0

    def caseChosen(self, caseNumber):
        self.case = caseNumber

    def miseChosen(self, mise):
        self.mise = mise

    def tour(self, caseSortie):
        if self.case == caseSortie:
            self.balance += self.mise * 15
        print("Balance :", self.balance)
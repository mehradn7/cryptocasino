class Model: # mettre dans un fichier à part
    def __init__(self):
        self.gains = 100
        self.mise = 1
        self.case = 0

    def caseChosen(self, caseNumber):
        self.case = caseNumber

    def miseChosen(self, mise):
        self.mise = mise

    def tour(self, caseSortie):
        if self.case == caseSortie:
            self.gains += self.mise * 15
        print("Money :", self.gains)
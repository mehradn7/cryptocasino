class Model: # mettre dans un fichier à part
    def __init__(self):
        self.gains = 100
        self.mise = 0
        self.case = 0

    def caseChosen(self, i):
        self.case = i
        print("Model.caseChosen : ", i)


import rng.randomNumber as randomNumber

# A class describing the model of the game
class Model:
    bet_values = [10, 20, 50, 100]

    def __init__(self, prng_mode = "lfsr"):
        self.balance = 100
        self.mise = Model.bet_values[0]
        self.case = 0

        self.prng = randomNumber.PRNG(prng_mode)
        self.nextValue = -1

    def caseChosen(self, caseNumber):
        self.case = caseNumber

    def miseChosen(self, mise):
        self.mise = mise

    def play_turn(self):
        if self.case == self.nextValue:
            self.balance += self.mise * 15
        else:
            self.balance -= self.mise
        print("Balance :", self.balance)

    def compute_next_value(self):
        self.nextValue = self.prng.randomNumber_4bits()
        return self.nextValue

import rng.randomNumber as randomNumber

# A class describing the model of the game
class Model:
    bet_values = [10, 20, 50, 100]

    def __init__(self, prng_mode="lfsr"):
        self.balance = 100
        self.bet = Model.bet_values[0]
        self.pocket = 0

        self.prng = randomNumber.PRNG(prng_mode)
        self.nextValue = -1

    def set_pocket(self, pocket_number):
        self.pocket = pocket_number

    def set_bet(self, bet):
        self.bet = bet

    def play_turn(self):
        if self.pocket == self.nextValue:
            self.balance += self.bet * 15
        else:
            self.balance -= self.bet

    def compute_next_value(self):
        self.nextValue = self.prng.randomNumber_4bits()
        return self.nextValue

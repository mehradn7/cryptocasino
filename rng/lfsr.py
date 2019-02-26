import utils

class Lfsr:
    def __init__(self):
        self.state = [0, 0, 1, 0, 1]
    
    def nextBit(self):
        next = (self.state[0] + self.state[1] + self.state[3]+ self.state[4])%2
        self.state = [next] + self.state
        self.state = self.state[:-1]
        return next

    def getRandomNumber(self):
        # 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1
        numbers = []
        for i in range(4):
            numbers.append(self.nextBit())
        return utils.bitToInt(numbers)
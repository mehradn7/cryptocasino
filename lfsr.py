class Lfsr:
    def __init__(self):
        self.state = [1, 0, 1, 0, 0]
    
    def nextBit(self):
        next = (self.state[0] + self.state[3] + self.state[2])%2
        self.state.append(next)
        self.state = self.state[1:]
        return next

    def next32(self):
        # 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1
        numbers = []
        for i in range(32):
            numbers.append(self.nextBit())
        return numbers
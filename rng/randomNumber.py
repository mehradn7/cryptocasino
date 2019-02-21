import rng.lfsr as lfsr
import utils
import random as r

class PRNG:
    def __init__(self, mode):
        self.mode = mode
        if (mode=="lfsr"):
            self.lfsr = lfsr.Lfsr()
        if (mode=="mt_truncated"):
            self.nbDropped = 3
        else:
            self.nbDropped = 0
        self.nbOutput = 0
        self.stored = 0

    def randLFSR(self):
        return self.lfsr.getRandomNumber()

    def randMt(self):
        if ((self.nbOutput % (8 - self.nbDropped)) == 0):
            self.stored = r.getrandbits(32)
        output = self.stored & 0xf
        self.stored = self.stored >> 4
        self.nbOutput += 1
        return output

    def randomNumber_4bits(self):
        if (self.mode == "lfsr"):
            return self.randLFSR()
        else:
            return self.randMt()

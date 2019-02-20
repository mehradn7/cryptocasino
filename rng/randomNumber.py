import rng.lfsr as lfsr
import utils
import random as r

class PRNG:
    def __init__(self, mode):
        self.mode = mode
        if (mode=="lfsr"):
            self.lfsr = lfsr.Lfsr()

        else:
            self.nbOutput = 0
            self.stored = 0

    def randLFSR(self):
        return self.lfsr.getRandomNumber()

    def randMt(self, k = 0):
        # k = nombre de sorties jetées
        if ((self.nbOutput % (8 - k)) == 0):
            self.stored = r.getrandbits(32)
        output = self.stored & 0xf
        self.stored = self.stored >> 4
        self.nbOutput += 1
        return output

    def randomNumber_4bits(self):
        if (self.mode == "lfsr"):
            return self.randLFSR()
        elif(self.mode == "mt_truncated"):
            return self.randMt(k = 3)
        else:
            return self.randMt()


    
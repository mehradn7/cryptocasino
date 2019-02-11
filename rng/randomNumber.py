import rng.lfsr as lfsr
import rng.mersenneTwister as mersenneTwister
import utils

class PRNG:
    def __init__(self, mode, seed = 5489):
        if (mode=="lfsr"):
            self.generator = lfsr.Lfsr()
        else:
            self.generator = mersenneTwister.Mt(seed)
        self.precalculated = []

    def randomNumber_4bits(self):
        if (self.precalculated == []):  # on calcule par paquets de 32 bits pour avoir une généralisation facile avec le mersenne twister
            self.precalculated = utils.intToBits(self.generator.getRandomNumber(), 32)
        n = utils.bitToInt(self.precalculated[0:4])
        self.precalculated  = self.precalculated[4:]
        return n
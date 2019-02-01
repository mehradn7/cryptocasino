import lfsr

def bitToInt(bits):
    n = 0
    for i in range (len(bits)):
        n+= bits[i]*(2**i)
    return n

def intToBits(n, length):
    bits = []
    for i in range(length):
        bits.append(n%2)
        n = n//2
    return bits

class PRNG:
    def __init__(self, mode):
        if (mode=="lfsr"):
            self.generator = lfsr.Lfsr()
        self.precalculated = []

    def randomNumber_4bits(self):
        if (self.precalculated == []):  # on calcule par paquets de 32 bits pour avoir une généralisation facile avec le mersenne twister
            self.precalculated = self.generator.next32()
        n = bitToInt(self.precalculated[0:4])
        self.precalculated  = self.precalculated[4:]
        return n
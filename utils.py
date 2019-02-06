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
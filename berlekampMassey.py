""""Implementation inspirée de wikipédia"""

def BerlekampMasseyAlgorithm(stream):
    N = len(stream)

    # polynoms
    S = [stream[i] for i in range(N)]
    B = [1]+[0 for _ in range(N-1)]
    C = [1]+[0 for _ in range(N-1)]

    L = 0 # length of minimal lfsr
    m = -1 # nombre d'iter depuis la dernière update

    for n in range(N):
        # calculate discrepancy
        d = S[n]
        for i in range(1, L+1):
            d ^= C[i] & S[n-i]
        # discrepancy is zero; annihilation continues
        if d==1:
            print("a")
            T = [C[i] for i in range(len(C))]
            for i in range (N-n+m):
                C[i+n-m] ^= B[i]
            if (L <= n/2):
                L = n+1-L
                m = n
                B = T
    return L, C



stream = [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1] 
L, C = BerlekampMasseyAlgorithm(stream)
print('Solution is '), #Output registers 
print(L, ", ", C)
import random as r

# https://github.com/james727/MTP
# http://www.quadibloc.com/crypto/co4814.htm

class Mt(object):
	def __init__(self, seed = 5489):
		self.state = [0]*624
		self.f = 1812433253
		self.m = 397
		self.u = 11
		self.s = 7
		self.b = 0x9D2C5680
		self.t = 15
		self.c = 0xEFC60000
		self.l = 18
		self.index = 624
		self.lower_mask = (1<<31)-1		#011111111...
		self.upper_mask = 1<<31			#100000000...

		# update state
		self.state[0] = seed
		for i in range(1,624):
			self.state[i] = self.int_32(self.f*(self.state[i-1]^(self.state[i-1]>>30)) + i)

	def twist(self):
		for i in range(624):
			temp = self.int_32((self.state[i]&self.upper_mask)+(self.state[(i+1)%624]&self.lower_mask))
			# temp = fonction de state[i] et state[i+1]
			temp_shift = temp>>1	
			if temp%2 != 0:
				temp_shift = temp_shift^0x9908b0df
			#tempshift = function de temp
			self.state[i] = self.state[(i+self.m)%624]^temp_shift	# state[i+397] xor tempshift
		self.index = 0
	#remarque : à partir de state[i], state[i+1], state[i+397] (valeurs anciennes jusqu'à i=226), on trouve le nouveau state[i]

	def getRandomNumber(self):
		if self.index >= 624:
			self.twist()
		y = self.state[self.index]
		y = y^(y>>self.u)
		y = y^((y<<self.s)&self.b)
		y = y^((y<<self.t)&self.c)
		y = y^(y>>self.l)
		self.index+=1
		return self.int_32(y)

	def int_32(self, number):
		return int(0xFFFFFFFF & number)

def test():
    rng = Mt(1)
    r.seed(1)
    for i in range(10):
        print(rng.getRandomNumber(), " == ", r.getrandbits(32))

# test()
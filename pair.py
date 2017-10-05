class Pair(object):
	'''Represents a 2-tuple'''

	def __init__(self, a, b):
		'''Create the 2-tuple'''
		self.a = a
		self.b = b

	def __repr__(self):
		return 'Pair({0}, {1})'.format(self.a, self.b)

	def __str__(self):
		return'<{0}, {1}>'.format(self.a, self.b)

	def __len__(self):
		return 2

	def __add__(self, other):
		return Pair(self.a + other.a, self.b + other.b)
	
	def as_tuple(self):
		return self.a, self.b

	def __sub__(self, other):
		print('my __sub__ method')
		return Pair(self.a - other.a, self.b - other.b)

	def __mul__(self, other):
		print('my __mul__ method')
		return Pair(self.a * other.a, self.b * other.b)

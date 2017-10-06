from __future__ import print_function

class myIterator(object):
	"""docstring for myIterator"""
	def __init__(self, a, b,):
		self.a = a
		self.b = b
		self._index = 0
		return self
		

	def next(self):
		if self._index==0:
			self._index+=1
			return self.a
		elif self._index==1:
			self._index+=1
			return self.b
		else:
			raise IndexError


class MySeq(object):
		def __init__(self, a, b):
			self.a = a
			self.b = b
			

		def __iter__(self):
			return myIterator(self)

#if __name__ == '__main__':
seq = MySeq(1,2)
for i in seq:
		print(i)



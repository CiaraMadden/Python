
class Person(object):

	def __init__(self, name, address):
		self.name = name #declaring a name for each object
		self.address = address #declaring an address for each object
	def description(self):
		return '{}, of {}'.format(self.name, self.address)

if __name__=='__main__':

	p1 = Person('Sean', 'Galway')
	p2 = Person('Mary', 'Cork')
	print p1.description()


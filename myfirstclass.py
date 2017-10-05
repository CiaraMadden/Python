'''importing print statement'''
from __future__ import print_function


class Dog(object):
	
	def __init__(self):
		self.string='Woof Woof'

	def bark(self):
		print(self.string)

if __name__=='__main__':
	object = Dog()
	object.bark()

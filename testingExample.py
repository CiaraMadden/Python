from __future__ import print_function
import hello
import unittest

class MyTest(unittest.TestCase):
	def testhello(self):
			self.assertEquals('Hello world.', hello.hello())


if __name__ == '__main__':
	unittest.main()




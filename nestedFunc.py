from __future__ import print_function

def getHelloWorldPrinter():
	def doPrinting():
		print(string)
	string = 'Hello World'
	return doPrinting

def factorial(num):
	factorial = 1
	if num<0:
		print('Error')
	elif num==0:
		print('Factorial of 0 is 1')
	else:
		for i in xrange(1, num+1):
			factorial = factorial * i
		print('The factorial of ',num,' is ',factorial)
	

if __name__=='__main__':
	f=getHelloWorldPrinter()
	print(f)
	f()
	factorial(5)

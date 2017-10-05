from __future__ import print_function



def monitor(f):
	def wrapper(*args, **kwargs):
		print("Calling function")
		return f(*args, **kwargs)	
	return wrapper


@monitor
def double(x):
	return x*2



if __name__=='__main__':
	print(double((2,4)))

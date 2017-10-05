from __future__ import print_function
import random
import time

def randomGen():

	result = []
	result.append(random.randrange(0xFFFFFFFF))
	result.append('-')
	result.append(int(time.time()))
	
	map(str, result)
	resultnew = ''.join(result)
	

	return result

if __name__=='__main__':

	print(randomGen())

	

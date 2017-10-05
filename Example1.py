""" 
Example 1 
"""

from __future__ import print_function

__author__="Ciara Madden"
__version__="0.1"
__date__="3-10-2017"



def skipSecond(data):

	result=[]

	#skip every second word	
	for i in xrange(0, len(data), 2):
		result.append(data[i])
	return result

def convertsingle(data):
	
	result=[]

	#convert to single string
	result.append(' '.join(data))
	return result

def caps(data):

	result=[]

	#to get to uppercase
	result.append(data[0].upper())
	
	return result

if __name__=='__main__':

	#definig the list 
	list=["This", "mostly", "is", "some", "text", "which", "I", "would", "want", "now", "to", "simplify"]


	print(skipSecond(list))
	print(convertsingle(list))
	print(caps(convertsingle(list)))

from __future__ import print_function

def flattenTwoNestedTuple(outsideTuple):
	for insideTuple in outsideTuple:
		for insideVal in insideTuple:
			yield insideVal
						

def flattenMultiNestedTuple(outsideTuple):
	for x in outsideTuple:
		if isinstance(x, tuple):
			yield x
			for y in flattenMultiNestedTuple(x):
				yield y

def flattenMul(turtles):
	for sub in turtles:
		if type(sub)==tuple:
			for val in flattenMul(sub):
				yield val
		else:
			yield sub



if __name__ == '__main__':
	
	#tv = ((0,1),(2,3,4),(9,10))
	#flattened=flattenTwoNestedTuple(tv)

	tvTwo = ((0,1),(2,(3,3,3),3,4),(9,10))
	flattenedTwo = flattenMul(tvTwo)

	#for i in flattened:
	#	print(i)

	for i in flattenedTwo:
		print(i)


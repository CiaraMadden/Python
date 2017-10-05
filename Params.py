"""function with and without default
"""

def default_Values(a='Hello ', b='there ', c='how ', d='are ', e='you ', f='!'):
	print(a + b + c + d + e + f)

def show(name, location='Dublin', *args, **kwargs):
	print(name, location, args, kwargs)

def show2(name,location='Dublin', *pos, **kw):
	print(name,location,pos,kw)


if __name__=='__main__':

	default_Values()
	default_Values(b='Ciara ')

	show('Ciara Madden')
	show('Ciara', 'Dublin', 'Ammeon')
	show('Ciara Madden', age='23', hometown='Laois', favcol='green')

	

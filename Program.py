from __future__ import print_function
from pair import Pair


p1 = Pair(1,2)
p2 = Pair(2,4)
print(p1.__mul__(p2))
print(p1.__sub__(p2))
print(p1 * p2)
print(p1 - p2)

p1.next()
p2.next()
from z1 import *

a = Bool('a')
b = Bool('b')
c = Bool('c')

s = Solver()

#s.add('(a&~b)|~c')
#s.add(Or(And(a, Not(b)), Not(c)))

print(s.check())
print(s.model())
